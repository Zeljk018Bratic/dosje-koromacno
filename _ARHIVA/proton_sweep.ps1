<#
================================================================================
 PROTON_SWEEP.PS1  -  v1.1  (13.10.2026)
 BajteBrothers / dosje-koromacno  -  SIGURNOSNA HIGIJENA, NIJE DOKAZ U DOSJEU
================================================================================
 Sto radi:
   0) STANJE  - SSD/HDD, TRIM, BitLocker, volumeni, otvoreni preglednici
   1) SCAN    - trazi ostatke datoteke s Proton recovery phrase:
                a) po IMENU na svim pogonima (profili, Downloads, OneDrive...)
                b) po SADRZAJU tekstualnih datoteka (.txt/.md/.json/.html/.eml)
                c) SIROVO po bazama preglednika (Chrome/Edge/Firefox "History")
                   -> tu stoji povijest preuzimanja, otkriva je li skinuto 2x
                d) popis MALIH PDF-ova u Downloads/Desktop (za rucnu provjeru
                   ako je datoteka preimenovana)
   2) CISTI   - nepovratno prepisuje i brise pogotke (default 3 prolaza:
                random, random, nule) + Recycle Bin na svim pogonima
   3) PRAZNI  - temp / Recent / JumpList / thumbcache / INetCache / prefetch
   4) CIPHER  - "cipher /w:X:" = brise SLOBODAN prostor (ono "opet izbrisi
                izbrisano"), 3 prolaza po volumenu, traje satima

 Sto NE radi:
   - NE cita i NE sprema sadrzaj nadenih datoteka (samo putanja, velicina, hash)
   - NE dira dosje/, repo/, C:\Dokazi_E-2026-10 osim sto tamo pise izvjestaj
   - Nista ne brise bez -Potvrdi

 NIKADA: rijeci iz phrase-a ne lijepi u chat / mail / AI alat / biljesku.

 Pokretanje (PowerShell kao Administrator):
   Set-ExecutionPolicy -Scope Process Bypass -Force
   .\proton_sweep.ps1                          # samo SCAN + izvjestaj (nista ne brise)
   .\proton_sweep.ps1 -Cisti -Potvrdi          # SCAN + unisti pogotke (pita UNISTI)
   .\proton_sweep.ps1 -Cisti -Predmemorija -Potvrdi -Povijest
   .\proton_sweep.ps1 -Duboko                  # skeniraj CIJELE pogone (sporo)
   .\proton_sweep.ps1 -SlobodanProstor -Potvrdi# cipher /w (noce, na punjacu)

 Zastita od greske:
   - brisanje krece tek kad upises rijec UNISTI na upit
   - putanje dosjea (dosje, repo_dosje, Forenzika, Evidence, Pravni-akti, ZPPI,
     MANIFEST-SHA256, PAKET_, Proton_Sweep_) se NIKAD ne brisu, samo prijave
   - History baza preglednika dira se samo uz -Povijest (kirurski) ili
     -PovijestKompletno (brise cijelu bazu)
================================================================================
#>

[CmdletBinding()]
param(
    [switch]$Cisti,
    [switch]$Predmemorija,
    [switch]$Povijest,           # kirurski brise redove iz History baze (winsqlite3)
    [switch]$PovijestKompletno,  # brise CIJELU History bazu (nuklearna opcija)
    [switch]$SlobodanProstor,    # cipher /w:X:
    [switch]$Indeks,             # rebuild Windows Search (admin)
    [switch]$Duboko,             # cijeli pogoni, ne samo korisnicki profili
    [switch]$BezMaliPdf,         # iskljuci popis malih PDF-ova
    [switch]$Potvrdi,            # BEZ ovoga nijedno brisanje ne krece
    [string]$Izlaz = 'C:\Dokazi_E-2026-10',
    [string[]]$Pogoni,
    [int]$Prolazi = 3,
    [int]$MaliPdfKB = 400
)

$ErrorActionPreference = 'SilentlyContinue'
$ProgressPreference    = 'SilentlyContinue'

# ------------------------------------------------------------------------- setup
$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()
           ).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

