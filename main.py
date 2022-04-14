from datetime import datetime
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import os
import time

def button_callback(message):
    print("ring off")
    os.system('pkill mpg321')
    time.sleep(500)

def ring_off():
    GPIO.setwarnings(False) 
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
    GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) 
    message = input("Press enter to quit\n\n") 
    GPIO.cleanup() 

def wake_up():
    print("wake up")
    hour = time.strftime('%H:%M:%S', time.localtime())
    wakeHour = "05:55:10"
    print(hour)
    if hour == wakeHour:
        os.system('mpg321 ring.mp3 &')
        ring_off()
        


while True:
    wake_up()
    time.sleep(1)
