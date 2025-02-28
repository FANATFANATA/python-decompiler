Write-Host "=== Lua Script Decompiler ==="

$luac_file = Read-Host "Enter the path to the .luac file"
if (-Not (Test-Path $luac_file)) {
    Write-Host "File not found!"
    exit
}

$tool = Read-Host "Choose a tool (unluac/luadec)"
if ($tool -ne "unluac" -and $tool -ne "luadec") {
    Write-Host "Invalid tool choice!"
    exit
}

$output_file = Read-Host "Enter the path to save the result"

if ($tool -eq "unluac") {
    java -jar tools/unluac.jar $luac_file > $output_file
} elseif ($tool -eq "luadec") {
    ./tools/luadec $luac_file > $output_file
}

Write-Host "Decompilation complete. Result saved to $output_file"
