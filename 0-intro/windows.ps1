# windows.ps1
# Dev Container prerequisites for Windows.
# Run in PowerShell AS ADMINISTRATOR:  powershell -ExecutionPolicy Bypass -File .\windows.ps1

$ErrorActionPreference = "Stop"

$DevContainerExtension = "ms-vscode-remote.remote-containers"
$CourseImage           = "mafudge/ist356:latest"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

# $ErrorActionPreference = "Stop" does NOT react to native programs like winget
# and wsl -- they report failure through an exit code, not a PowerShell error.
# Without this wrapper the script sails past a failed install and still prints
# "Done", which is how a broken setup looks like a working one.
function Invoke-Step {
    param(
        [Parameter(Mandatory)][string] $Description,
        [Parameter(Mandatory)][scriptblock] $Command
    )
    Write-Host "==> $Description" -ForegroundColor Cyan
    & $Command
    if ($LASTEXITCODE -ne 0) {
        throw "$Description failed (exit code $LASTEXITCODE). Nothing after this point would have worked, so stopping here."
    }
}

function Write-Fatal {
    param([Parameter(Mandatory)][string[]] $Lines)
    Write-Host ""
    foreach ($line in $Lines) { Write-Host $line -ForegroundColor Red }
    Write-Host ""
    exit 1
}

# ---------------------------------------------------------------------------
# Are you running as Administrator?
#
# Installing WSL 2 and Docker Desktop requires it. Stop now with a useful
# message rather than failing halfway through with a wall of red text.
# ---------------------------------------------------------------------------
Write-Host "==> Checking for Administrator rights..." -ForegroundColor Cyan
$identity  = [Security.Principal.WindowsIdentity]::GetCurrent()
$principal = New-Object Security.Principal.WindowsPrincipal($identity)
if (-not $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Fatal @(
        "STOP: this PowerShell window is not running as Administrator.",
        "",
        "Installing WSL 2 and Docker Desktop requires administrator rights,",
        "so this script cannot continue. You have three options:",
        "",
        "  1. Close this window. Click Start, type 'PowerShell', right-click",
        "     'Windows PowerShell' and choose 'Run as administrator'. Then run",
        "     this script again.",
        "  2. If this is a school- or work-managed PC, ask your IT support for",
        "     administrator rights on your account.",
        "  3. Skip the local install entirely and use GitHub Codespaces --",
        "     see Step 1 option 2 in 0-intro/0-0-setup.md. Nothing to install."
    )
}

# If the student cleared the UAC prompt using SOMEBODY ELSE'S administrator
# account, VS Code and its extensions install into that account's profile.
# Everything then "installs fine" but their own login has no Dev Containers
# extension -- a confusing failure worth naming up front.
$elevatedUser    = $identity.Name
$interactiveUser = "$env:USERDOMAIN\$env:USERNAME"
if ($elevatedUser -ne $interactiveUser) {
    Write-Host ""
    Write-Host "WARNING: This window is elevated as '$elevatedUser', but you are" -ForegroundColor Yellow
    Write-Host "         logged in as '$interactiveUser'." -ForegroundColor Yellow
    Write-Host "         VS Code and its extensions will be installed for" -ForegroundColor Yellow
    Write-Host "         '$elevatedUser', NOT for you, and the dev container will" -ForegroundColor Yellow
    Write-Host "         not work from your own login." -ForegroundColor Yellow
    Write-Host "         See 'Troubleshooting (Windows)' in 0-1-install-pre-reqs.md." -ForegroundColor Yellow
    Write-Host ""
}

# ---------------------------------------------------------------------------
# WSL 2
#
# On a machine that doesn't have it yet, `wsl --install` needs a REBOOT before
# WSL works and before Docker Desktop can start its engine. Continuing past
# that point installs Docker against a backend that cannot run, which is what
# makes "Reopen in Container" hang forever with no error.
# ---------------------------------------------------------------------------
Write-Host "==> Enabling WSL 2 (may require a reboot to complete)..." -ForegroundColor Cyan
wsl --install

# Deliberately ignore the exit code of `wsl --install` -- on a machine that
# already has WSL it reports failure (or just prints help) even though
# everything is fine. `wsl --status` is the honest test of whether WSL works.
wsl --status *> $null
$wslReady = ($LASTEXITCODE -eq 0)

if (-not $wslReady) {
    Write-Fatal @(
        "REBOOT REQUIRED.",
        "",
        "WSL 2 has been installed but cannot be used until this PC restarts.",
        "Docker Desktop will not be able to start its engine until then, and",
        "the dev container would hang forever with no error message.",
        "",
        "  1. Restart your computer now.",
        "  2. Run this exact same script again afterwards.",
        "",
        "It will pick up where it left off and skip anything already installed."
    )
}

# ---------------------------------------------------------------------------
# Packages
# ---------------------------------------------------------------------------
Invoke-Step "Installing Git..." {
    winget install --id Git.Git -e --accept-source-agreements --accept-package-agreements
}

Invoke-Step "Installing Visual Studio Code..." {
    winget install --id Microsoft.VisualStudioCode -e --accept-source-agreements --accept-package-agreements
}

Invoke-Step "Installing Docker Desktop..." {
    winget install --id Docker.DockerDesktop -e --accept-source-agreements --accept-package-agreements
}