$stamp  = Get-Date -Format 'yyyyMMdd_HHmmss'
$outDir = Join-Path $Izlaz ("Proton_Sweep_" + $stamp)
New-Item -ItemType Directory -Path $outDir -Force | Out-Null
$logPath    = Join-Path $outDir 'SWEEP_LOG.txt'
$csvPath    = Join-Path $outDir 'FUNDLISTE.csv'
$reportPath = Join-Path $outDir 'IZVJESTAJ.txt'
$malipdf    = Join-Path $outDir 'MALI_PDF_POPIS.txt'

function Log([string]$m) {
    $line = "[{0}] {1}" -f (Get-Date -Format 'HH:mm:ss'), $m
    Add-Content -LiteralPath $logPath -Value $line
    Write-Host $line
}
function Section([string]$t) {
    Write-Host ""
    Write-Host ("=== " + $t + " " + ('=' * [Math]::Max(1, 64 - $t.Length)))
    Log ("--- " + $t + " ---")
}

$uzorciImena = @(
    'proton[\s_\-\.]*recovery', 'recovery[\s_\-\.]*phrase', 'recoveryphrase',
    'recovery[\s_\-\.]*kit', 'wiederherstellungs[\s_\-\.]*phrase',
    'wiederherstellung[\s_\-\.]*proton', 'seed[\s_\-\.]*phrase', 'seedphrase',
    'mnemonic', 'passphrase', '12[\s_\-]*word', '12[\s_\-]*rijeci',
    'account[\s_\-\.]*recovery', 'skrivene[\s_\-]*rijeci', 'tajna[\s_\-]*fraza',
    'oporavak.{0,12}(fraza|rijeci|kljuc)', '(fraza|rijeci|kljuc).{0,12}oporavak',
    'proton.{0,15}(backup|keys|kljuc|phrase|fraza|passwort|password|lozinka|kit|seed)',
    '(backup|keys|kljuc|phrase|fraza|passwort|password|lozinka|kit|seed).{0,15}proton'
)
$rxIme = ($uzorciImena -join '|')

$uzorciSadrzaja = @(
    'recovery phrase', 'recovery-phrase', 'Wiederherstellungsphrase',
    'Proton Recovery', 'account recovery phrase', 'recovery kit',
    '12 rijeci', 'dvanaest rijeci'
)
$rxSadrzaj = ($uzorciSadrzaja -join '|')

$tekstualne = @('.txt','.md','.log','.csv','.json','.html','.htm','.xml','.rtf','.ini','.conf','.ps1','.eml','.url')

$pogodci = New-Object System.Collections.ArrayList
function Novi-Pogodak($f, [string]$vrsta, [string]$detalj) {
    $h = ''
    if ($f.Length -lt 20MB) { $h = (Get-FileHash -LiteralPath $f.FullName -Algorithm SHA256).Hash }
    [void]$pogodci.Add([PSCustomObject]@{
        Vrsta=$vrsta; Putanja=$f.FullName; Ime=$f.Name; VelicinaB=$f.Length
        ZadnjaPromjena=$f.LastWriteTime.ToString('yyyy-MM-dd HH:mm:ss')
        SHA256=$h; Detalj=$detalj; Obrisan=''
    })
    Log ("POGODAK [" + $vrsta + "] " + $f.FullName + "  (" + $f.Length + " B, " + $f.LastWriteTime + ") " + $detalj)
}

