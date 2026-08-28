# windows.ps1
# Dev Container prerequisites for Windows.
# Run in PowerShell AS ADMINISTRATOR:  powershell -ExecutionPolicy Bypass -File .\windows.ps1
#   (or)  irm https://.../0-intro/windows.ps1 | iex
#
# Note: piped into iex this runs inside the student's own PowerShell process,
# so `exit` would close their window instantly. Write-Fatal pauses for ENTER
# before exiting so the message is readable either way -- keep that pause.

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
        [Parameter(Mandatory)][scriptblock] $Command,
        [int[]] $AllowExitCodes = @()
    )
    Write-Host "==> $Description" -ForegroundColor Cyan
    & $Command
    if ($LASTEXITCODE -ne 0 -and $AllowExitCodes -notcontains $LASTEXITCODE) {
        throw "$Description failed (exit code $LASTEXITCODE). Nothing after this point would have worked, so stopping here."
    }
}

# winget reports failure when a package is already present, which is exactly
# what happens every time a student re-runs this script after the reboot we
# ask them for. Treat "already installed" and "no upgrade available" as success.
$WingetAlreadyInstalled = @(
    -1978335135,  # 0x8A150061 APPINSTALLER_CLI_ERROR_PACKAGE_ALREADY_INSTALLED
    -1978335189,  # 0x8A15002B APPINSTALLER_CLI_ERROR_UPDATE_NOT_APPLICABLE
    -1978335212   # 0x8A150014 APPINSTALLER_CLI_ERROR_NO_APPLICATIONS_FOUND (re-run edge case)
)

function Write-Fatal {
    # No [Parameter(Mandatory)] here on purpose: a mandatory [string[]] refuses
    # to bind an array containing empty strings, and every message below uses
    # "" for blank lines.
    param([string[]] $Lines = @())
    Write-Host ""
    foreach ($line in $Lines) { Write-Host $line -ForegroundColor Red }
    Write-Host ""
    # Hold the window open. This script is normally piped into iex, which runs
    # it inside the student's own PowerShell process, so the `exit` below would
    # otherwise close the whole window and the message above is never read.
    try { Read-Host "Press ENTER to close" | Out-Null } catch { }
    exit 1
}

# Who is actually sitting at this machine? NOT $env:USERNAME -- when a process
# is elevated as a different account, that account's environment comes with it,
# so $env:USERNAME reports the elevated user and the mismatch is invisible.
# The owner of explorer.exe is the interactive session's real user.
function Get-InteractiveUser {
    try {
        $explorer = Get-CimInstance Win32_Process -Filter "Name='explorer.exe'" -ErrorAction Stop |
                    Select-Object -First 1
        if (-not $explorer) { return $null }
        $owner = Invoke-CimMethod -InputObject $explorer -MethodName GetOwner -ErrorAction Stop
        if ($owner.ReturnValue -ne 0) { return $null }
        return "$($owner.Domain)\$($owner.User)"
    } catch {
        return $null   # can't tell; don't block on it
    }
}

# winget ships inside "App Installer", a PER-USER package surfaced through
# %LOCALAPPDATA%\Microsoft\WindowsApps. That is why it vanishes in a session
# elevated as somebody else, and why "winget is not recognized" is such a
# common failure here.
function Resolve-Winget {
    $cmd = Get-Command winget -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }

    # $env:LOCALAPPDATA can be missing in odd elevation contexts -- which is
    # precisely when this function matters -- so never hand Join-Path a null.
    $userPath = $null
    if ($env:LOCALAPPDATA) {
        $userPath = Join-Path $env:LOCALAPPDATA "Microsoft\WindowsApps\winget.exe"
        if (Test-Path $userPath) { return $userPath }
    }

    # Usual cure when App Installer is present but not wired into this session.
    try {
        Add-AppxPackage -RegisterByFamilyName `
                        -MainPackage Microsoft.DesktopAppInstaller_8wekyb3d8bbwe `
                        -ErrorAction Stop
        $cmd = Get-Command winget -ErrorAction SilentlyContinue
        if ($cmd) { return $cmd.Source }
        if ($userPath -and (Test-Path $userPath)) { return $userPath }
    } catch {
        # fall through to the caller's error message
    }

    return $null
}

# wsl.exe prints UTF-16LE, which arrives as text riddled with null bytes unless
# the console is told what to expect. Without this the distro list looks like
# gibberish and never matches anything.
function Get-WslDistro {
    $previousEncoding = [Console]::OutputEncoding
    try {
        [Console]::OutputEncoding = [Text.Encoding]::Unicode
        $raw = & wsl.exe --list --quiet 2>$null
    } catch {
        return @()
    } finally {
        [Console]::OutputEncoding = $previousEncoding
    }
    # docker-desktop registers distros of its own; they are plumbing, not a
    # Linux environment the student can use.
    return @($raw |
             ForEach-Object { ($_ -replace "`0", "").Trim() } |
             Where-Object { $_ -ne "" -and $_ -notmatch '^docker-desktop' })
}

