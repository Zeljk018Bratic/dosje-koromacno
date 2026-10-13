# =====================================================================
#  SVE_U_REPO_13-10.ps1  —  13.10.2026.  —  SVE U JEDNOM, DO GITHUB-A
#
#  Sto radi (ovim redom):
#   0) git status + git pull --ff-only origin main
#   1) backup Evidence_Matrix.csv IZVAN repo-a
#   2) raspakira PAKET v3 u repo (ako nadje zip; inace preskoci)
#   3) zastiti E-041 (zip-verzija matrice ga NEMA):
#      - vrati lokalnu matricu iz backupa, a ako ni ona nema E-041
#        -> postavi CLEAN_PREVIEW (44 retka, E-001..E-044)
#   4) interne datoteke (oznacene "NE ide u javni repo") premjesti IZVAN repo-a
#   5) kopira danasnji paket u repo (forenzika, E-042/43/44, Vijece, run-sheet)
#   6) pokrene NETEH_SAZETAK_PROVJERA.ps1 (hash papirnate kopije + dedup matrice)
#   7) validacija: matrica mora imati 44+ jedinstvenih redaka, E-041..E-044,
#      1 zaglavlje, 0 duplikata  ->  inace STOP, bez commita
#   8) git add / commit / push + ispis HEAD i ROOT HASH docs/
#
#  Pokretanje (iz mape gdje si raspakirao PAKET_REPO_FINAL_13-10-2026.zip):
#     powershell -ExecutionPolicy Bypass -File .\SVE_U_REPO_13-10.ps1
#
#  Log:  %LOCALAPPDATA%\dosje-lf-logovi\SVE_U_REPO_<vrijeme>.log
#  Sve sto se izdvaja iz repo-a ide u: %LOCALAPPDATA%\dosje-izolacija-INTERNO
#  NISTA se ne brise. Zaustavi li se skripta (STOP), posalji QWENU log.
# =====================================================================

param(
    [string]$Repo    = "C:\Users\zeljk\dosje-lf",
    [string]$PaketV3 = ""
)

$ErrorActionPreference = "Stop"
$pkg    = Split-Path -Parent $MyInvocation.MyCommand.Path
$logDir = Join-Path $env:LOCALAPPDATA "dosje-lf-logovi"
$izol   = Join-Path $env:LOCALAPPDATA "dosje-izolacija-INTERNO"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
New-Item -ItemType Directory -Force -Path $izol   | Out-Null
$stamp = Get-Date -Format "yyyy-MM-dd_HHmm"
$log   = Join-Path $logDir "SVE_U_REPO_$stamp.log"
function W($m) { Write-Host $m; Add-Content -LiteralPath $log -Value $m -Encoding UTF8 }

W "=== SVE_U_REPO 13.10.2026. ==="
W ("paket : " + $pkg)
W ("repo  : " + $Repo)
if (-not (Test-Path -LiteralPath (Join-Path $Repo ".git"))) {
    W "STOP: repo mapa nije git-klon (nema .git). Pokreni iz ispravne mape ili proslijedi -Repo."
    exit 1
}

# ---------------------------------------------------------------- 0) GIT
W ""
W "=== 0) GIT STATUS + PULL ==="
Set-Location -LiteralPath $Repo
$st = & git status --porcelain
if ($st) {
    W "radna kopija NIJE cista - lokalne izmjene ulaze u ovaj commit (prvih 15):"
    $st | Select-Object -First 15 | ForEach-Object { W ("   " + $_) }
} else { W "radna kopija cista" }
$ErrorActionPreference = "Continue"   # git pise progress na stderr - inace PS 5.1 zna lažno baciti gresku
$pullOut = & git pull --ff-only origin main 2>&1
$pullExit = $LASTEXITCODE
$ErrorActionPreference = "Stop"
$pullOut | ForEach-Object { W ("pull: " + $_) }
if ($pullExit -ne 0) { W ("STOP: git pull --ff-only nije prosao. Posalji QWENU log: " + $log); exit 1 }
W ("HEAD prije: " + (& git log -1 --format="%h %s"))

# ------------------------------------------------------- 1) BACKUP MATRICE
W ""
W "=== 1) BACKUP MATRICE (izvan repo-a) ==="
$mat    = Join-Path $Repo "docs\Evidence\Evidence_Matrix.csv"
$bakMat = Join-Path $izol ("Evidence_Matrix.csv.bak_" + $stamp)
if (Test-Path -LiteralPath $mat) {
    Copy-Item -LiteralPath $mat -Destination $bakMat -Force
    W ("backup: " + $bakMat)
} else {
    W "NEMA lokalne matrice - kasnije ce se postaviti CLEAN_PREVIEW iz paketa."
}

