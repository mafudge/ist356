#!/usr/bin/env bash
# macos.sh
# Dev Container prerequisites for macOS.
# Usage:  chmod +x macos.sh && ./macos.sh
#   (or)  curl -fsSL .../0-intro/macos.sh | bash

set -euo pipefail

# ---------------------------------------------------------------------------
# Are you an administrator?
#
# Homebrew and Docker Desktop both need administrator rights. If this account
# is a "standard" user, macOS asks for an ADMINISTRATOR's name and password --
# your own password will be rejected no matter how many times you type it. Stop
# here with a useful message instead of letting you loop on a password prompt.
# ---------------------------------------------------------------------------
echo "==> Checking that your account is an administrator..."
if ! dscl . -read /Groups/admin GroupMembership 2>/dev/null | grep -qw "$(id -un)"; then
  echo ""
  echo "STOP: your macOS account ('$(id -un)') is not an administrator."
  echo ""
  echo "Installing Homebrew and Docker Desktop requires admin rights, so this"
  echo "script cannot continue. You have three options:"
  echo ""
  echo "  1. Have an administrator of this Mac run the script for you."
  echo "  2. If this is a school- or work-managed Mac, ask your IT support"
  echo "     for administrator rights on your account."
  echo "  3. Skip the local install entirely and use GitHub Codespaces --"
  echo "     see Step 1 option 2 in 0-intro/0-0-setup.md. Nothing to install."
  echo ""
  exit 1
fi

# ---------------------------------------------------------------------------
# Heads up about the password prompt before it appears.
# ---------------------------------------------------------------------------
echo ""
echo "NOTE: You will be asked for your Mac login password below."
echo "      Nothing appears on screen as you type -- no dots, no asterisks."
echo "      That is normal. Type your password and press ENTER."
echo ""

echo "==> Checking for Homebrew..."
if ! command -v brew >/dev/null 2>&1; then
  echo "    Installing Homebrew..."
  # Read from the terminal, not from stdin. When this script is run as
  # `curl ... | bash`, stdin is the pipe rather than your keyboard, and the
  # Homebrew installer would switch to non-interactive mode and fail.
  if [ -r /dev/tty ]; then
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" < /dev/tty
  else
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  fi
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
# The cask used to be called `docker`. It was renamed to `docker-desktop`;
# `docker` on its own is now a formula that installs only the command-line
# tool, without the Docker Desktop app we need.
brew install --cask docker-desktop

echo "==> Installing Dev Containers extension..."
code --install-extension ms-vscode-remote.remote-containers

echo ""
echo "Done. NEXT STEPS:"
echo "  1. Launch Docker Desktop once:  open -a Docker"
echo "     (It asks for your password again to install its networking"
echo "      components. This is expected -- it needs admin rights.)"
echo "  2. Verify with: docker run hello-world"
