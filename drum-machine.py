# File Name: drum-machine.py
# Author: Brian Thompson
# Date: April 2, 2016
# Python Version: 3
# Purpose: A six button drum machine with three drums mapped to 
#	GPIO 17, 27, 22 and three symbols mapped to GPIO 14, 15, 18

#IMPORTS
import pygame.mixer
from pygame.mixer import Sound
import RPi.GPIO as GPIO
import time

#DEFINITIONS
BUTTON1=17
BUTTON2=27
BUTTON3=22
BUTTON4=14
BUTTON5=15
BUTTON6=18


#PIN SETUP
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(BUTTON1 ,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON2 ,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON3 ,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON4 ,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON5 ,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON6 ,GPIO.IN, pull_up_down=GPIO.PUD_UP)

#INITIALIZE PYGAME TO PLAY SOUND
pygame.mixer.pre_init(44100,-16,6,1024)
pygame.mixer.init()
sound1 = Sound("samples/drum_heavy_kick.wav")
sound2 = Sound("samples/drum_snare_hard.wav")
sound3 = Sound("samples/drum_tom_hi_hard.wav")
sound4 = Sound("samples/drum_cymbal_closed.wav")
sound5 = Sound("samples/drum_cymbal_soft.wav")
sound6 = Sound("samples/drum_splash_hard.wav")

#DEFINE CALLBACKS
def my_callback_one(BUTTON1):
        sound1.play()

def my_callback_two(BUTTON2):
        sound2.play()

def my_callback_three(BUTTON3):
        sound3.play()
        
def my_callback_four(BUTTON4):
        sound4.play()

def my_callback_five(BUTTON5):
        sound5.play()

def my_callback_six(BUTTON6):
        sound6.play()

#EVENTS
GPIO.add_event_detect(BUTTON1, GPIO.FALLING, callback=my_callback_one, bouncetime=200)
GPIO.add_event_detect(BUTTON2, GPIO.FALLING, callback=my_callback_two, bouncetime=200)
GPIO.add_event_detect(BUTTON3, GPIO.FALLING, callback=my_callback_three, bouncetime=200)
GPIO.add_event_detect(BUTTON4, GPIO.FALLING, callback=my_callback_four, bouncetime=200)
GPIO.add_event_detect(BUTTON5, GPIO.FALLING, callback=my_callback_five, bouncetime=200)
GPIO.add_event_detect(BUTTON6, GPIO.FALLING, callback=my_callback_six, bouncetime=200)

#MAIN
try:
        while True:
                print("Welcome to my demo!")

#CLEANUP
except KeyboardInterrupt:
    GPIO.cleanup()