# Run wsl.exe with a time limit, in a background job so it can never sit
# waiting on the keyboard. A distro that has not completed its first run wants
# to start an interactive setup wizard; from a job that fails fast instead of
# hanging this script forever. Returns the exit code, or $null on timeout.
function Invoke-WslWithTimeout {
    param(
        [Parameter(Mandatory)][string[]] $Arguments,
        [int] $TimeoutSeconds = 90
    )
    $job = Start-Job -ScriptBlock {
        param($wslArgs)
        & wsl.exe @wslArgs *> $null
        $LASTEXITCODE
    } -ArgumentList (, $Arguments)

    if (-not (Wait-Job -Job $job -Timeout $TimeoutSeconds)) {
        Stop-Job   -Job $job -ErrorAction SilentlyContinue
        Remove-Job -Job $job -Force -ErrorAction SilentlyContinue
        return $null
    }
    $code = Receive-Job -Job $job -ErrorAction SilentlyContinue
    Remove-Job -Job $job -Force -ErrorAction SilentlyContinue
    if ($code -is [array]) { $code = $code | Select-Object -Last 1 }
    if ($null -eq $code)   { return $null }
    return [int]$code
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

# If the UAC prompt was cleared with SOMEBODY ELSE'S administrator account,
# this whole script runs as that person. winget disappears (it is per-user),
# and anything that does install lands in their profile, not the student's.
# There is no way to salvage that, so stop rather than produce a broken setup.
$elevatedUser    = $identity.Name
$interactiveUser = Get-InteractiveUser
if ($interactiveUser -and ($elevatedUser -ne $interactiveUser)) {
    Write-Fatal @(
        "STOP: this window is running as the wrong user.",
        "",
        "  You are logged in as:      $interactiveUser",
        "  This window is running as: $elevatedUser",
        "",
        "That happens when the User Account Control prompt asked for an",
        "administrator's username and password, and a different account was",
        "entered -- which means your own account is not an administrator.",
        "",
        "If this script continued, Git, VS Code and its extensions would all",
        "install for '$elevatedUser' instead of for you, and the dev container",
        "would never work from your login. The 'winget is not recognized'",
        "error comes from this too: winget is installed per-user, so it does",
        "not exist for the account that was elevated.",
        "",
        "You have three options:",
        "",
        "  1. Sign in to Windows directly as an administrator account and run",
        "     this script there.",
        "  2. If this is a school- or work-managed PC, ask your IT support to",
        "     make YOUR account an administrator.",
        "  3. Skip the local install entirely and use GitHub Codespaces --",
        "     see Step 1 option 2 in 0-intro/0-0-setup.md. Nothing to install."
    )
}

# ---------------------------------------------------------------------------
# Windows version and winget
# ---------------------------------------------------------------------------
Write-Host "==> Checking Windows version..." -ForegroundColor Cyan
$build = [int](Get-CimInstance Win32_OperatingSystem).BuildNumber
if ($build -lt 17763) {
    Write-Fatal @(
        "STOP: this version of Windows is too old (build $build).",
        "",
        "This course needs Windows 10 version 1809 (build 17763) or newer,",
        "and realistically Windows 11 for a good experience.",
        "",
        "Run Windows Update, then try again. If this PC cannot be updated,",
        "use GitHub Codespaces instead -- see Step 1 option 2 in",
        "0-intro/0-0-setup.md."
    )
}

Write-Host "==> Locating winget..." -ForegroundColor Cyan
$winget = Resolve-Winget
if (-not $winget) {
    Write-Fatal @(
        "STOP: winget is not available.",
        "",
        "winget is part of 'App Installer'. It ships with Windows 11 and with",
        "current Windows 10, but it is missing here.",
        "",
        "To fix it:",
        "",
        "  1. Open the Microsoft Store, search for 'App Installer', and",
        "     install or update it. Then run this script again in a NEW",
        "     PowerShell window.",
        "  2. If there is no Microsoft Store on this PC, download App Installer",
        "     directly from  https://aka.ms/getwinget  and install it.",
        "",
        "Then confirm it works by running:  winget --version"
    )
}
Write-Host "    Using: $winget"

# ---------------------------------------------------------------------------
# WSL 2
#
# On a machine that doesn't have it yet, `wsl --install` needs a REBOOT before
# WSL works and before Docker Desktop can start its engine. Continuing past
# that point installs Docker against a backend that cannot run, which is what
# makes "Reopen in Container" hang forever with no error.
# ---------------------------------------------------------------------------
if (-not (Get-Command wsl -ErrorAction SilentlyContinue)) {
    Write-Fatal @(
        "STOP: the 'wsl' command is not available on this PC.",
        "",
        "WSL 2 is what Docker Desktop runs containers on, so it is required.",
        "",
        "Run Windows Update and install everything it offers, restart, then",
        "run this script again. If this PC is managed by an IT department,",
        "they may have blocked WSL -- in that case use GitHub Codespaces,",
        "see Step 1 option 2 in 0-intro/0-0-setup.md."
    )
}

Write-Host "==> Enabling WSL 2 and installing Ubuntu (may require a reboot)..." -ForegroundColor Cyan
# Name the distro explicitly. `wsl --install` on its own has meant different
# things across Windows builds -- on some it installs Ubuntu, on others it only
# turns the feature on and leaves the machine with no distro at all, which is
# invisible until Docker's WSL integration list turns up empty.
wsl --install -d Ubuntu

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
# Ubuntu's FIRST RUN.
#
# Installing a distro only downloads it. It is not finished until it has been
# launched once and a UNIX user has been created -- and an unfinished distro
# does not appear in Docker Desktop under Settings -> Resources -> WSL
# integration, so there is nothing there for Docker to integrate with. That
# first run prompts for a username and password, so it cannot be automated;
# hand the console to the student instead of trying.
# ---------------------------------------------------------------------------
Write-Host "==> Checking the Ubuntu WSL distro..." -ForegroundColor Cyan
$distros = Get-WslDistro
if ($distros.Count -eq 0) {
    Write-Host "    No Linux distro is installed yet. Installing Ubuntu..."
    wsl --install -d Ubuntu
    $distros = Get-WslDistro
}

if ($distros.Count -eq 0) {
    Write-Fatal @(
        "STOP: no WSL Linux distro is installed.",
        "",
        "Docker Desktop runs your containers inside a WSL 2 Linux distro, so",
        "without one nothing in this course will run.",
        "",
        "  1. Run:  wsl --install -d Ubuntu",
        "  2. Restart your computer if it asks you to.",
        "  3. Run:  wsl          (and create a UNIX username and password)",
        "  4. Run this script again.",
        "",
        "If this PC is managed by an IT department they may have blocked WSL.",
        "In that case use GitHub Codespaces -- see Step 1 option 2 in",
        "0-intro/0-0-setup.md."
    )
}
Write-Host "    Installed distro(s): $($distros -join ', ')"

# Can the default distro actually run a command? One that has not completed its
# first run cannot -- it wants to show its setup wizard instead.
$distroReady = ((Invoke-WslWithTimeout -Arguments @("-e", "true")) -eq 0)

if (-not $distroReady) {
    Write-Host ""
    Write-Host "ONE MANUAL STEP: Ubuntu has to be started once to finish installing." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "  Ubuntu will now open and ask you to CREATE A UNIX USERNAME AND"
    Write-Host "  PASSWORD. This is a brand new account that lives inside Ubuntu."
    Write-Host "  It is NOT your Windows login, your NetID, or your GitHub account."
    Write-Host "  Pick something short you will remember, and write it down."
    Write-Host ""
    Write-Host "  NOTHING APPEARS ON SCREEN WHILE YOU TYPE THE PASSWORD -- no dots,"
    Write-Host "  no asterisks. That is normal, not a broken keyboard."
    Write-Host ""
    Write-Host '  When you reach a prompt that looks like  you@yourpc:~$  type'
    Write-Host "  exit  and press ENTER to come back here."
    Write-Host ""
    try { Read-Host "Press ENTER to start Ubuntu" | Out-Null } catch { }

    wsl.exe

    Write-Host ""
    Write-Host "==> Re-checking the Ubuntu WSL distro..." -ForegroundColor Cyan
    $distroReady = ((Invoke-WslWithTimeout -Arguments @("-e", "true")) -eq 0)
}

if (-not $distroReady) {
    Write-Fatal @(
        "STOP: the Ubuntu distro still isn't finished installing.",
        "",
        "It is installed but cannot run a command yet, which means its",
        "first-time setup did not complete. Docker Desktop will not be able to",
        "integrate with it in that state.",
        "",
        "  1. Open PowerShell and run:  wsl",
        "  2. Create the UNIX username and password it asks for.",
        "  3. When you get a Linux prompt, type:  exit",
        "  4. Run this script again.",
        "",
        "If 'wsl' reports an error instead of asking for a username, try:",
        "",
        "     wsl --unregister Ubuntu",
        "     wsl --install -d Ubuntu",
        "",
        "then repeat from step 1. (Unregister deletes the Ubuntu distro and",
        "anything stored in it -- fine here, since it never finished setting up.)"
    )
}
Write-Host "    Ubuntu is set up and can run commands." -ForegroundColor Green

# ---------------------------------------------------------------------------
# Packages
# ---------------------------------------------------------------------------
Invoke-Step "Installing Git..." -AllowExitCodes $WingetAlreadyInstalled {
    & $winget install --id Git.Git -e --accept-source-agreements --accept-package-agreements
}

Invoke-Step "Installing Visual Studio Code..." -AllowExitCodes $WingetAlreadyInstalled {
    & $winget install --id Microsoft.VisualStudioCode -e --accept-source-agreements --accept-package-agreements
}

Invoke-Step "Installing Docker Desktop..." -AllowExitCodes $WingetAlreadyInstalled {
    & $winget install --id Docker.DockerDesktop -e --accept-source-agreements --accept-package-agreements
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
        "  3. In Docker Desktop: Settings -> Resources -> WSL integration,",
        "     tick 'Enable integration with my default WSL distro', switch the",
        "     'Ubuntu' toggle on, and click Apply & restart.",
        "",
        "Then run this script again."
    )
}

