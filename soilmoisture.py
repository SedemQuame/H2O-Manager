#!/usr/bin/python3
#Author - Nagendra Thangella
#Disclaimer - No warranties or guaranties. Use this at your own risk.
#Prior to running this program, install Rpi-GPIO using command "sudo apt-get install rpi.gpio"
import RPi.GPIO as GPIO; import datetime; import time

#Define Static variables, file names and time format
#pollTime below is set to 1 second
#Besides the below pins, I use pin 1 for 3.3V
rPin = 7; yPin = 11; gPin = 23  
pollTime = 1; prevStatus = -1; timeFormat = "%I:%M:%S %p"

#Setup GPIO
GPIO.setwarnings(False); GPIO.setmode(GPIO.BOARD)
#Setup various pins
GPIO.setup([gPin,yPin,rPin], GPIO.IN, GPIO.PUD_DOWN)

#Run infintely until user interrupts
try:
    while 1:
        #Get status of input pins
        red = GPIO.input(rPin); yellow = GPIO.input(yPin); green = GPIO.input(gPin)
        status = (red * 4) + (yellow * 2) + (green * 1)
        #If status changes, set level indicator as red, yellow, green or blue in that order
        # blue (no pin) is on when all red, yellow and green are off. 
        if status != prevStatus:
            levelIndicator = ((("0-25%","25-50%")[green == 1],"50-75%")[yellow == 1],"75-100%")[red == 1]
            prevStatus = status
            currentTime = datetime.datetime.now().strftime(timeFormat)
            print ("Status of water level at %s is %s \r\n" % (currentTime, levelIndicator))
        time.sleep(pollTime)
#when user interrupts, cleanup and exit
except KeyboardInterrupt:
    GPIO.cleanup()
print("Exiting")