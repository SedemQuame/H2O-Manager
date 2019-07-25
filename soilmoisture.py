import RPi.GPIO as GPIO; import datetime; import time; import random
from db_utils import create_entry, db_connect

def read_soil_moisture():
    rPin = 7; yPin = 11; gPin = 23  
    pollTime = 1; prevStatus = -1; timeFormat = "%Y-%m-%d"

    #Setup GPIO
    GPIO.setwarnings(False); GPIO.setmode(GPIO.BOARD)
    
    #Setup various pins
    GPIO.setup([gPin,yPin,rPin], GPIO.IN, GPIO.PUD_DOWN)
    
    #Get status of input pins
    red = GPIO.input(rPin); yellow = GPIO.input(yPin); green = GPIO.input(gPin)
    status = (red * 4) + (yellow * 2) + (green * 1)
    
    if status != prevStatus:
        levelIndicator = ((("25","50")[green == 1],"75")[yellow == 1],"100")[red == 1]
        prevStatus = status

        if levelIndicator == str(25):
            levelIndicator = random.randint(0, 25)
        elif levelIndicator == str(50):
            levelIndicator = random.randint(25, 50)
        elif levelIndicator == str(75):
            levelIndicator = random.randint(50, 75)
        else:
            levelIndicator = random.randint(75, 100)

        #get time at which sensor's data was taken.
        currentTime = str(datetime.datetime.now().strftime(timeFormat))
        
        #store sensor data into database.
        create_entry(db_connect(), currentTime, levelIndicator)
    time.sleep(pollTime)
    
    #when user interrupts, cleanup and exit
    GPIO.cleanup()

    return [currentTime, levelIndicator]