#!/usr/bin/env bash
# install-prereqs-ubuntu.sh
# Dev Container prerequisites for Ubuntu (installs Docker Engine natively).
# Usage:  chmod +x install-prereqs-ubuntu.sh && ./install-prereqs-ubuntu.sh

set -euo pipefail

echo "==> Installing Git..."
sudo apt update
sudo apt install -y git wget gpg apt-transport-https curl

echo "==> Adding Microsoft apt repo and installing VS Code..."
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" | sudo tee /etc/apt/sources.list.d/vscode.list
rm -f packages.microsoft.gpg
sudo apt update
sudo apt install -y code

echo "==> Installing Docker Engine..."
curl -fsSL https://get.docker.com | sudo sh

echo "==> Adding $USER to the docker group..."
sudo usermod -aG docker "$USER"

echo "==> Installing Dev Containers extension..."
code --install-extension ms-vscode-remote.remote-containers

echo ""
echo "Done. NEXT STEPS:"
echo "  1. Log out and back in (or run: newgrp docker) so the docker group takes effect."
echo "  2. Verify with: docker run hello-world"