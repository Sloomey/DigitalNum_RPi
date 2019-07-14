import RPi.GPIO as GPIO

""" This file contains the locations for every LED (in twos)
    so it can easily be called. This helps clear up confusion. """

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)

MIDDLE_TOP = [GPIO.output(12, True), GPIO.output(7, True)]
LEFT_TOP = [GPIO.output(11, True), GPIO.output(13, True)]
RIGHT_TOP = [GPIO.output(18, True), GPIO.output(16, True)]
MIDLE_MIDDLE = [GPIO.output(15, True), GPIO.output(22, True)]
LEFT_BOTTOM = [GPIO.output(21, True), GPIO.output(29, True)]
RIGHT_BOTTOM = [GPIO.output(24, True), GPIO.output(26, True)]
MIDDLE_BOTTOM = [GPIO.output(31, True), GPIO.output(32, True)]
