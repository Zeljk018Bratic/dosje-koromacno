# SHA-256 working-tree manifest for Dosje Koromačno
# Does not modify files. Does not commit or push.
# Excludes .git object store (working tree only).

param(
    [string]$Root = (Split-Path -Parent $PSScriptRoot),
    [string]$OutFile,
    [switch]$KeyEvidenceOnly
)

$ErrorActionPreference = "Stop"

if (-not $OutFile) {
    $OutFile = Join-Path $Root "docs\00_MANIFEST_SHA256_PRIJE.txt"
}

$outDir = Split-Path -Parent $OutFile
if (-not (Test-Path -LiteralPath $outDir)) {
    New-Item -ItemType Directory -Path $outDir -Force | Out-Null
}

$started = Get-Date
$files = Get-ChildItem -LiteralPath $Root -Recurse -File -Force -ErrorAction SilentlyContinue |
    Where-Object {
        $_.FullName -notmatch '[\\/]\.git[\\/]' -and
        $_.FullName -ne $OutFile
    }

if ($KeyEvidenceOnly) {
    $files = $files | Where-Object { $_.Extension -match '^\.(pdf|csv|json)$' }
}

$files = $files | Sort-Object FullName

$lines = New-Object System.Collections.Generic.List[string]
$lines.Add("# SHA-256 MANIFEST")
$lines.Add("# root=$Root")
$lines.Add("# generated_utc=$((Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ'))")
$lines.Add("# algorithm=SHA256")
$lines.Add("# excludes=.git")
$lines.Add("# key_evidence_only=$($KeyEvidenceOnly.IsPresent)")
$lines.Add("# format=SHA256  RELATIVE_PATH")
$lines.Add("#")

$count = 0
$bytes = [int64]0

foreach ($f in $files) {
    $rel = $f.FullName.Substring($Root.Length).TrimStart('\', '/')
    $hash = (Get-FileHash -LiteralPath $f.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
    $lines.Add("$hash  $rel")
    $count++
    $bytes += $f.Length
}

$elapsed = ((Get-Date) - $started).TotalSeconds
$lines.Add("#")
$lines.Add("# file_count=$count")
$lines.Add("# bytes=$bytes")
$lines.Add("# elapsed_seconds={0:N2}" -f $elapsed)

$utf8 = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::WriteAllLines($OutFile, $lines, $utf8)

Write-Host "Wrote $count hashes to $OutFile"
Write-Host "Bytes: $bytes"
Write-Host "Elapsed: $([math]::Round($elapsed, 2)) s"
