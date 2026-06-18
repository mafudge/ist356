# Dev Container Prerequisites — Installation Guide

Everything you need to clone a Git repo and run it in a VS Code Dev Container, with command-line install steps for **Windows**, **macOS**, and **Ubuntu**.

## What gets installed

On every platform you end up with the same four things:

- **Git** — to clone the repo
- **Visual Studio Code** — the editor
- **Dev Containers extension** (`ms-vscode-remote.remote-containers`) — drives the container workflow
- **A container runtime** — Docker Desktop (Windows/macOS) or Docker Engine (Ubuntu)

---

## Quick start — run the script remotely

If you host these scripts at a URL (e.g. a GitHub raw link), you can run each one in a single command without downloading it first. Replace `<BASE_URL>` with wherever you host them — for a GitHub repo this looks like `https://raw.githubusercontent.com/<user>/<repo>/main`.

**Windows** (PowerShell as Administrator):

```powershell
irm <BASE_URL>/windows.ps1 | iex
```

**macOS** (Terminal):

```bash
curl -fsSL <BASE_URL>/macos.sh | bash
```

**Ubuntu** (Terminal):

```bash
curl -fsSL <BASE_URL>/ubuntu.sh | bash
```

> **Safety note:** piping a remote script straight into a shell runs whatever the URL returns. Only do this with a source you control or trust, and prefer pinning to a specific commit/tag rather than `main` so the content can't change underneath you. If you'd rather inspect first, download and review before running:
>
> ```bash
> curl -fsSL <BASE_URL>/install-prereqs-ubuntu.sh -o install-prereqs-ubuntu.sh
> less install-prereqs-ubuntu.sh   # review
> chmod +x install-prereqs-ubuntu.sh && ./install-prereqs-ubuntu.sh
> ```
>
> On macOS the Ubuntu sudo prompts won't appear, but the `curl | bash` scripts may still prompt for your password mid-run (for `sudo`/Homebrew) — piping doesn't suppress those.

---

## Windows

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

## macOS

Run in **Terminal**. Uses [Homebrew](https://brew.sh).

```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Git
brew install git

# Visual Studio Code
brew install --cask visual-studio-code

# Docker Desktop
brew install --cask docker

# Dev Containers extension
code --install-extension ms-vscode-remote.remote-containers
```

**After installing:**

1. Launch **Docker Desktop** once (`open -a Docker`) to start the daemon — Homebrew installs it but doesn't start it.
2. On Apple Silicon, the cask automatically pulls the correct ARM build.

---

## Ubuntu

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

## Verify everything works

On any platform, confirm the runtime is up before opening a dev container:

```bash
docker run hello-world
```

Then in VS Code: clone the repo → **Reopen in Container** when prompted (or run **Dev Containers: Clone Repository in Container Volume** from the command palette). VS Code reads `.devcontainer/devcontainer.json` and builds the container automatically.
