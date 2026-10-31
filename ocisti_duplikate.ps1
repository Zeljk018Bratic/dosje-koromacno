# ocisti_duplikate.ps1
$ErrorActionPreference = "Stop"

$root = "C:\Users\zeljk\dosije-koromacno"
$csv  = Join-Path $root "docs\evidence\Evidence_Matrix.csv"
$log  = Join-Path $root "cleanup_log_$(Get-Date -Format yyyyMMdd_HHmmss).txt"

function Log($msg) {
    Write-Host $msg
    $msg | Out-File -Append -Encoding UTF8 $log
}

Log "=== POCETAK $(Get-Date) ==="

# 1. Backup matrice
if (Test-Path $csv) {
    Copy-Item $csv "$csv.bak_$(Get-Date -Format yyyyMMdd_HHmmss)"
    Log "Backup matrice spremljen."
}

# 2. Nadji sve PDF-ove i hashiraj
$pdfs = Get-ChildItem -Path $root -Recurse -File -Filter *.pdf -ErrorAction SilentlyContinue |
        Where-Object { $_.FullName -notmatch '\\\.git\\' -and $_.FullName -notmatch '_TRASH_' }

Log "Nadeno PDF-ova: $($pdfs.Count)"

$hashes = @{}
foreach ($f in $pdfs) {
    $h = (Get-FileHash $f.FullName -Algorithm SHA256).Hash
    if (-not $hashes.ContainsKey($h)) { $hashes[$h] = @() }
    $hashes[$h] += $f
}

# 3. Prikazi duplikate (isti hash, razlicite putanje)
$duplikati = @()
foreach ($k in $hashes.Keys) {
    if ($hashes[$k].Count -gt 1) {
        Log "--- DUPLIKAT (hash $k):"
        foreach ($f in $hashes[$k]) { Log "    $($f.FullName)" }
        $duplikati += $hashes[$k]
    }
}

if ($duplikati.Count -eq 0) {
    Log "Nema duplikata po hash-u."
} else {
    Log "Ukupno duplikata: $($duplikati.Count)"
}

# 4. Azuriraj Evidence_Matrix.csv Veza_na_dosje na temelju hash-a
if (Test-Path $csv) {
    $data = Import-Csv $csv -Encoding UTF8
    $updated = 0
    foreach ($row in $data) {
        $hv = $row.Dokazna_vrijednost
        if ($hv -and $hashes.ContainsKey($hv)) {
            $f = $hashes[$hv][0]
            $rel = $f.FullName.Substring($root.Length).TrimStart('\')
            if ($row.Veza_na_dosje -ne $rel) {
                $row.Veza_na_dosje = $rel
                $updated++
            }
        }
    }
    $data | Export-Csv $csv -NoTypeInformation -Encoding UTF8
    Log "Azurirano $updated redova u Evidence_Matrix.csv"
}

Log "=== KRAJ $(Get-Date) ==="
Log "Log: $log"