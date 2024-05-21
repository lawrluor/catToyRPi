#!/bin/bash

# Update the system
echo "Updating system..."
sudo apt update && sudo apt upgrade -y

# Install RealVNC
echo "Installing RealVNC..."
sudo apt-get install -y realvnc-vnc-viewer

# Install Python
sudo apt-get install python3-venv python3-setuptools python3-pip python3-wheel

# Install virtualenv
echo "Installing virtualenv..."
sudo apt install -y python3-virtualenv || true

# Install Git
echo "Installing Git..."
sudo apt install -y git
git config --global credential.helper store

# Clone the repository and set up the environment
echo "Cloning repository and setting up the environment..."
git clone https://github.com/lawrluor/catToyRPi.git || true
cd catToyRPi || { echo "Failed to enter the repository directory"; exit 1; }

# Create virtual environment using virtualenv
echo "Creating virtual environment..."
python3 -m virtualenv venv || true

# Activate the virtual environment and install dependencies
echo "Activating virtual environment and installing dependencies..."
source venv/bin/activate || true
pip install -r requirements.txt || true

# Create the .desktop file content
DESKTOP_FILE_CONTENT="[Desktop Entry]
Name=Run Setup Script
Comment=This will run the setup script
Exec=catToyRPi/run.sh
Icon=utilities-terminal
Terminal=true
Type=Application"

# Create the .desktop file on the Desktop
echo "$DESKTOP_FILE_CONTENT" > Desktop/runServer.desktop

# Make the .desktop file executable
chmod +x Desktop/runServer.desktop

echo "Desktop shortcut created successfully."
echo "To run the server in the future: bash run.sh"
echo "Or, click the desktop shortcut that was created"

echo "Setup completed. You can now use your Raspberry Pi as a cat toy controller."

# Run the application
echo "Starting the application..."
cd catToyRPi
source venv/bin/activate
python app.py
