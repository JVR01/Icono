#!/usr/bin/python
from Tkinter import *
from Tkinter import Label, Tk

import tkFont
import RPi.GPIO as GPIO
import os
import sys
import time
import pylibmc
import subprocess
from PIL import ImageTk, Image
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, GPIO.HIGH)


print ("Hello World");
print ("Gar Nichts");
#os.system("chromium-browser "192.168.178.34:8081" ")
#os.system("python codesource.py")
#os.system('sudo python interface.py')
#os.system('chromium-browser "192.168.178.34:8081"')


B=[0 for i in range(10)]

z=745000.
P=350000.
q=0.
n=0.
#shared = pylibmc.Client(["127.0.0.1"], binary=True,behaviors={"tcp_nodelay": True,"ketama": True})

win = Tk()

myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')
myFont1 = tkFont.Font(family = 'Helvetica', size = 20, weight = 'bold')
myFont2 = tkFont.Font(family = 'Helvetica', size = 30, weight = 'bold')


#img1=PhotoImage(file="/home/pi/Documents/orig2.png")
#img2=img1.subsample(4,4)
#img3=img2.zoom(3,3)
#lab1= Label(win, image=img1, width=1060, height=220).place(x=0,y=150)




                
def turnOff():
	print("LED button pressed")
	if GPIO.input(7) :
 		GPIO.output(7,GPIO.LOW)
                #time.sleep(5) 
		off["text"] = "Turned Off"
                print("debio prender")
	else:
		GPIO.output(7,GPIO.HIGH)
                #time.sleep(5) 
                off["text"] = "Turned On"
                print("debio apagar aqui")


        #print("la va a apagar aohora")
        #os.system("python codesource.py")
        #os.system('sudo python /home/pi/Documents/interface.py')
        #p=subprocess.Popen(["python","codesource.py"])
        #off["text"] = "apagada"
#http://192.168.2.126/
def startLive():
        print("abrir Chromium")
        os.system('chromium-browser "192.168.2.126"')
        #p=subprocess.Popen(["python","codesource.py"])
        ledazul["text"] = "Open now :)"


def exitProgram():
	print("Exit Button pressed")
	#p=subprocess.Popen(["python","codesource.py"])
	#os.terminate()
        #os.kill()
        #time.sleep(5) 
        GPIO.cleanup()
	win.quit()
	os.system('sudo sh /home/pi/Documents/close.sh')
        

win.title("Sensor values")
#win.geometry('1080x730')
win.geometry('600x200')

print('Ahora nuevo ciclo')

# Definicion Botones
exitButton  = Button(win, text = "Exit", font = myFont2,relief=GROOVE, command = exitProgram, height =2 , width = 6) 
exitButton.pack(side = BOTTOM)

off = Button(win, text = "TurnOff Printer", font = myFont1, command = turnOff, height = 1, width =11,fg= "blue" )
off.place(x=15,y=25)


start = Button(win, text = "LiveStreaming", font = myFont1, command = startLive, height = 1, width =11,fg= "blue" )
start.place(x=350,y=25)



mainloop()



