import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 5 to be an input pin and set initial value to be pulled low (off)

waiting = False
pressed = False
long_pressed = False
pressed_time = time.time()
start_time = time.time()
while True:
    if waiting:
        if(time.time() - pressed_time)*1000 >= 20:
            if GPIO.input(5) == GPIO.HIGH:
                pressed = True
        if time.time() - pressed_time > 1:
            waiting = False
            if GPIO.input(5) == GPIO.HIGH:
                long_pressed = True
    else:
        if pressed:
            if long_pressed:
                print("Button is long pressed")
            else:
                print("Button is pressed")
            pressed = False
            long_pressed = False

        elif GPIO.input(5) == GPIO.HIGH:
            pressed_time = time.time()
            waiting = True
        