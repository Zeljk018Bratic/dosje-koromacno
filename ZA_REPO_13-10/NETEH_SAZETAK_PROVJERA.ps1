# =====================================================================
#  NETEH_SAZETAK_PROVJERA.ps1   —  13.10.2026.
#  Namjena:
#   1) hash lokalne kopije netehnickog sazetka + usporedba sa sluzbenom MZOZT kopijom
#   2) preuzimanje sluzbene kopije s MZOZT-a (arhiva)
#   3) CIŠĆENJE Evidence_Matrix.csv (udvostruceni redovi E-001..E-040)
#   4) dodavanje novih redova E-042, E-043, E-044
#  Pokretanje:  desni klik -> Run with PowerShell   (ili: powershell -ExecutionPolicy Bypass -File .\NETEH_SAZETAK_PROVJERA.ps1)
#  NAPOMENA: sve se radi s kopijama; original se ne prepisuje bez backupa.
# =====================================================================

$ErrorActionPreference = 'Stop'
$repo   = "C:\Users\zeljk\dosje-lf"
$arhiva = Join-Path $repo "docs\Arhiva"
$evid   = Join-Path $repo "docs\Evidence"
$logDir = Join-Path $env:LOCALAPPDATA "dosje-lf-logovi"
New-Item -ItemType Directory -Force -Path $arhiva,$evid,$logDir | Out-Null
$stamp  = Get-Date -Format "yyyy-MM-dd_HHmm"
$log    = Join-Path $logDir "NETEH_PROVJERA_$stamp.log"

function W($m){ Write-Host $m; Add-Content -LiteralPath $log -Value $m -Encoding UTF8 }

W "=== 1) HASH LOKALNE KOPIJE ==="
$mojPdf = $null
$kand = Get-ChildItem -LiteralPath $arhiva -Filter "NETEHNI*.pdf" -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -notlike "MZOZT_*" } | Select-Object -First 1
if ($kand) { $mojPdf = $kand.FullName }
$sluzbeniHash = "431B0D03DFD76474F79F08450F2B8F57AE9000C963359F5C8FE8C6FF75DED146"
$sluzbenaVel  = 2199766

if ($mojPdf -and (Test-Path -LiteralPath $mojPdf)) {
    W ("pronadjena lokalna kopija: {0}" -f (Split-Path $mojPdf -Leaf))
    $h = (Get-FileHash -Algorithm SHA256 -LiteralPath $mojPdf).Hash
    $v = (Get-Item -LiteralPath $mojPdf).Length
    W ("lokalno : {0}  {1} bajtova" -f $h,$v)
    W ("sluzbeno: {0}  {1} bajtova" -f $sluzbeniHash,$sluzbenaVel)
    if ($h -eq $sluzbeniHash) {
        W "REZULTAT: IDENTICNO -> to je sluzbena MZOZT kopija (javno dostupna). Nema potrebe za duplikatom u repozitoriju."
    } else {
        W "REZULTAT: RAZLICITO -> MOGUCA DRUGA VERZIJA (npr. puna Studija ili nacrt). JAVI QWENU PRIJE NEGO STO NESTO POSALJES."
    }
} else {
    W "NISAM NASAO lokalnu kopiju na: $mojPdf"
    W "Ako je drugdje, promijeni $mojPdf na tocnu putanju i pokreni ponovno."
}

W ""
W "=== 2) PREUZIMANJE SLUZBENE KOPIJE (MZOZT) ==="
$url = "https://mzozt.gov.hr/UserDocsImages//UPRAVA-ZA-PROCJENU-UTJECAJA-NA-OKOLIS-ODRZIVO-GOSPODARENJE-OTPADOM/Puo//14_08_2026_Sa%C5%BEetak_tvornica_cementa_Koroma%C4%8Dno.pdf"
$out = Join-Path $arhiva "MZOZT_Netehnicki_sazetak_Koromacno_14-08-2026.pdf"
try {
    Invoke-WebRequest -Uri $url -OutFile $out -UserAgent "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" -TimeoutSec 120
    $h2 = (Get-FileHash -Algorithm SHA256 -LiteralPath $out).Hash
    W ("preuzeto: {0} bajtova  SHA256 {1}" -f (Get-Item -LiteralPath $out).Length,$h2)
    if ($h2 -ne $sluzbeniHash) { W "UPOZORENJE: hash preuzete datoteke ne odgovara hashu iz sandboxa (moguce je da je MZOZT zamijenio datoteku). Sacuvaj obje i javi." }
} catch {
    W ("GREŠKA pri preuzimanju: {0}" -f $_.Exception.Message)
}

