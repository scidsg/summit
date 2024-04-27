set -euo pipefail

# Welcome message and ASCII art
cat <<"EOF"
 ______     __  __     __    __     __    __     __     ______
/\  ___\   /\ \/\ \   /\ "-./  \   /\ "-./  \   /\ \   /\__  _\
\ \___  \  \ \ \_\ \  \ \ \-./\ \  \ \ \-./\ \  \ \ \  \/_/\ \/
 \/\_____\  \ \_____\  \ \_\ \ \_\  \ \_\ \ \_\  \ \_\    \ \_\
  \/_____/   \/_____/   \/_/  \/_/   \/_/  \/_/   \/_/     \/_/

🏔️ Summit it an OCR application to extract and summarize text from a set of images.

A free and open-source tool by Science & Design, Inc. - https://scidsg.org
EOF
sleep 3

# Function to check and install Homebrew
install_homebrew() {
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    if [[ $? -ne 0 ]]; then
        echo "Failed to install Homebrew."
        exit 1
    fi
}

# Check for Homebrew and install if not present
if ! command -v brew &>/dev/null; then
    echo "Homebrew not found. Installing Homebrew..."
    install_homebrew
fi

# Install Python3 if not present
if ! command -v python3 &>/dev/null; then
    echo "Python3 is not installed. Installing Python3..."
    brew install python
fi

# Install pip if not present
if ! command -v pip3 &>/dev/null; then
    echo "pip3 is not installed. Installing pip3..."
    brew install pip3
fi

# Create a virtual environment
echo "🧑‍💻 Creating a virtual environment..."
python3 -m venv venv

# Activate the virtual environment
echo "🎬 Activating the virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📋 Installing required packages from requirements.txt..."
pip3 install -r requirements.txt

# Run the Python script
echo "🚀 Summiting..."
python3 summit.py

# Deactivate the virtual environment
deactivate

echo "🏁 Script completed successfully."