# ------------------------------------------------------------- 2) PAKET v3
W ""
W "=== 2) PAKET v3 ==="
if (-not $PaketV3) {
    $kandidati = @(
        (Join-Path $pkg "PAKET_v3_13-10-2026.zip"),
        (Join-Path (Join-Path $env:USERPROFILE "Downloads") "PAKET_v3_13-10-2026.zip"),
        (Join-Path (Join-Path $env:USERPROFILE "Desktop")   "PAKET_v3_13-10-2026.zip")
    )
    foreach ($k in $kandidati) { if (Test-Path -LiteralPath $k) { $PaketV3 = $k; break } }
}
if ($PaketV3 -and (Test-Path -LiteralPath $PaketV3)) {
    Expand-Archive -LiteralPath $PaketV3 -DestinationPath $Repo -Force
    W ("raspakirano: " + $PaketV3)
} else {
    W "PAKET v3 zip nije nadjen - preskacem (u redu je ako je vec ranije raspakiran u repo)."
}

# --------------------------------------------------- 3) MATRICA: ZASTITI E-041
W ""
W "=== 3) MATRICA - provjera E-041 ==="
function Test-ImaE41($f) {
    if (-not (Test-Path -LiteralPath $f)) { return $false }
    return [bool](Select-String -LiteralPath $f -Pattern '^"E-041"' -Quiet)
}
if (Test-ImaE41 $mat) {
    W "matrica u repu sadrzi E-041 - OK"
} elseif (Test-ImaE41 $bakMat) {
    Copy-Item -LiteralPath $bakMat -Destination $mat -Force
    W "zip-verzija matrice nema E-041 -> vracena lokalna matrica iz backupa"
} else {
    $cp = Join-Path $pkg "docs\Evidence\Evidence_Matrix_CLEAN_PREVIEW.csv"
    if (Test-Path -LiteralPath $cp) {
        Copy-Item -LiteralPath $cp -Destination $mat -Force
        W "E-041 nema ni lokalno -> postavljena CLEAN_PREVIEW matrica (44 retka, E-001..E-044)"
    } else {
        W "STOP: nema E-041 ni CLEAN_PREVIEW. Nista dalje. Posalji QWENU log."
        exit 1
    }
}

# ------------------------------------------- 4) INTERNE DATOTEKE IZVAN REPO-A
W ""
W "=== 4) INTERNE DATOTEKE (ne idu u javni repo) ==="
$interno = @(
    "docs\Zastita\PAKET_ZA_MATEU_FINAL.md",
    "docs\Zastita\OPCIJE_ZASTITA_SLAPP_I_PETAK.md",
    "docs\Uzorkovanje\IZJAVA_PREDLOZAK_MATEA.md",
    "docs\Akcija\2026-10-13_PLAN_JAVNOG_SKUPA_I_SUDJELOVANJA.md"
)
foreach ($f in $interno) {
    $p = Join-Path $Repo $f
    if (Test-Path -LiteralPath $p) {
        Move-Item -LiteralPath $p -Destination (Join-Path $izol (Split-Path $f -Leaf)) -Force
        W ("izdvojeno izvan repo-a: " + $f)
    }
}
# zaostali .bak_* unutar docs\Evidence (od ranijih pokretanja PROVJERE)
$evDir = Join-Path $Repo "docs\Evidence"
Get-ChildItem -LiteralPath $evDir -Filter "*.bak_*" -ErrorAction SilentlyContinue | ForEach-Object {
    Move-Item -LiteralPath $_.FullName -Destination (Join-Path $izol $_.Name) -Force
    W ("izdvojen zaostali backup: " + $_.Name)
}

