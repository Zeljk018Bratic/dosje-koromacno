# === SHA-256 Manifest Generator (ispravljeno) ===
$Root = (Get-Location).Path
$OutFile = Join-Path $Root "MANIFEST_FULL.sha256"
$files = Get-ChildItem -Path $Root -Recurse -File | Where-Object {
    $_.FullName -notmatch '\\.git\\' -and
    $_.Name -ne "MANIFEST_FULL.sha256"
}

$lines = [System.Collections.Generic.List[string]]::new()
$lines.Add("# SHA-256 Manifest - Dosje Koromačno")
$lines.Add("# Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')")
$lines.Add("# Root: $Root")
$lines.Add("#")

$count = 0
$bytes = [int64]0
$started = Get-Date

foreach ($f in $files) {
    $rel = $f.FullName.Substring($Root.Length).TrimStart('\', '/').Replace('\', '/')
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