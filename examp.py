from tkinter import *
#from Tkinter import Label, Tk
#import commands
#import tkFont
import RPi.GPIO as GPIO
import os
import sys
import time
import pylibmc
import subprocess
#from PIL import ImageTk, Image
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)
print(subprocess.getoutput('hostname -I'))
print("nichts")
#print(subprocess.getoutput('ifconfig wlan0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1'))
def clicked():
 
    lbl.configure(text="Button was clicked !!")
    os.system('chromium-browser "192.168.2.126"')
btn = Button(window, text="Click Me", command=clicked)
 
btn.grid(column=1, row=0)
 
window.mainloop()