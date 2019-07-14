import LEDarea as area
import RPi.GPIO as GPIO
import digits
import time

number = int(input('Number (0-9): '))
duration = int(input('Show for how long (in seconds): '))
digits.digit(number)
time.sleep(duration)
GPIO.cleanup()
