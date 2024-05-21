#!/bin/bash

# Update the system
echo "Updating system..."
sudo apt update && sudo apt upgrade -y

# Install RealVNC
echo "Installing RealVNC..."
sudo apt-get install -y realvnc-vnc-viewer

# Install Git
echo "Installing Git..."
sudo apt install -y git
git config --global credential.helper store

# Clone the repository and set up the environment
echo "Cloning repository and setting up the environment..."
git clone https://github.com/lawrluor/catToyRPi.git || true
sleep 3s
cd catToyRPi || { echo "Failed to enter the repository directory"; exit 1; }
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create the .desktop file content
DESKTOP_FILE_CONTENT="[Desktop Entry]
Name=Run Setup Script
Comment=This will run the setup script
Exec=/home/pi/Repos/catToyRPi/run.sh
Icon=utilities-terminal
Terminal=true
Type=Application"

# Create the .desktop file on the Desktop
echo "$DESKTOP_FILE_CONTENT" > /home/pi/Desktop/runServer.desktop

# Make the .desktop file executable
chmod +x /home/pi/Desktop/runServer.desktop

echo "Desktop shortcut created successfully."
echo "To run the server in the future: bash run.sh"
echo "Or, click the desktop shortcut that was created"

echo "Setup completed. You can now use your Raspberry Pi as a cat toy controller."

# Run the application
echo "Starting the application..."
cd catToyRPi
source venv/bin/activate
python app.py
