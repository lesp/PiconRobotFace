#!/usr/bin/python
import piconzero as pz, time, hcsr04
pz.init()
hcsr04.init()
pz.setOutputConfig(5, 3)    # set output 5 to WS2812
speed = 50
pz.setBrightness(16)

def smile():
	mouth = [0,1,2,3,4,5]
	#Eyes
	pz.setPixel(15,0,255,0)
	pz.setPixel(16,0,255,0)
	for i in mouth:
		pz.setPixel(i,255,0,0)


def oops():
	mouth = [0,1,2,3,4,5,6,7,8,9]
	#Eyes
	pz.setPixel(15,255,0,0)
	pz.setPixel(16,255,0,0)
	for i in mouth:
		pz.setPixel(i,255,0,0)

def left():
	mouth = [4,5,9]
	#Eyes
	pz.setPixel(15,255,255,0)
	pz.setPixel(16,255,255,0)
	for i in mouth:
		pz.setPixel(i,255,255,0)	

def right():
	mouth = [0,1,6]
	#Eyes
	pz.setPixel(15,255,0,255)
	pz.setPixel(16,255,0,255)
	for i in mouth:
		pz.setPixel(i,255,0,255)	


def angry():
	mouth = [1,4,6,9,11,12]
	#Eyes
	pz.setPixel(15,255,0,0)
	pz.setPixel(16,255,0,0)
	for i in mouth:
		pz.setPixel(i,255,0,0)

try:
	while True:
		distance = int(hcsr04.getDistance())
		print(distance)
		pz.setAllPixels(0,0,0)
		#time.sleep(1)
		if distance < 10 and distance > 5:
			#pz.setAllPixels(0,0,0)
			oops()
			pz.reverse(speed)
			time.sleep(1)
			pz.spinRight(speed)
			time.sleep(1.2)
			#pz.stop()
		elif distance > 10 and distance < 20:
			#pz.setAllPixels(0,0,0)
			left()
			pz.spinLeft(speed)
			time.sleep(0.6)
		else:
			#pz.setAllPixels(0,0,0)
			smile()
			pz.forward(speed)
			time.sleep(0.2)

except KeyboardInterrupt:
	print("STOPPED")
finally:
	hcsr04.cleanup()
	pz.cleanup()
