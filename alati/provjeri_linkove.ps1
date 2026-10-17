# provjeri_linkove.ps1
cd C:\Users\zeljk\dosje-koromacno
$greske = 0
Get-ChildItem *.html | ForEach-Object {
    $f = $_
    $content = Get-Content $f.FullName -Raw
    $links = [regex]::Matches($content, 'href="([^"#]+)"') | ForEach-Object { $_.Groups[1].Value }
    
    foreach ($link in $links) {
        if ($link -match '^https?://') { continue }
        if ($link -match '^#') { continue }
        
        $target = Join-Path $f.DirectoryName $link
        if (-not (Test-Path $target)) {
            Write-Host "❌ POKVARENO: $($f.Name) -> $link" -ForegroundColor Red
            $greske++
        }
    }
}
if ($greske -eq 0) {
    Write-Host "✅ Svi lokalni linkovi u HTML datotekama su ispravni!" -ForegroundColor Green
} else {
    Write-Host "⚠️ Pronađeno je $greske pokvarenih linkova." -ForegroundColor Yellow
}
