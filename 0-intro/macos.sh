#!/usr/bin/env bash
# install-prereqs-macos.sh
# Dev Container prerequisites for macOS.
# Usage:  chmod +x install-prereqs-macos.sh && ./install-prereqs-macos.sh
 
set -euo pipefail
 
echo "==> Checking for Homebrew..."
if ! command -v brew >/dev/null 2>&1; then
  echo "    Installing Homebrew..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  # Make brew available in this session (Apple Silicon vs Intel paths)
  if [ -x /opt/homebrew/bin/brew ]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
  elif [ -x /usr/local/bin/brew ]; then
    eval "$(/usr/local/bin/brew shellenv)"
  fi
fi
 
echo "==> Installing Git..."
brew install git
 
echo "==> Installing Visual Studio Code..."
brew install --cask visual-studio-code
 
echo "==> Installing Docker Desktop..."
brew install --cask docker
 
echo "==> Installing Dev Containers extension..."
code --install-extension ms-vscode-remote.remote-containers
 
echo ""
echo "Done. NEXT STEPS:"
echo "  1. Launch Docker Desktop once:  open -a Docker"
echo "  2. Verify with: docker run hello-world"