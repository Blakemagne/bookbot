#!/bin/bash
# BookBot Installation Script
# Creates system-wide commands for bookbot and pdf-get

echo "🔧 Installing BookBot shell commands..."

# Get current directory
BOOKBOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Create virtual environment if it doesn't exist
if [ ! -d "$BOOKBOT_DIR/.venv" ]; then
    echo "🐍 Creating virtual environment..."
    python3 -m venv "$BOOKBOT_DIR/.venv"
fi

# Install dependencies
echo "📦 Installing dependencies..."
source "$BOOKBOT_DIR/.venv/bin/activate"
pip install -r "$BOOKBOT_DIR/requirements.txt"

# Create ~/.local/bin if it doesn't exist
mkdir -p ~/.local/bin

# Create symlinks to make commands available globally
ln -sf "$BOOKBOT_DIR/bookbot" ~/.local/bin/bookbot
ln -sf "$BOOKBOT_DIR/pdf-get" ~/.local/bin/pdf-get

# Check if ~/.local/bin is in PATH
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    echo "📝 Adding ~/.local/bin to PATH..."
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
    echo "⚠️  Please run: source ~/.bashrc or restart your terminal"
fi

echo "✅ Installation complete!"
echo ""
echo "📚 You can now use:"
echo "   bookbot <file>              # Analyze any book/PDF"
echo "   pdf-get --list              # List PDFs on Windows Desktop"
echo "   pdf-get --analyze <name>    # Copy and analyze PDF"
echo ""
echo "🔄 If this is your first install, run: source ~/.bashrc"