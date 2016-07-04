
# Robot.py
## A robot with a face!
Les Pounder July 4th 2016
This is a Creative Commons CC-BY-SA 2.0 Project, so go ahead and make it cool!

---
Hi this project is to create a simple robot using the following parts

A Raspberry Pi Zero
The latest version of Raspbian, downloaded from the [Raspberry Pi Website](https://www.raspberrypi.org/downloads/)
A Picon Zero board from 4tronix
A McRoboFace board from 4tronix
2 x Micro gear metal motors
A Chassis of your choosing.
A power supply with enough power for the Pi, Motors and McRoboFace
An Internet connection to complete the software installation

## Software Installation 

The Picon Zero is an I2C device, so you must ensure that your Raspberry Pi is setup to use I2C and smbus correctly:

In a Terminal type the following
'''
sudo apt update && sudo apt install python-smbus python3-smbus python-dev python3-dev
'''
sudo nano /boot/config.txt
and add the following 2 lines to the end of the file:
dtparam=i2c1=on
dtparam=i2c_arm=on
Press <ctrl-x> and accept the default prompts to save the file
sudo reboot
Plug the Picon Zero onto the Pi and run

i2cdetect -y 1
If all is well, you will see the Picon Zero showing up as address 22 as below:


The code for this 

