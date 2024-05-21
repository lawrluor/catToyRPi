
# Set Up Hardware
https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/1
Connect mouse, keyboard, HDMI display, ethernet (if Raspberry Pi 2 or below)

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

# For private/proprietary files: SCP instead