Write-Host "    Docker engine is running." -ForegroundColor Green

# ---------------------------------------------------------------------------
# Docker <-> WSL integration.
#
# Docker Desktop only exposes the docker command inside a distro that is switched
# on under Settings -> Resources -> WSL integration. The "default WSL distro"
# checkbox is on out of the box, but the per-distro toggle for Ubuntu is not,
# and Docker exposes no supported command line for it -- so this is a GUI step
# the student has to do. Running docker from inside Ubuntu is the honest test of
# whether they did.
# ---------------------------------------------------------------------------
Write-Host "==> Checking that Docker is integrated with WSL..." -ForegroundColor Cyan
$wslDockerOk = ((Invoke-WslWithTimeout -Arguments @("-e", "docker", "info")) -eq 0)

$attempts = 0
while (-not $wslDockerOk -and $attempts -lt 3) {
    $attempts++
    Write-Host ""
    Write-Host "ONE MANUAL STEP: Docker is not switched on for Ubuntu yet." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "  In the Docker Desktop window:"
    Write-Host ""
    Write-Host "    1. Click the gear icon (Settings), top right."
    Write-Host "    2. Choose  Resources  in the left sidebar."
    Write-Host "    3. Click the  WSL integration  tab."
    Write-Host "    4. TICK      'Enable integration with my default WSL distro'"
    Write-Host "    5. SWITCH ON the 'Ubuntu' toggle underneath, in"
    Write-Host "                 'Enable integration with additional distros'"
    Write-Host "    6. Click  Apply & restart  and wait for 'Engine running'."
    Write-Host ""
    Write-Host "  There is a screenshot of this screen in"
    Write-Host "  0-intro/0-1-install-pre-reqs.md (Windows, step 5)."
    Write-Host ""
    try { Read-Host "Press ENTER once you have done that" | Out-Null } catch { }

    Write-Host "==> Re-checking Docker's WSL integration..." -ForegroundColor Cyan
    $wslDockerOk = ((Invoke-WslWithTimeout -Arguments @("-e", "docker", "info")) -eq 0)
}