# funkcija za nepovratno unistavanje (samostalna: ne ovisi o vanjskim varijablama)
function Unisti([string]$p, [int]$prolazi) {
    if (-not (Test-Path -LiteralPath $p)) { return 'nije-postojalo' }
    try {
        $rnd = New-Object System.Security.Cryptography.RNGCryptoServiceProvider
        $buf = New-Object byte[] (1MB)
        $len = (Get-Item -LiteralPath $p -Force).Length
        $fs  = [IO.File]::Open($p, 'Open', 'ReadWrite', 'None')
        for ($pass = 1; $pass -le $prolazi; $pass++) {
            $fs.Position = 0
            [long]$napisano = 0
            while ($napisano -lt $len) {
                $n = [int][Math]::Min($buf.Length, ($len - $napisano))
                if ($pass -eq $prolazi) { [Array]::Clear($buf, 0, $n) } else { $rnd.GetBytes($buf) }
                $fs.Write($buf, 0, $n)
                $napisano += $n
            }
            $fs.Flush($true)
        }
        $fs.SetLength(0); $fs.Close(); $fs.Dispose()
        try { Remove-Item -LiteralPath $p -Stream * -Force } catch {}
        Remove-Item -LiteralPath $p -Force
        if (Test-Path -LiteralPath $p) { return 'GRESKA-jos-postoji' }
        return ('unisten-' + $prolazi + '-prolaza')
    } catch {
        return ('GRESKA: ' + $_.Exception.Message)
    }
}

