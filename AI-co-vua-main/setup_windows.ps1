$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

$python312 = "$env:LOCALAPPDATA\Python\bin\python3.12-64.exe"
if (-not (Test-Path $python312)) {
    $python312 = (Get-Command py -ErrorAction SilentlyContinue)
    if ($python312) { & py -3.12 --version }
    else { throw 'Không tìm thấy Python 3.12. Cài Python 3.12 hoặc cập nhật đường dẫn python312 trong setup_windows.ps1.' }
}

if (-not (Test-Path '.venv312\Scripts\python.exe')) {
    & $python312 -m venv .venv312
}
$venvPython = Join-Path $root '.venv312\Scripts\python.exe'
$env:PYTHONUTF8 = '1'
& $venvPython -m pip install --upgrade pip
& $venvPython -m pip install -r requirements.txt

$stockfish = 'D:\Trí tuệ nhân tạo\stockfish-windows-x86-64-universal\stockfish\stockfish-windows-x86-64-universal.exe'
if (Test-Path $stockfish) {
    $env:STOCKFISH_PATH = $stockfish
    Write-Host "Stockfish: $stockfish"
} else {
    Write-Warning 'Không tìm thấy Stockfish tại đường dẫn dự án; hãy đặt biến STOCKFISH_PATH.'
}
Write-Host "Môi trường đã sẵn sàng. Kích hoạt bằng: .\.venv312\Scripts\Activate.ps1"