W ""
W "=== 3) CISCENJE Evidence_Matrix.csv (duplikati) ==="
$csv = Join-Path $evid "Evidence_Matrix.csv"
if (Test-Path -LiteralPath $csv) {
    $bakDir = Join-Path $env:LOCALAPPDATA "dosje-izolacija-INTERNO"
    New-Item -ItemType Directory -Force -Path $bakDir | Out-Null
    $bakFile = Join-Path $bakDir "Evidence_Matrix.csv.bak_$stamp"
    Copy-Item -LiteralPath $csv -Destination $bakFile -Force
    W "backup: $bakFile"

    $raw = Get-Content -LiteralPath $csv -Encoding UTF8
    # preskoci prazne retke i ponovljena zaglavlja
    $head = $raw | Where-Object { $_ -match '^"ID","Datum_od"' } | Select-Object -First 1
    $data = $raw | Where-Object { $_ -match '^"E-\d+"' }

    W ("ucitani podatkovni redovi: {0}" -f ($data | Measure-Object).Count)

    # deduplikacija po ID-u: zadrzi redak s NAJDUZIM opisom (polje 7)
    $byId = @{}
    foreach ($line in $data) {
        if ($line -match '^"(E-\d+)"') {
            $id = $Matches[1]
            if (-not $byId.ContainsKey($id)) { $byId[$id] = $line }
            else { if ($line.Length -gt $byId[$id].Length) { $byId[$id] = $line } }
        }
    }
    $clean = $byId.Keys | Sort-Object { [int]($_ -replace 'E-','') } | ForEach-Object { $byId[$_] }
    W ("jedinstvenih ID-eva: {0}  (prije: {1})" -f $clean.Count, ($data | Measure-Object).Count)

    # === 4) DODAVANJE E-042 / E-043 / E-044 ===
    $noviCsv = Join-Path $evid "E-MATRIX_NOVI_REDOVI_E042-E044.csv"
    $dodano = 0
    if (Test-Path -LiteralPath $noviCsv) {
        $nove = Get-Content -LiteralPath $noviCsv -Encoding UTF8 | Where-Object { $_ -match '^"E-\d+"' }
        foreach ($n in $nove) {
            if ($n -match '^"(E-\d+)"') {
                $id = $Matches[1]
                if ($byId.ContainsKey($id)) { W "preskacem $id (vec postoji)" }
                else { $clean += $n; $byId[$id] = $n; $dodano++; W "dodano: $id" }
            }
        }
    } else {
        W "NISAM NASAO $noviCsv — novi redovi nisu dodani (prvo kopiraj tu datoteku iz ZA_REPO paketa)."
    }

    # spremanje: UTF8 bez BOM-a, LF
    $sadrzaj = (@($head) + $clean) -join "`n"
    [System.IO.File]::WriteAllText($csv, $sadrzaj + "`n", (New-Object System.Text.UTF8Encoding($false)))
    W ("zapisano: {0} redova (zaglavlje + {1} dokaza, novo dodanih {2})" -f (1 + $clean.Count), $clean.Count, $dodano)
    W ("SHA256 nove matrice: {0}" -f (Get-FileHash -Algorithm SHA256 -LiteralPath $csv).Hash)
} else {
    W "NISAM NASAO $csv"
}

W ""
W "=== GOTOVO ==="
W "Sljedece: posalji QWENU (1) hash lokalne kopije, (2) SHA256 nove matrice, (3) broj redova."
W "Ne commitaj dok ti Qwen ne potvrdi da je matrica cista."
