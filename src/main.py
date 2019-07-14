import LEDarea as area
import RPi.GPIO as GPIO
import digits
import time

""" This is the main file (showed by its name, main.py). This is the file that
    makes everything come together and work. It has two inputs, the number
    and the amount of time to show that numer. """

number = int(input('Number (0-9): '))
duration = int(input('Show for how long (in seconds): '))
digits.digit(number)
time.sleep(duration)
GPIO.cleanup()