# stit: ovo se NIKADA ne brise automatski (samo prijavi) - zastita dosjea
$zasticeno = @('\dosje','\repo_dosje','\Forenzika\','\Evidence\','\Pravni-akti\',
               '\Mediji\','\Uzorkovanje\','\Zastita\','\Akcija\','\ZPPI',
               'MANIFEST-SHA256','\PAKET_','\Proton_Sweep_','\Dokazi\')
function Je-Zasticeno([string]$p) {
    foreach ($z in $zasticeno) { if ($p -like ('*' + $z + '*')) { return $true } }
    return $false
}

# kirursko brisanje reda iz History baze preglednika (winsqlite3.exe, Windows 10+)
function Ocisti-Bazu([string]$db, [string]$ctx) {
    $leaf = Split-Path $db -Leaf
    $wsql = Join-Path $env:SystemRoot 'System32\winsqlite3.exe'
    if ($browsers) { return 'PRESKOCENO: preglednik je otvoren, baza je zakljucana' }
    if ($PovijestKompletno) { return ('kompletno-' + (Unisti $db $Prolazi)) }
    if (-not (Test-Path -LiteralPath $wsql)) {
        return 'GRESKA: nema winsqlite3.exe - koristi -PovijestKompletno ili obrisi rucno'
    }
    if ($leaf -ne 'History') {
        return 'PRESKOCENO: za ovu bazu treba -PovijestKompletno (druga shema)'
    }
    $like = @('%recovery%','%phrase%','%mnemonic%','%seed%phrase%','%proton%kit%')
    $wD = (($like | ForEach-Object { "target_path LIKE '$_'" }) -join ' OR ')
    $wU = (($like | ForEach-Object { "url LIKE '$_' OR title LIKE '$_'" }) -join ' OR ')
    try {
        $sel = "SELECT 'DL:'||id||':'||target_path FROM downloads WHERE $wD; SELECT 'URL:'||id||':'||url FROM urls WHERE $wU;"
        $prije = & $wsql $db $sel 2>&1
        foreach ($r in $prije) { Log ("  baza-stavka prije: " + $r) }
        $del = "DELETE FROM downloads WHERE $wD; DELETE FROM urls WHERE $wU; DELETE FROM keyword_search_terms WHERE term LIKE '%recovery%' OR term LIKE '%phrase%'; VACUUM;"
        $null = & $wsql $db $del 2>&1
        $poslije = & $wsql $db $sel 2>&1
        if ($poslije) { return 'GRESKA: stavke su jos u bazi' }
        return 'redovi-obrisani+VACUUM (stari blokovi ostaju u slobodnom prostoru -> preporucen -SlobodanProstor)'
    } catch {
        return ('GRESKA: ' + $_.Exception.Message)
    }
}



# ============================================================================= 0
Section "0. STANJE SISTEMA"
Log ("Administrator: " + $isAdmin)
Log ("Mod: Cisti=$Cisti Predmemorija=$Predmemorija Povijest=$Povijest SlobodanProstor=$SlobodanProstor Duboko=$Duboko Potvrdi=$Potvrdi Prolazi=$Prolazi")
Log ("Racunalo: $env:COMPUTERNAME | korisnik: $env:USERNAME")

Get-PhysicalDisk | ForEach-Object {
    Log ("Disk: " + $_.FriendlyName + " | tip=" + $_.MediaType + " | " + [math]::Round($_.Size/1GB,0) + " GB")
}
if ($isAdmin) {
    $trim = & fsutil behavior query DisableDeleteNotify 2>$null
    Log ("TRIM provjera: " + (($trim | Where-Object { $_ }) -join ' | '))
} else {
    Log "TRIM provjera preskocena (treba Administrator: fsutil behavior query DisableDeleteNotify)"
}
Log "  DisableDeleteNotify = 0  -> TRIM UKLJUCEN: SSD sam nulira obrisane blokove,"
Log "                            'cipher /w' uglavnom nije potreban (tedi disk i vrijeme)."
Log "  DisableDeleteNotify = 1  -> TRIM ISKLJUCEN: obavezno pusti -SlobodanProstor."

try {
    Get-BitLockerVolume | ForEach-Object { Log ("BitLocker " + $_.MountPoint + ": " + $_.ProtectionStatus + " / " + $_.VolumeStatus) }
} catch { Log "BitLocker: modul nedostupan ili treba admin (nije kriticno)" }

Get-Volume | Where-Object { $_.DriveLetter } | ForEach-Object {
    Log ("Volumen " + $_.DriveLetter + ": '" + $_.FileSystemLabel + "' | " + $_.DriveType +
         " | slobodno " + [math]::Round($_.SizeRemaining/1GB,1) + " / " + [math]::Round($_.Size/1GB,1) + " GB")
}

if (-not $Pogoni) {
    $Pogoni = @( (Get-Volume | Where-Object {
        $_.DriveLetter -and ($_.DriveType -eq 'Fixed' -or $_.DriveType -eq 'Removable')
    }).DriveLetter | ForEach-Object { $_.ToString() } )
}
Log ("Pogoni za rad: " + ($Pogoni -join ', '))

$browsers = @('chrome','msedge','firefox','brave','opera','vivaldi') | ForEach-Object { if (Get-Process -Name $_) { $_ } }
if ($browsers) { Log ("POZOR - otvoreni preglednici: " + ($browsers -join ', ') + " -> cache/History se ne mogu obrisati dok rade") }
else           { Log "Preglednici: nijedan nije otvoren (dobro)" }

# ============================================================================= 1
Section "1. PRETRAGA PO IMENU"
$korijeni = New-Object System.Collections.ArrayList
foreach ($p in $Pogoni) {
    $root = $p + ':\'
    if ($Duboko) { [void]$korijeni.Add($root); continue }
    $prof = Join-Path $root 'Users'
    if (Test-Path -LiteralPath $prof) {
        Get-ChildItem -LiteralPath $prof -Directory -Force | ForEach-Object {
            if (@('Public','Default','Default User','All Users') -notcontains $_.Name) {
                foreach ($d in @('Downloads','Documents','Desktop','Pictures','Videos','Music','Saved Games','AppData\Local\Packages')) {
                    $x = Join-Path $_.FullName $d
                    if (Test-Path -LiteralPath $x) { [void]$korijeni.Add($x) }
                }
                Get-ChildItem -LiteralPath $_.FullName -Directory -Force |
                    Where-Object { $_.Name -like '*OneDrive*' -or $_.Name -like '*Dokumente*' -or $_.Name -like '*Documenti*' } |
                    ForEach-Object { [void]$korijeni.Add($_.FullName) }
                Get-ChildItem -LiteralPath $_.FullName -File -Force |
                    Where-Object { $_.Name -match $rxIme } |
                    ForEach-Object { Novi-Pogodak $_ 'ime' '(korijen profila)' }
            }
        }
    }
}
$korijeni = @($korijeni | Select-Object -Unique)

$i = 0
foreach ($k in $korijeni) {
    $i++
    Write-Host ("  [{0}/{1}] {2}" -f $i, $korijeni.Count, $k)
    Get-ChildItem -LiteralPath $k -Recurse -File -Force |
        Where-Object { $_.Name -match $rxIme -and $_.FullName -notlike ($outDir + '*') } |
        ForEach-Object { Novi-Pogodak $_ 'ime' '' }
}

# ============================================================================= 2
Section "2. PRETRAGA PO SADRZAJU (tekstualne < 5 MB, preskace cloud-placeholdere)"
$skendir = New-Object System.Collections.ArrayList
foreach ($p in $Pogoni) {
    $prof = Join-Path ($p + ':\') 'Users'
    if (Test-Path -LiteralPath $prof) { [void]$skendir.Add($prof) }
}
foreach ($k in @($skendir | Select-Object -Unique)) {
    Write-Host ("  sadrzaj: " + $k)
    Get-ChildItem -LiteralPath $k -Recurse -File -Force |
        Where-Object {
            $_.Length -gt 0 -and $_.Length -lt 5MB -and
            ($tekstualne -contains $_.Extension.ToLower()) -and
            $_.FullName -notlike ($outDir + '*') -and
            ($_.Attributes -band [IO.FileAttributes]::Offline) -eq 0 -and
            ($_.Attributes -band [IO.FileAttributes]::ReparsePoint) -eq 0
        } |
        ForEach-Object {
            $hit = Select-String -LiteralPath $_.FullName -Pattern $rxSadrzaj -List
            if ($hit) { Novi-Pogodak $_ 'sadrzaj' ('linija ' + $hit.LineNumber) }
        }
}

# ============================================================================= 3
Section "3. SIROVA PRETRAGA BAZA PREGLEDNIKA (povijest preuzimanja)"
$profili = @(
    "$env:LOCALAPPDATA\Google\Chrome\User Data",
    "$env:LOCALAPPDATA\Microsoft\Edge\User Data",
    "$env:LOCALAPPDATA\BraveSoftware\Brave-Browser\User Data",
    "$env:LOCALAPPDATA\Vivaldi\User Data",
    "$env:APPDATA\Opera Software\Opera Stable",
    "$env:APPDATA\Mozilla\Firefox\Profiles"
)
$bazaImena = @('History','places.sqlite','History-journal','Favicons','Top Sites')

function Nadi-U-Binarnom([string]$path, [string]$rx, [string]$vrsta) {
    if (-not (Test-Path -LiteralPath $path)) { return }
    $tmp = Join-Path $env:TEMP ('sw_' + [IO.Path]::GetRandomFileName() + '.bin')
    Copy-Item -LiteralPath $path -Destination $tmp -Force
    if (-not (Test-Path -LiteralPath $tmp)) { Log ("  zakljucano, ne mogu kopirati: " + $path); return }
    try {
        $bytes = [IO.File]::ReadAllBytes($tmp)
        $txt   = [Text.Encoding]::GetEncoding('ISO-8859-1').GetString($bytes)
        foreach ($m in [regex]::Matches($txt, $rx, 'IgnoreCase')) {
            $s   = [Math]::Max(0, $m.Index - 140)
            $len = [Math]::Min(360, $txt.Length - $s)
            $ctx = ($txt.Substring($s, $len) -replace '[^\x20-\x7E]', '.')
            Log ("RAW POGODAK [" + $vrsta + "] " + $path)
            Log ("   kontekst: " + $ctx)
            $fi = Get-Item -LiteralPath $path -Force
            [void]$pogodci.Add([PSCustomObject]@{
                Vrsta=('raw-'+$vrsta); Putanja=$path; Ime=(Split-Path $path -Leaf)
                VelicinaB=$fi.Length; ZadnjaPromjena=$fi.LastWriteTime.ToString('yyyy-MM-dd HH:mm:ss')
                SHA256=''; Detalj=$ctx; Obrisan=''
            })
        }
    } finally { Remove-Item -LiteralPath $tmp -Force }
}

foreach ($b in $profili) {
    if (Test-Path -LiteralPath $b) {
        Write-Host ("  baza: " + $b)
        Get-ChildItem -LiteralPath $b -Recurse -File -Force |
            Where-Object { $bazaImena -contains $_.Name } |
            ForEach-Object { Nadi-U-Binarnom $_.FullName $rxIme 'browser' }
    }
}

# ============================================================================= 3b
if (-not $BezMaliPdf) {
    Section "3b. MALI PDF-OVI (rucna provjera - datoteka je mozda preimenovana)"
    $linije = New-Object System.Collections.ArrayList
    foreach ($k in $korijeni) {
        Get-ChildItem -LiteralPath $k -Recurse -File -Force |
            Where-Object { $_.Extension -ieq '.pdf' -and $_.Length -lt ($MaliPdfKB * 1KB) } |
            ForEach-Object {
                [void]$linije.Add(("{0,8:N0} B | {1} | {2}" -f $_.Length, $_.LastWriteTime.ToString('yyyy-MM-dd HH:mm'), $_.FullName))
            }
    }
    $linije = @($linije | Sort-Object -Unique)
    $linije | Set-Content -LiteralPath $malipdf -Encoding UTF8
    Log ("Popis malih PDF-ova (< " + $MaliPdfKB + " KB): " + $linije.Count + " stavki -> " + $malipdf)
    Log "  Ove datoteke se NE brisu automatski. Pogledaj popis i javi ako nesto lici na phrase PDF."
}

# ============================================================================= 4
Section "4. REZULTAT PRETRAGE"
$seen = @{}
$dedup = New-Object System.Collections.ArrayList
foreach ($g in $pogodci) {
    $key = $g.Vrsta + '|' + $g.Putanja
    if (-not $seen.ContainsKey($key)) { $seen[$key] = $true; [void]$dedup.Add($g) }
}
$pogodci = $dedup
$broj = $pogodci.Count
if ($broj -eq 0) { Log "CISTO: nijedna datoteka/baza s imenom ili sadrzajem recovery phrase nije nadena." }
else             { Log ("NADENO: " + $broj + " stavki -> FUNDLISTE.csv") }

# ============================================================================= 5
if ($Cisti) {
    Section "5. NEPOVRATNO UNISTAVANJE POGODAKA"
    if (-not $Potvrdi) { Log "ZAUSTAVLJENO: za brisanje dodaj -Potvrdi" }
    elseif ($broj -eq 0) { Log "Nema sto brisati." }
    else {
        Write-Host ""
        Write-Host "Ove stavke ce biti PREPISANE (3 prolaza) i OBRISANE:" -ForegroundColor Yellow
        $n = 0
        foreach ($g in $pogodci) { $n++; Write-Host ("  {0,3}. [{1}] {2}" -f $n, $g.Vrsta, $g.Putanja) }
        Write-Host ""
        Write-Host "Zasticene putanje (dosje, Forenzika, Evidence, MANIFEST, PAKET) se NE brisu,"
        Write-Host "samo se prijave. Baze preglednika se brisu samo uz -Povijest."
        Write-Host ""
        $odgovor = ''
        try { $odgovor = Read-Host "Upisi UNISTI za nastavak (bilo sto drugo = odustani)" } catch { $odgovor = '' }
        if ($odgovor -cne 'UNISTI') {
            Log "ODUSTAO: brisanje prekinuto (nije upisano UNISTI). Nista nije obrisano."
        } else {
            foreach ($g in $pogodci) {
                if (Je-Zasticeno $g.Putanja) {
                    $g.Obrisan = 'ZASTICENO-prijavljeno-ne-brise-se'
                    Log ("ZASTICENO (ne brisem): " + $g.Putanja)
                    continue
                }
                if ($g.Vrsta -like 'raw-*') {
                    if (-not $Povijest) { $g.Obrisan = 'preskoceno-baza (treba -Povijest)'; Log ("PRESKACEM bazu: " + $g.Putanja); continue }
                    $g.Obrisan = Ocisti-Bazu $g.Putanja $g.Detalj
                    Log ($g.Obrisan + " : " + $g.Putanja)
                    continue
                }
                $g.Obrisan = Unisti $g.Putanja $Prolazi
                Log ($g.Obrisan + " : " + $g.Putanja)
            }
        }
    }
}

# ============================================================================= 6
if ($Predmemorija) {
    Section "6. PRAZNJENJE RECYCLE BINA I PREDMEMORIJE"
    if (-not $Potvrdi) { Log "ZAUSTAVLJENO: treba -Potvrdi" }
    else {
        foreach ($p in $Pogoni) {
            $rb = $p + ':\$Recycle.Bin'
            if (Test-Path -LiteralPath $rb) {
                Get-ChildItem -LiteralPath $rb -Recurse -Force | Remove-Item -Recurse -Force
                Log ("Recycle.Bin ociscen: " + $rb)
            }
            Clear-RecycleBin -DriveLetter $p -Force -Confirm:$false
        }
        $ciljevi = @(
            "$env:TEMP\*", 'C:\Windows\Temp\*',
            "$env:APPDATA\Microsoft\Windows\Recent\*",
            "$env:APPDATA\Microsoft\Windows\Recent\AutomaticDestinations\*",
            "$env:APPDATA\Microsoft\Windows\Recent\CustomDestinations\*",
            "$env:LOCALAPPDATA\Microsoft\Windows\INetCache\*",
            "$env:LOCALAPPDATA\Microsoft\Windows\WebCache\WebCacheV*.dat",
            "$env:LOCALAPPDATA\Microsoft\Windows\Explorer\thumbcache_*.db",
            "$env:LOCALAPPDATA\Microsoft\Windows\Explorer\iconcache_*.db",
            "$env:LOCALAPPDATA\Google\Chrome\User Data\*\Cache\*",
            "$env:LOCALAPPDATA\Google\Chrome\User Data\*\Code Cache\*",
            "$env:LOCALAPPDATA\Microsoft\Edge\User Data\*\Cache\*",
            "$env:LOCALAPPDATA\Microsoft\Edge\User Data\*\Code Cache\*",
            "$env:LOCALAPPDATA\Mozilla\Firefox\Profiles\*\cache2\*",
            "$env:LOCALAPPDATA\Packages\*\TempState\*"
        )
        foreach ($c in $ciljevi) {
            $items = @(Get-Item -Path $c -Force)
            if ($items.Count -gt 0) {
                $items | Remove-Item -Recurse -Force
                Log ("ocisceno (" + $items.Count + " stavki): " + $c)
            } else { Log ("prazno/nedostupno: " + $c) }
        }
        if ($isAdmin) { Get-ChildItem 'C:\Windows\Prefetch\*' -Force | Remove-Item -Force; Log "Prefetch ociscen" }
        else          { Log "Prefetch preskocen (treba Administrator)" }
        if ($browsers) { Log "Cache preglednika preskocen jer su otvoreni - zatvori ih pa pusti ponovno, ili Ctrl+Shift+Del u pregledniku." }
    }
}

# ============================================================================= 7
if ($Indeks) {
    Section "7. WINDOWS SEARCH INDEKS"
    if ($isAdmin) {
        Stop-Service WSearch -Force
        Remove-Item 'C:\ProgramData\Microsoft\Search\Data\Applications\Windows\Windows.edb' -Force
        Start-Service WSearch
        Log "Windows.edb obrisan, servis ponovno pokrenut (rebuild ide u pozadini)"
    } else { Log "Preskoceno (treba Administrator)" }
}

# ============================================================================= 8
if ($SlobodanProstor) {
    Section "8. CIPHER /w  -  BRISANJE SLOBODNOG PROSTORA"
    if (-not $Potvrdi) { Log "ZAUSTAVLJENO: treba -Potvrdi. Rucno: cipher /w:C:\Users\zeljk" }
    else {
        Log "Prije: powercfg /change standby-timeout-ac 0  (da ne zaspi), laptop na punjac."
        Log "Traje satima po volumenu. Prekid je bezopasan - mozes Ctrl+C i nastaviti drugi put."
        foreach ($p in $Pogoni) {
            $v = $p + ':\'
            $t0 = Get-Date
            Log ("POKRECEN: cipher /w:" + $v)
            & cipher.exe ("/w:" + $v) 2>&1 | ForEach-Object { Log ("   " + $_) }
            Log ("GOTOVO " + $v + " za " + [math]::Round(((Get-Date) - $t0).TotalMinutes,1) + " min")
        }
    }
}

# ============================================================================= 9
Section "9. IZVJESTAJ"
$pogodci | Export-Csv -LiteralPath $csvPath -NoTypeInformation -Encoding UTF8 -Delimiter ';'

$rep = New-Object System.Collections.ArrayList
[void]$rep.Add("PROTON SWEEP - IZVJESTAJ (sigurnosna higijena, nije dokaz u dosjeu)")
[void]$rep.Add("Vrijeme : " + (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'))
[void]$rep.Add("Stroj   : $env:COMPUTERNAME | korisnik $env:USERNAME | admin $isAdmin")
[void]$rep.Add("Mod     : Cisti=$Cisti Predmemorija=$Predmemorija Povijest=$Povijest SlobodanProstor=$SlobodanProstor Duboko=$Duboko Potvrdi=$Potvrdi Prolazi=$Prolazi")
[void]$rep.Add("Pogoni  : " + ($Pogoni -join ', '))
[void]$rep.Add("TRIM    : " + (($trim | Where-Object { $_ }) -join ' | '))
[void]$rep.Add("")
[void]$rep.Add("UKUPNO POGODAKA: " + $broj)
foreach ($g in $pogodci) {
    [void]$rep.Add(("  [{0}] {1} | {2} B | {3} | hash {4} | status: {5}" -f $g.Vrsta,$g.Putanja,$g.VelicinaB,$g.ZadnjaPromjena,$g.SHA256,$g.Obrisan))
}
[void]$rep.Add("")
[void]$rep.Add("Sadrzaj nadenih datoteka NIJE citan ni spreman u ovaj izvjestaj.")
[void]$rep.Add("Stara recovery phrase je nevaljana od rotacije 13.10.2026. - ovo je higijena,")
[void]$rep.Add("ne krizna situacija. Ako je bilo koji pogodak ostao statusom GRESKA, javi.")
$rep | Set-Content -LiteralPath $reportPath -Encoding UTF8

Write-Host ""
Write-Host ("IZVJESTAJ   : " + $reportPath)
Write-Host ("FUNDLISTE   : " + $csvPath)
Write-Host ("MALI PDF-ovi: " + $malipdf)
Write-Host ("LOG         : " + $logPath)
foreach ($f in @($reportPath, $csvPath, $malipdf, $logPath)) {
    if (Test-Path -LiteralPath $f) {
        $h = (Get-FileHash -LiteralPath $f -Algorithm SHA256).Hash
        Write-Host ("SHA-256 [" + (Split-Path $f -Leaf) + "] = " + $h)
        Log ("HASH " + (Split-Path $f -Leaf) + " = " + $h)
    }
}
Write-Host ""
Write-Host "GOTOVO."