# -------------------------------------------------- 5) DANASNJI PAKET -> REPO
W ""
W "=== 5) DANASNJI PAKET -> REPO ==="
New-Item -ItemType Directory -Force -Path (Join-Path $Repo "docs\Forenzika") | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $Repo "docs\Evidence")  | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $Repo "docs\Akcija")    | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $Repo "alati")          | Out-Null
$kopiraj = @(
    @{ src = "docs\Forenzika\2026-10-13_NETEHNICKI_SAZETAK_KODECO_ANALIZA.md"; dst = "docs\Forenzika" },
    @{ src = "docs\Evidence\E-MATRIX_NOVI_REDOVI_E042-E044.csv";               dst = "docs\Evidence"  },
    @{ src = "SHA256_NOVI_DOKAZI_13-10-2026.txt";                              dst = "docs\Evidence"  },
    @{ src = "docs\Akcija\RASA_VIJECE_14-10-2026.md";                          dst = "docs\Akcija"    },
    @{ src = "docs\PONEDJELJAK_19-10_RUNSHEET.md";                             dst = "docs"          },
    @{ src = "NETEH_SAZETAK_PROVJERA.ps1";                                     dst = "alati"         },
    @{ src = "SVE_U_REPO_13-10.ps1";                                           dst = "alati"         }
)
foreach ($k in $kopiraj) {
    $s = Join-Path $pkg $k.src
    if (Test-Path -LiteralPath $s) {
        Copy-Item -LiteralPath $s -Destination (Join-Path $Repo $k.dst) -Force
        W ("kopirano: " + $k.src + "  ->  " + $k.dst)
    } else {
        W ("PAZI: u paketu nedostaje " + $k.src)
    }
}
# list za Vijece i na Desktop (za sutra, print/citanje)
$sheet = Join-Path $pkg "docs\Akcija\RASA_VIJECE_14-10-2026.md"
if (Test-Path -LiteralPath $sheet) {
    Copy-Item -LiteralPath $sheet -Destination (Join-Path $env:USERPROFILE "Desktop") -Force
    W "RASA_VIJECE_14-10-2026.md kopiran i na Desktop"
}

# ------------------------------------------------- 6) PROVJERA (hash + dedup)
W ""
W "=== 6) PROVJERA (hash papirnate kopije + dedup + E-042/43/44) ==="
$prov = Join-Path $Repo "alati\NETEH_SAZETAK_PROVJERA.ps1"
& $prov
$provLog = Get-ChildItem -LiteralPath $logDir -Filter "NETEH_PROVJERA_*.log" -ErrorAction SilentlyContinue |
           Sort-Object LastWriteTime -Descending | Select-Object -First 1
$rez = "NEMA-REZULTATA"
if ($provLog) {
    $txt = Get-Content -LiteralPath $provLog.FullName -Raw
    if     ($txt -match "REZULTAT: IDENTICNO")  { $rez = "IDENTICNO" }
    elseif ($txt -match "REZULTAT: RAZLICITO")  { $rez = "RAZLICITO" }
    elseif ($txt -match "NISAM NASAO lokalnu")  { $rez = "PDF-NIJE-NADJEN" }
}
W ("rezultat hash-provjere papirnate kopije: " + $rez)

# papirnata kopija (ako postoji u repo mapi) ide IZVAN repo-a - sada kad je hashiran
$arh = Join-Path $Repo "docs\Arhiva"
$kand = Get-ChildItem -LiteralPath $arh -Filter "NETEHNI*.pdf" -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -notlike "MZOZT_*" } | Select-Object -First 1
if ($kand) {
    Move-Item -LiteralPath $kand.FullName -Destination (Join-Path $izol $kand.Name) -Force
    W ("papirnata kopija izdvojena izvan repo-a: " + $kand.Name)
}

if ($rez -eq "RAZLICITO") {
    W "STOP: papirnata kopija NIJE identicna sluzbenoj MZOZT kopiji."
    W "To bi bila NOVA VERZIJA dokumenta - velik nalaz, ali NISTA ne ide na GitHub dok Qwen ne potvrdi."
    W ("Posalji QWENU oba loga: " + $log + "  i  " + $provLog.FullName)
    exit 2
}

# ------------------------- 6b) FINALNA MATRICA = CLEAN_PREVIEW (ako je sigurno)
# Razlog: lokalni redovi E-033/037/040/041 znali su imati CSV-gresku (ravan " unutar polja).
# CLEAN_PREVIEW u ovom paketu je popravljen i CSV-validan. Ako lokalna matrica nema NIJEDAN
# ID koji vec nije u CLEAN_PREVIEW-u -> CLEAN_PREVIEW postaje konacna matrica.
W ""
W "=== 6b) FINALNA MATRICA ==="
function Get-Ids($f) {
    $res = @()
    if (Test-Path -LiteralPath $f) {
        Get-Content -LiteralPath $f -Encoding UTF8 | ForEach-Object {
            if ($_ -match '^"(E-\d+)"') { $res += $Matches[1] }
        }
    }
    return $res
}
$cp = Join-Path $pkg "docs\Evidence\Evidence_Matrix_CLEAN_PREVIEW.csv"
if (Test-Path -LiteralPath $cp) {
    $cpIds  = @(Get-Ids $cp  | Select-Object -Unique)
    $matIds = @(Get-Ids $mat | Select-Object -Unique)
    $visak  = @($matIds | Where-Object { $cpIds -notcontains $_ })
    if ($visak.Count -eq 0) {
        Copy-Item -LiteralPath $cp -Destination $mat -Force
        W ("CLEAN_PREVIEW postavljen kao konacna matrica (" + $cpIds.Count + " ID-ova, CSV-validan)")
    } else {
        W ("PAZI: lokalna matrica ima ID-ove kojih nema u CLEAN_PREVIEW: " + ($visak -join ", "))
        W "Zadrzavam lokalnu matricu - posalji QWENU ovu liniju pa cemo ih spojiti rucno."
    }
} else {
    W "CLEAN_PREVIEW nije u paketu - ostavljam matricu kakvu je PROVJERA složila."
}

