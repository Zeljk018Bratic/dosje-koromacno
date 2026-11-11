## Konačna PowerShell skripta (AMS Scraper s pravim API endpointima)

Ova verzija koristi točne endpointe koje si pronašao na stranici `zrak.infomedica.hr`. Skripta dohvaća podatke za sva 4 plina (NO₂, SO₂, NO, NOx), izvlači zadnju izmjerenu vrijednost i sprema je u centralni CSV. Također, detektira negativne vrijednosti i šalje Telegram alarm.

**Napomena:** Budući da ne znamo točan format JSON odgovora, pretpostavio sam da vraća listu mjerenja s poljima `time` (ili `timestamp`) i `value`. Skripta je napisana tako da bude otporna na manje razlike u formatu.

```powershell
# ============================================================
# Koromačno AMS Scraper + Central Archive + Telegram Alarm
# LOKACIJA: b54fb46b-32b6-4d66-af03-2612faae6deb
# ============================================================

$ErrorActionPreference = "Continue"

# === POSTAVKE ===
$StationId       = "b54fb46b-32b6-4d66-af03-2612faae6deb"
$BaseUrl         = "https://zrak.infomedica.hr/v1/public/locations/$StationId/series"
$CentralCsv      = "C:\Users\zeljk\dosje-koromacno\data\ams_central.csv"
$AnomalyLog      = "C:\Users\zeljk\dosje-koromacno\data\ams_anomalies.log"
$PollIntervalMin = 60
$MaxRetries      = 5
$RetryDelaySec   = 3

# === TELEGRAM ALARM POSTAVKE ===
$TelegramToken   = "TVOJ_NOVI_TOKEN_OVDJE" # <-- OBAVEZNO REVOKEJ STARI I STAVI NOVI!
$TelegramChatId  = "TVOJ_CHAT_ID"          # <-- Tvoj osobni Chat ID

# Kreiraj folder ako ne postoji
$dataDir = Split-Path $CentralCsv
if (!(Test-Path $dataDir)) { New-Item -ItemType Directory -Path $dataDir -Force | Out-Null }

# Inicijaliziraj CSV header
if (!(Test-Path $CentralCsv)) {
    "timestamp_utc,timestamp_local,NO2,SO2,NO,NOx,status,anomaly_flag" | Out-File -FilePath $CentralCsv -Encoding utf8
}

function Write-Anomaly($msg) {
    $line = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') | $msg"
    Add-Content -Path $AnomalyLog -Value $line -Encoding utf8
    Write-Host "⚠ ANOMALIJA: $msg" -ForegroundColor Yellow

    # --- SLANJE TELEGRAM ALARMA ---
    if ($TelegramToken -ne "TVOJ_NOVI_TOKEN_OVDJE" -and $TelegramChatId -ne "TVOJ_CHAT_ID") {
        $tgUrl = "https://api.telegram.org/bot$TelegramToken/sendMessage"
        $body = @{
            chat_id = $TelegramChatId
            text    = "⚠ KOROMAČNO ALARM: $msg"
        }
        try {
            Invoke-RestMethod -Uri $tgUrl -Method Post -Body $body | Out-Null
            Write-Host "  ✈ Telegram alarm poslan." -ForegroundColor Cyan
        } catch {
            Write-Host "  ✕ Greška pri slanju Telegram alarma." -ForegroundColor Red
        }
    }
}

function Get-PollutantData {
    param([string]$Pollutant, [string]$Url)
    
    $headers = @{
        "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        "Accept"     = "application/json"
    }

    for ($i = 1; $i -le $MaxRetries; $i++) {
        try {
            $response = Invoke-RestMethod -Uri $Url -Method Get -Headers $headers -TimeoutSec 30
            
            # Provjeri je li odgovor lista i ima li elemenata
            if ($response -is [Array] -and $response.Count -gt 0) {
                # Uzmi zadnji element (najnovije mjerenje)
                $latest = $response[-1]
                
                # Pokušaj izvući vrijednost (prilagođeno za različite formate: value, val, itd.)
                $val = $null
                if ($null -ne $latest.value) { $val = $latest.value }
                elseif ($null -ne $latest.val) { $val = $latest.val }
                elseif ($null -ne $latest.concentration) { $val = $latest.concentration }
                else { $val = $latest } # Ako je samo broj
                
                return $val
            } else {
                Write-Host "  ⚠ Nema podataka za $Pollutant" -ForegroundColor DarkYellow
                return $null
            }
        }
        catch {
            $err = $_.Exception.Message
            if ($err -match "database is locked" -or $err -match "locked") {
                Write-Host "  ↻ Database locked – retry $i/$MaxRetries za $Pollutant..." -ForegroundColor DarkYellow
                Start-Sleep -Seconds $RetryDelaySec
            }
            else {
                Write-Host "  ✕ Greška API za $Pollutant: $err" -ForegroundColor Red
                return $null
            }
        }
    }
    Write-Host "  ✕ Max retries dostignut za $Pollutant" -ForegroundColor Red
    return $null
}

function Process-And-Archive {
    $nowUtc   = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
    $nowLocal = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

    # Dohvati podatke za svaki plin (range=24h da bude sigurno da uhvatimo zadnje)
    $no2 = Get-PollutantData -Pollutant "NO2" -Url "$BaseUrl`?pollutant=no2&range=24h"
    $so2 = Get-PollutantData -Pollutant "SO2" -Url "$BaseUrl`?pollutant=so2&range=24h"
    $no  = Get-PollutantData -Pollutant "NO"  -Url "$BaseUrl`?pollutant=no&range=24h"
    $nox = Get-PollutantData -Pollutant "NOx" -Url "$BaseUrl`?pollutant=nox&range=24h"

    # Ako su svi null, preskačemo ovaj ciklus
    if ($null -eq $no2 -and $null -eq $so2 -and $null -eq $no -and $null -eq $nox) {
        Write-Host "[$nowLocal] Nema podataka ni za jedan plin. Preskačem." -ForegroundColor Red
        return
    }

    $anomalyFlag = ""
    $status = "OK"

    # Detekcija negativnih vrijednosti
    if (($no2 -lt 0) -or ($so2 -lt 0) -or ($no -lt 0) -or ($nox -lt 0)) {
        $anomalyFlag = "NEGATIVE_VALUE"
        $status = "ANOMALY"
        Write-Anomaly "Negativne vrijednosti → NO2=$no2 SO2=$so2 NO=$no NOx=$nox"
    }

    Write-Host "[$nowLocal] NO2=$no2  SO2=$so2  NO=$no  NOx=$nox  [$status]" -ForegroundColor $(if($status -eq "OK"){"Green"}else{"Yellow"})

    # Upis u centralni CSV
    $line = "$nowUtc,$nowLocal,$no2,$so2,$no,$nox,$status,$anomalyFlag"
    Add-Content -Path $CentralCsv -Value $line -Encoding utf8
}

# === GLAVNA PETLJA ===
Write-Host "=== Koromačno AMS Central Archive pokrenut ===" -ForegroundColor Cyan
Write-Host "Lokacija ID: $StationId"
Write-Host "Interval: $PollIntervalMin min"
Write-Host ""

while ($true) {
    Process-And-Archive
    Write-Host "Sljedeća provjera za $PollIntervalMin min..." -ForegroundColor DarkGray
    Start-Sleep -Seconds ($PollIntervalMin * 60)
}