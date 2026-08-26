# Dev Container Prerequisites — Installation Guide

Everything you need to clone a Git repo and run it in a VS Code Dev Container, with command-line install steps for **Windows**, **macOS**, and **Ubuntu**. This is software you will need to install to work on code in this course.

## What gets installed

On every platform you end up with the same four things:

- **Git** — to clone the repo, commit your changes, and share to Github.
- **Visual Studio Code** — the integrated development environment: editor, debugger
- **Dev Containers extension** (`ms-vscode-remote.remote-containers`) — drives the container workflow. runs your code in isolation on your computer
- **A container runtime** — Docker Desktop (Windows/macOS) or Docker Engine (Ubuntu). This isolates the code.

### Installing

You can install the pre-requisites using a script or run the commands manually yourself.

1. If you want to use the script, see **Script Setup**
2. To type the command yourself, see **Manual Setup**

---

## Script Setup

If you don't want to run the commands manually, you can try these automated scripts. You will download code and it will attempt to setup automatically. 

**NOTE:** if they don't work try the manual setup.

**Windows** (Open PowerShell as Administrator):

```powershell
irm https://raw.githubusercontent.com/mafudge/ist356/refs/heads/main/0-intro/windows.ps1 | iex
```

**macOS** (Open a Terminal):

```bash
curl -fsSL https://raw.githubusercontent.com/mafudge/ist356/refs/heads/main/0-intro/macos.sh | bash
```

**Ubuntu** (Open a Terminal):

```bash
curl -fsSL https://raw.githubusercontent.com/mafudge/ist356/refs/heads/main/0-intro/ubuntu.sh | bash
```

> **Safety note:** piping a remote script straight into a shell runs whatever the URL returns. Only do this with a source you control or trust, and prefer pinning to a specific commit/tag rather than `main` so the content can't change underneath you. If you'd rather inspect first, download and review before running:
>
> ```bash
> curl -fsSL https://raw.githubusercontent.com/mafudge/ist356/refs/heads/main/0-intro/ubuntu.sh -o ubuntu.sh
> less ubuntu.sh   # review
> chmod +x ubuntu.sh && ./ubuntu.sh
> ```
>
> **About the password prompt (macOS and Ubuntu):** these scripts will stop and ask for your computer's login password. **Nothing appears on screen as you type it** — no dots, no asterisks. That is normal, not a broken keyboard. Type your password and press ENTER. On macOS you also need to be an **administrator** on the Mac, because Docker Desktop can't install without admin rights. See [Troubleshooting (macOS)](#troubleshooting-macos) below if you get stuck on this.

---

## Manual Setup

### Windows

Run in **PowerShell as Administrator**. Windows 10/11 includes `winget`.

```powershell
# Enable WSL 2 (installs WSL + default Ubuntu distro, sets WSL 2 as default)
wsl --install

# Git
winget install --id Git.Git -e

# Visual Studio Code
winget install --id Microsoft.VisualStudioCode -e

# Docker Desktop (uses the WSL 2 backend by default)
winget install --id Docker.DockerDesktop -e

# Dev Containers extension
code --install-extension ms-vscode-remote.remote-containers
```

**After installing:**

1. **Reboot** to finish WSL 2 setup.
2. Launch **Docker Desktop** once so it completes WSL integration.
3. Open a fresh terminal if `code` isn't recognized (PATH refresh).

> Requires virtualization enabled in BIOS/UEFI.

---

### macOS

Run in **Terminal**. Uses [Homebrew](https://brew.sh).

```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Git
brew install git

# Visual Studio Code
brew install --cask visual-studio-code

# Docker Desktop
brew install --cask docker-desktop

# Dev Containers extension
code --install-extension ms-vscode-remote.remote-containers
```

> The Docker Desktop cask used to be called `docker`. It was renamed to `docker-desktop` — `brew install docker` on its own now installs only the command-line tool, without the Docker Desktop app you need for this course.

**After installing:**

1. Launch **Docker Desktop** once (`open -a Docker`) to start the daemon — Homebrew installs it but doesn't start it. It will ask for your password again so it can install its networking components; this is expected.
2. On Apple Silicon, the cask automatically pulls the correct ARM build.
3. You must be an **administrator** on this Mac. If you aren't, see [Troubleshooting (macOS)](#troubleshooting-macos).

---

### Ubuntu Linux

Run in **Terminal**. Installs Docker Engine natively (no Docker Desktop needed).

```bash
# Git
sudo apt update && sudo apt install -y git

# VS Code — add Microsoft's apt repo, then install
sudo apt install -y wget gpg apt-transport-https
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" | sudo tee /etc/apt/sources.list.d/vscode.list
rm -f packages.microsoft.gpg
sudo apt update && sudo apt install -y code

# Docker Engine — via Docker's official convenience script
curl -fsSL https://get.docker.com | sudo sh

# Run Docker without sudo (log out / back in afterward)
sudo usermod -aG docker $USER

# Dev Containers extension
code --install-extension ms-vscode-remote.remote-containers
```

**After installing:**

1. **Log out and back in** (or run `newgrp docker`) so the `docker` group takes effect.

---

## Troubleshooting (macOS)

Almost every macOS setup problem in this course is one of these three. Find your symptom.

### "Terminal is asking for a password, but nothing happens when I type."

**It is working.** For security, the terminal shows *nothing at all* while you type a password — no dots, no asterisks, no moving cursor. It looks identical to a frozen screen or a dead keyboard.

**What to do:** Type your Mac login password anyway and press **ENTER**.

If you mistype it, you'll see `Sorry, try again.` and get two more attempts. After three, you'll see `3 incorrect password attempts` and the command quits — that isn't a lockout, just re-run the command and try again.

### "A window is asking me to log in as an administrator, and my password is rejected."

Read that window carefully. If it asks for **an administrator's name and password** (with a *username* box, not just a password box), macOS is telling you that **your account is not an administrator**. Your own password will be rejected every time, no matter how carefully you type it. This is not a typo and not a bug.

**Check whether you're an admin:** Open  → **System Settings** → **Users & Groups**. Find your account in the list. Underneath your name it says either **Administrator** or **Standard**.

**If it says Standard, pick one of these:**

1. **Get an administrator to authorize it.** If someone else set up this Mac, have them enter their name and password at the prompt, or run the install for you.
2. **Ask IT for admin rights.** If this is a school- or employer-managed Mac (it was handed to you already configured, or it force-installs software), your account was deliberately made Standard. You'll need to request administrator access from whoever manages it — for SU-managed machines that's [ITS](https://its.syr.edu/).
3. **Use GitHub Codespaces instead.** 👈 *This is the fastest unblock.* Codespaces runs the whole course environment in your browser with **nothing installed on your Mac and no admin rights required**. See **Step 1, option 2** in [Course Setup](0-0-setup.md). You can always come back and install locally later.

### "Docker Desktop keeps asking for my password when I launch it."

Expected. The first time Docker Desktop runs, it installs a privileged helper for its networking components, and macOS requires administrator approval for that. Enter your password and allow it.

If that prompt won't accept your password, you're in the previous case — your account is Standard, not Administrator.

---

## Verify everything works

On any platform, confirm the Docker runtime works.

```bash
docker run hello-world
```

After that you can continue with the [Course Setup](0-0-setup.md)
