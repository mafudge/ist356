# install-prereqs.ps1
# Dev Container prerequisites for Windows.
# Run in PowerShell AS ADMINISTRATOR:  powershell -ExecutionPolicy Bypass -File .\install-prereqs.ps1
 
$ErrorActionPreference = "Stop"
 
Write-Host "==> Enabling WSL 2 (may require a reboot to complete)..." -ForegroundColor Cyan
wsl --install
 
Write-Host "==> Installing Git..." -ForegroundColor Cyan
winget install --id Git.Git -e --accept-source-agreements --accept-package-agreements
 
Write-Host "==> Installing Visual Studio Code..." -ForegroundColor Cyan
winget install --id Microsoft.VisualStudioCode -e --accept-source-agreements --accept-package-agreements
 
Write-Host "==> Installing Docker Desktop..." -ForegroundColor Cyan
winget install --id Docker.DockerDesktop -e --accept-source-agreements --accept-package-agreements
 
Write-Host "==> Installing Dev Containers extension..." -ForegroundColor Cyan
# 'code' may not be on PATH until a new shell; resolve it if needed.
$code = Get-Command code -ErrorAction SilentlyContinue
if (-not $code) {
    $code = "$env:LOCALAPPDATA\Programs\Microsoft VS Code\bin\code.cmd"
}
& $code --install-extension ms-vscode-remote.remote-containers
 
Write-Host ""
Write-Host "Done. NEXT STEPS:" -ForegroundColor Green
Write-Host "  1. Reboot to finish WSL 2 setup."
Write-Host "  2. Launch Docker Desktop once to complete WSL integration."
Write-Host "  3. Verify with: docker run hello-world"
 