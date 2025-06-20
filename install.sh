#!/bin/bash
# BookBot Installation Script
# Creates system-wide commands for bookbot and pdf-get
#
# LEARNING NOTE: This installation script demonstrates:
# 1. Automated software installation patterns
# 2. Virtual environment creation and management
# 3. System PATH modification
# 4. Symbolic link creation for command availability
# 5. User feedback and progress indication
# 6. Conditional execution and error handling
#
# This script automates the entire setup process, making it easy for
# users to get started with BookBot without manual configuration.

echo "🔧 Installing BookBot shell commands..."

# BEGINNER CONCEPT: Getting the script's directory
# This finds where the installation script is located
BOOKBOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# BEGINNER CONCEPT: Conditional directory creation
# ! means "not" - so this checks "if directory does NOT exist"
if [ ! -d "$BOOKBOT_DIR/.venv" ]; then
    echo "🐍 Creating virtual environment..."
    # BEGINNER CONCEPT: Python virtual environment creation
    # Virtual environments isolate dependencies to avoid conflicts
    python3 -m venv "$BOOKBOT_DIR/.venv"
fi

# BEGINNER CONCEPT: Dependency installation
echo "📦 Installing dependencies..."
# Activate the virtual environment we just created
source "$BOOKBOT_DIR/.venv/bin/activate"
# Install packages listed in requirements.txt (pdfplumber, nltk)
pip install -r "$BOOKBOT_DIR/requirements.txt"

# BEGINNER CONCEPT: User directory creation
# ~/.local/bin is the standard location for user-installed commands
mkdir -p ~/.local/bin

# BEGINNER CONCEPT: Symbolic link creation
# ln -sf creates symbolic links (shortcuts) that make our commands globally available
# -s means "symbolic link", -f means "force (overwrite if exists)"
ln -sf "$BOOKBOT_DIR/bookbot" ~/.local/bin/bookbot
ln -sf "$BOOKBOT_DIR/pdf-get" ~/.local/bin/pdf-get

# BEGINNER CONCEPT: PATH environment variable management
# Check if ~/.local/bin is already in the user's PATH
# The PATH variable tells the shell where to look for commands
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    echo "📝 Adding ~/.local/bin to PATH..."
    # BEGINNER CONCEPT: Shell configuration modification
    # Add the export command to ~/.bashrc so it persists across sessions
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
    echo "⚠️  Please run: source ~/.bashrc or restart your terminal"
fi

# BEGINNER CONCEPT: User feedback and success messaging
echo "✅ Installation complete!"
echo ""
echo "📚 You can now use:"
echo "   bookbot <file>              # Analyze any book/PDF"
echo "   pdf-get --list              # List PDFs on Windows Desktop"  
echo "   pdf-get --analyze <name>    # Copy and analyze PDF"
echo ""
echo "🔄 If this is your first install, run: source ~/.bashrc"