# ----------------------------------------------------- 7) VALIDACIJA MATRICE
W ""
W "=== 7) VALIDACIJA MATRICE ==="
$raw  = Get-Content -LiteralPath $mat -Encoding UTF8
$head = @($raw | Where-Object { $_ -match '^"ID","Datum_od"' })
$rows = @($raw | Where-Object { $_ -match '^"E-\d+"' })
$ids  = @($rows | ForEach-Object { if ($_ -match '^"(E-\d+)"') { $Matches[1] } })
$uniq = @($ids | Select-Object -Unique)
$dups = @($ids | Group-Object | Where-Object { $_.Count -gt 1 })
$nema = @(@("E-041","E-042","E-043","E-044") | Where-Object { $ids -notcontains $_ })
W ("redaka: " + $rows.Count + "  jedinstvenih: " + $uniq.Count + "  duplikata: " + $dups.Count + "  zaglavlja: " + $head.Count)
if ($dups.Count -gt 0) { W ("duplikati: " + (($dups | ForEach-Object Name) -join ", ")) }
if ($nema.Count  -gt 0) { W ("nedostaju: " + ($nema -join ", ")) }
$ok = ($rows.Count -eq $uniq.Count) -and ($uniq.Count -ge 44) -and ($head.Count -eq 1) -and ($nema.Count -eq 0)
if (-not $ok) {
    W "STOP: matrica nije cista -> NE commitam. Posalji QWENU log."
    exit 3
}
W ("matrica cista. SHA256: " + (Get-FileHash -LiteralPath $mat -Algorithm SHA256).Hash)

# -------------------------------------------------------- 8) COMMIT + PUSH
W ""
W "=== 8) COMMIT + PUSH ==="
& git add -A
if ($LASTEXITCODE -ne 0) { W "STOP: git add nije prosao. Posalji log QWENU."; exit 4 }
$staged = @(& git diff --cached --name-only)
W ("staged datoteka: " + $staged.Count)
$zabranjeno = @($staged | Where-Object { $_ -match "PAKET_ZA_MATEU|OPCIJE_ZASTITA|IZJAVA_PREDLOZAK_MATEA|PLAN_JAVNOG_SKUPA|Evidence_Matrix\.csv\.bak|NETEHNI.*Ra.*\.pdf" })
if ($zabranjeno.Count -gt 0) {
    & git reset | Out-Null
    W ("STOP: interno bi bilo commitano (" + ($zabranjeno -join ", ") + ") - staging vracen. Posalji log QWENU.")
    exit 4
}
if ($staged.Count -eq 0) {
    W "nema novih izmjena - sve je vec pushano."
} else {
    $msg = "13.10.2026.: forenzika netehnickog sazetka MZOZT (SHA 431b0d03) + E-042/43/44; matrica 44 retka; pitanja za Vijece Rasa 14.10.; run-sheet 19.10.; PAKET v3"
    & git commit -m $msg | ForEach-Object { W ("commit: " + $_) }
    if ($LASTEXITCODE -ne 0) { W "STOP: commit nije prosao. Posalji log QWENU."; exit 5 }
    $ErrorActionPreference = "Continue"
    $pushOut = & git push origin main 2>&1
    $pushExit = $LASTEXITCODE
    $ErrorActionPreference = "Stop"
    $pushOut | ForEach-Object { W ("push: " + $_) }
    if ($pushExit -ne 0) { W "STOP: push nije prosao (network/credentials?). Commit je ostao LOKALNO - javi QWENU."; exit 6 }
}
W ("HEAD: "          + (& git log -1 --format="%H %ci"))
W ("ROOT HASH docs/: " + (& git rev-parse "HEAD:docs"))

# ------------------------------------------------------------- SAZETAK
W ""
W "=== GOTOVO ==="
W "Posalji QWENU (moze cijeli log, moze samo ovo):"
W ("  1) hash-provjera papirnate kopije : " + $rez)
W ("  2) SHA256 matrice + broj redaka   : vidi korak 7")
W ("  3) ROOT HASH docs/                : vidi iznad")
W ("  4) HEAD                           : vidi iznad")
W ("Izdvojeno (INTERNO, nije obrisano): " + $izol)
W ("Logovi: " + $logDir)