if (-not $wslDockerOk) {
    Write-Fatal @(
        "STOP: Docker still is not available inside Ubuntu.",
        "",
        "Everything is installed, but Docker Desktop is not integrated with",
        "your WSL 2 distro, so the two halves of the setup cannot talk to each",
        "other.",
        "",
        "In Docker Desktop go to  Settings -> Resources -> WSL integration  and",
        "make sure BOTH of these are set:",
        "",
        "  - 'Enable integration with my default WSL distro' is TICKED",
        "  - the 'Ubuntu' toggle under 'Enable integration with additional",
        "    distros' is switched ON",
        "",
        "Click Apply & restart, wait for 'Engine running', then run this script",
        "again. You can check it yourself at any time with:",
        "",
        "     wsl -e docker run hello-world",
        "",
        "If 'Ubuntu' is not in that list at all, its first-time setup never",
        "finished. Run  wsl  in PowerShell, create a UNIX username and password,",
        "type  exit  , then restart Docker Desktop."
    )
}

Write-Host "    Docker is available inside Ubuntu." -ForegroundColor Green

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
Write-Host "  - The Ubuntu distro is installed and its first-run setup is complete"
Write-Host "  - Git, VS Code and Docker Desktop are installed"
Write-Host "  - The Dev Containers extension is installed"
Write-Host "  - The Docker engine is running"
Write-Host "  - Docker Desktop is integrated with the Ubuntu WSL distro"
Write-Host ""
Write-Host "NEXT STEPS:" -ForegroundColor Green
Write-Host "  1. Sanity check:  docker run hello-world"
Write-Host "  2. Continue with Course Setup (0-intro/0-0-setup.md) to clone the"
Write-Host "     repo and open it in the dev container."
Write-Host ""
Write-Host "  Leave Docker Desktop running. If you reboot, start Docker Desktop"
Write-Host "  before opening the dev container in VS Code."
