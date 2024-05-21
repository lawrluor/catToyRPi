#!/bin/bash

# Script to set up Raspberry Pi for a cat toy project

echo "Starting Raspberry Pi setup..."

# Update the system
echo "Updating system..."
sudo apt update && sudo apt upgrade -y

# Install RealVNC
echo "Installing RealVNC..."
sudo apt-get install -y realvnc-vnc-viewer

# Configure RealVNC
echo "Configuring RealVNC..."
# RealVNC should be configured manually as per instructions on the Raspberry Pi documentation
echo "Please go to the Raspberry Pi icon in the top left toolbar -> Internet -> VNC Server."
echo "Enter your credentials for the Raspberry Pi if prompted."
echo "After the VNC Server opens, on your other viewing computer, either enter the IP address of the Raspberry Pi listed,"
echo "or if it is a personal device, log in to VNC Server using RealVNC account credentials to have the viewing computer automatically store and remember this computer."

# Install Git
echo "Installing Git..."
sudo apt install -y git
git config --global credential.helper store

# Clone the repository and set up the environment
mkdir Repos
cd Repos
echo "Cloning repository and setting up the environment..."
git clone https://github.com/lawrluor/catToyRPi.git
sleep 3
cd catToyRPi || { echo "Failed to enter the repository directory"; exit 1; }
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

echo "Setup completed. You can now use your Raspberry Pi as a cat toy controller."

# Instructions for servo motor connection
echo "To connect the servo motor:"
echo "- Red wire: 1st row, 2nd column"
echo "- Black wire (ground): 5th row, 1st column"
echo "- Orange wire: 6th row, 1st column"

# Instructions for file transfer
echo "To transfer private/proprietary files, use scp or RealVNC file transfer functionality."
echo "For RealVNC file transfer, click the cycling arrows button and follow the instructions."
echo "To transfer files from your Raspberry Pi, use RealVNC Viewer to open the RealVNC Server dialog remotely, select Menu > File transfer, and follow the instructions."
echo "Detailed steps are available on the RealVNC documentation."

echo "Setup script finished."

# Run the application
echo "Starting the application..."
echo "Use python app.py to start the server in the future."
python app.py
