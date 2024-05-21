NOTE: This was tested with Raspberry Pi v1 B+, released in 2014.

# Set Up Hardware
https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/1

Install OS onto the microSD card.

Then, to the Raspberry Pi, connect microSD card, mouse, keyboard, HDMI display, ethernet (if Raspberry Pi 2 or below)

# Set Up Software

Install Raspberry Pi software/OS https://www.raspberrypi.com/documentation/computers/getting-started.html#configuration-on-first-boot

Then, in the terminal, run update command:
```sh
sudo apt update
```

# Connect Servo Motor
https://projects.raspberrypi.org/en/projects/grandpa-scarer/3. More references: https://www.digikey.com/en/maker/tutorials/2021/how-to-control-servo-motors-with-a-raspberry-pi

In this version:
- red wire: 1st row, 2nd column
- black wire (ground): 5th row, 1st column
- orange wire: 6th row, 1st column

# RealVNC (for Virtual Access to Raspberry Pi)
Connect via RealVNC: https://help.realvnc.com/hc/en-us/articles/360002249917-RealVNC-Connect-and-Raspberry-Pi#getting-connected-to-your-raspberry-pi-0-1

```sh
sudo apt-get install realvnc-vnc-viewer
```

Then, go to the Raspberry Pi icon in the top left toolbar -> Internet -> VNC Server.
Enter your credentials for the Raspberry Pi if prompted
After the VNC Server opens, on your other viewing computer, either enter the IP address of the Raspberry Pi listed, or if it is a personal device, log in to VNC Server using RealVNC account credentials to have the viewing computer automatically store and remember this computer.

(at this point, should be able to disconnect HDMI/external monitor and access the desktop of the Raspberry Pi virtually)

# Install git (for personal devices only)

Install and configure git
```sh
sudo apt install git
git config credential.helper store
```

Clone repo:
```sh
git clone https://github.com/lawrluor/catToyRPi.git
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python app.py
```

# For private/proprietary files:
Use scp or RealVNC file transfer functionality instead.

To transfer files to your Raspberry Pi, click the cycling arrows button and follow the instructions.

To transfer files from your Raspberry Pi, use RealVNC Viewer to open the RealVNC Server dialog remotely, select Menu > File transfer, and follow the instructions. Detailed steps are here.


# QUICKSTART (Personal Device Setup)
Use RealVNC file transfer to transfer the `quickstart.sh` file (available in the repo), or run:

```sh
git clone https://github.com/lawrluor/catToyRPi.git
bash catToyRpi/quickstart.sh
```

This will automatically create a `Repos` directory and `cd` into it.