import Tkinter as tk
from Tkinter import *
from gopigo import *
import RPi.GPIO as GPIO
import time

servo_pos=90

GPIO.setmode(GPIO.BCM) 

GPIO.setwarnings(False) 

GPIO.setup(17,GPIO.OUT)

def keydowni(i):
    GPIO.output(17,GPIO.LOW)

def keyupi(i):
    GPIO.output(17,GPIO.HIGH)

def keydownq(q):
    servo_pos=servo_pos+2

def keydowne(e):
    servo_pos=servo_pos-2


def key_input(event):
    key_press = event.keysym.lower()
    print(key_press)

    if key_press == 'w':
        fwd()
    elif key_press == 's':
        bwd()
    elif key_press == 'a':
        left_rot()
    elif key_press == 'd':
        right_rot() 
    elif key_press == 'space':
        stop()





root = Tk()
frame = Frame(root, width=100, height=100)
frame.bind('<Key>', key_input)
frame.bind("<KeyPress-i>", keydowni)
frame.bind("<KeyRelease-i>", keyupi)
frame.bind("<KeyPress-q>", keydownq)
frame.bind("<KeyPress-e>", keydowne)
frame.pack()
frame.focus_set()
root.mainloop()
GPIO.cleanup()

os.system('xset r off')