# ---------------------------------------------------------------------------
# Dev Containers extension
#
# `code` is usually not on PATH until a new shell, so fall back to the known
# install locations -- both the per-user and the machine-wide one.
# ---------------------------------------------------------------------------
Write-Host "==> Locating the VS Code command line (code)..." -ForegroundColor Cyan
$code = $null
$found = Get-Command code -ErrorAction SilentlyContinue
if ($found) {
    $code = $found.Source
} else {
    $candidates = @(
        "$env:LOCALAPPDATA\Programs\Microsoft VS Code\bin\code.cmd",  # user install (winget default)
        "$env:ProgramFiles\Microsoft VS Code\bin\code.cmd",           # machine-wide install
        "${env:ProgramFiles(x86)}\Microsoft VS Code\bin\code.cmd"
    )
    foreach ($candidate in $candidates) {
        if (Test-Path $candidate) { $code = $candidate; break }
    }
}

if (-not $code) {
    Write-Fatal @(
        "Could not find the VS Code command line tool (code.cmd).",
        "",
        "VS Code reported that it installed, but it isn't where we expected.",
        "Close this window, open a NEW PowerShell as Administrator, and run",
        "this script again -- that usually resolves it, because PATH is only",
        "refreshed for new windows.",
        "",
        "If it still fails, install the extension by hand: open VS Code, click",
        "the Extensions icon in the left sidebar, search for 'Dev Containers',",
        "and click Install."
    )
}

Invoke-Step "Installing Dev Containers extension..." {
    & $code --install-extension $DevContainerExtension
}

# Confirm it really landed, rather than assuming the command worked.
Write-Host "==> Verifying the Dev Containers extension..." -ForegroundColor Cyan
$installed = & $code --list-extensions
if ($installed -notcontains $DevContainerExtension) {
    Write-Fatal @(
        "The Dev Containers extension does not appear to be installed.",
        "",
        "Without it, VS Code will never offer 'Reopen in Container'.",
        "",
        "Install it by hand: open VS Code, click the Extensions icon in the",
        "left sidebar, search for 'Dev Containers', and click Install."
    )
}

# ---------------------------------------------------------------------------
# Start Docker Desktop and WAIT for the engine.
#
# This is the step whose absence caused the original bug report. Installing
# Docker Desktop does not start it, and on first launch it sits on a
# subscription agreement dialog doing nothing until somebody accepts it. Until
# the engine answers, "Reopen in Container" waits forever and never errors.
# ---------------------------------------------------------------------------
Write-Host "==> Starting Docker Desktop..." -ForegroundColor Cyan
$dockerDesktop = "$env:ProgramFiles\Docker\Docker\Docker Desktop.exe"
if (Test-Path $dockerDesktop) {
    Start-Process -FilePath $dockerDesktop | Out-Null
} else {
    Write-Host "    Could not find Docker Desktop.exe -- start it from the Start menu." -ForegroundColor Yellow
}

Write-Host "==> Waiting for the Docker engine to come up (up to 3 minutes)..." -ForegroundColor Cyan
Write-Host "    If Docker Desktop opens a window asking you to accept its"
Write-Host "    service agreement, accept it now -- the engine will not start"
Write-Host "    until you do."

$engineReady = $false
$deadline = (Get-Date).AddMinutes(3)
while ((Get-Date) -lt $deadline) {
    docker info *> $null
    if ($LASTEXITCODE -eq 0) { $engineReady = $true; break }
    Write-Host "    ...still waiting"
    Start-Sleep -Seconds 5
}

if (-not $engineReady) {
    Write-Fatal @(
        "The Docker engine never started.",
        "",
        "Everything installed, but Docker is not answering. If you stop here,",
        "'Reopen in Container' in VS Code will spin forever WITHOUT showing an",
        "error -- that is this exact problem.",
        "",
        "Check, in order:",
        "  1. Is the Docker Desktop window open, and does it say 'Engine running'",
        "     in the bottom-left corner? If it is showing a service agreement,",
        "     accept it.",
        "  2. Did you restart the PC after WSL 2 was installed?",
        "  3. In Docker Desktop: Settings -> Resources -> WSL Integration,",
        "     make sure integration is enabled.",
        "",
        "Then run this script again."
    )
}

Write-Host "    Docker engine is running." -ForegroundColor Green

# ---------------------------------------------------------------------------
# Pre-pull the course image.
#
# The dev container image is ~1.3 GB. Pulled from inside VS Code it is a tiny
# silent spinner that looks identical to a hang, and students give up. Pull it
# here instead, where Docker prints a real progress bar.
# ---------------------------------------------------------------------------
Write-Host ""
Write-Host "==> Downloading the course container image ($CourseImage)..." -ForegroundColor Cyan
Write-Host "    This is about 1.3 GB and is the slowest part of setup. Doing it"
Write-Host "    now means the dev container opens quickly later, instead of"
Write-Host "    appearing to hang while it downloads in the background."
Write-Host ""
docker pull $CourseImage
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "WARNING: could not download the course image." -ForegroundColor Yellow
    Write-Host "         Everything else is installed, so this is not fatal --" -ForegroundColor Yellow
    Write-Host "         VS Code will download it when you open the dev container." -ForegroundColor Yellow
    Write-Host "         Just expect the first open to take a long time." -ForegroundColor Yellow
}

# ---------------------------------------------------------------------------
Write-Host ""
Write-Host "Done. Verified:" -ForegroundColor Green
Write-Host "  - WSL 2 is working"
Write-Host "  - Git, VS Code and Docker Desktop are installed"
Write-Host "  - The Dev Containers extension is installed"
Write-Host "  - The Docker engine is running"
Write-Host ""
Write-Host "NEXT STEPS:" -ForegroundColor Green
Write-Host "  1. Sanity check:  docker run hello-world"
Write-Host "  2. Continue with Course Setup (0-intro/0-0-setup.md) to clone the"
Write-Host "     repo and open it in the dev container."
Write-Host ""
Write-Host "  Leave Docker Desktop running. If you reboot, start Docker Desktop"
Write-Host "  before opening the dev container in VS Code."
