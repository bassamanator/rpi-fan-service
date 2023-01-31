#!/usr/bin/env python

import os
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
st = 5 # How often to poll temp
pin = 24 # The pin ID, edit here to change it
ledPin = 21 # Pin to turn on LED
maxTMP = 65 # The high temperature in Celsius which will trigger the fan on
minTMP = 45 # The low temperature in Celsius which will trigger fan off

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
GPIO.setup(ledPin, GPIO.OUT) # set ledPin as an output
GPIO.setwarnings(False)
    
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
    #print(temp)
    return temp

def getTEMP():
    CPU_temp = float(getCPUtemperature())
    if CPU_temp>maxTMP:
        GPIO.output(pin, True)
        GPIO.output(ledPin, GPIO.HIGH)
    elif CPU_temp<minTMP:
        GPIO.output(pin, False)
        GPIO.output(ledPin, GPIO.LOW)
    return()

try:
    while True:
        getTEMP()
        time.sleep(st) # Read the temperature every 5 sec, increase or decrease this limit if you want
except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt 
    GPIO.cleanup() # resets all GPIO ports used by this program
