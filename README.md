
# Robot.py
## A robot with a face!
Les Pounder July 4th 2016
This is a Creative Commons CC-BY-SA 2.0 Project, so go ahead and make it cool!

---
Hi this project is to create a simple robot using the following parts

- A Raspberry Pi Zero
- The latest version of Raspbian, downloaded from the [Raspberry Pi Website](https://www.raspberrypi.org/downloads/)
- A Picon Zero board from 4tronix
- A McRoboFace board from 4tronix
- An HC-SR04 Ultraonic Sensor
- 2 x Micro gear metal motors
- A Chassis of your choosing.
- A power supply with enough power for the Pi, Motors and McRoboFace
- A handful of jumper wires (Female to Female)
- An Internet connection to complete the software installation

## Hardware Installtion
Attach the Picon Zero to all 40 of the GPIO pins and ensure that the board sits neatly atop of the Raspberry Pi.

## Software Installation 

The Picon Zero is an I2C device, so you must ensure that your Raspberry Pi is setup to use I2C and smbus correctly:

In a Terminal type the following
```
sudo apt update && sudo apt install python-smbus python3-smbus python-dev python3-dev
```

Next we need to edit the config.txt file, in the Terminal type
```
sudo nano /boot/config.txt
```
Now add the following 2 lines to the *end* of the file:
```
dtparam=i2c1=on
dtparam=i2c_arm=on
```

Press <ctrl-x> and accept the default prompts to save the file
Now in the terminal we need to reboot, type the following.
```
sudo reboot
```
With your Pi rebooted, in a Terminal type the following to check that your board is setup correctly.

i2cdetect -y 1
If all is well, you will see the Picon Zero showing up as address 22 

##Python Example Installation

The Picon Zero is provided with a python library which allows very simple access to all the features in an intuitive and consistent manner. A separate small library handles the ultrasonic which is on a GPIO pin and not part of the onboard micro-controller.


You can also download directly both libraries and example files by typing the following into the terminal window. Open LXTerminal and type:

```
wget http://4tronix.co.uk/piconz.sh -O piconz.sh
bash piconz.sh
```

That will create a piconzero folder in your home folder, with the libraries and example files:

- piconzero.py  library module for Picon Zero
- hcsr04.py  library module for ultrasonic sensor
- version.py prints the board type and firmware version
- motorTest.py  tests the motor functions using the arrow keys on the keyboard
- ioTest.py  demonstrates the use of an analog input (potentiometer on Input 0) used to control various forms of output
- sonarTest.py  demonstrates taking distance readings if you have an HC-SR04 ultrasonic sensor attached
- tempTest.py demonstrates reading the temperature from an attached DS18B20 sensor
- 10linesTest.py  shows a simple 10 (or 11) line program that reads an analog input and outputs to various devices (same as ioTest.py but without some bells and whistles). Simply to show how easy it can be to use the Picon Zero
- pixelTest.py  flashes all the attached neopixels from White to Off and back again
- servoTest.py uses the arrow keys to move 2 servos (pan and tilt) and the G, H keys to move a third servo (grabber claw)

Use the motorTest.py and sonarTest.py files to test that your motors and sensor are working.

Full project instructions as available from [bigl.es](http://bigl.es)