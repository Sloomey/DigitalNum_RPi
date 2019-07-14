import LEDarea as area
import RPi.GPIO as GPIO
import digits
import time

number = int(input('Number (0-9): '))
digits.digit(number)
time.sleep(5)
GPIO.cleanup()
