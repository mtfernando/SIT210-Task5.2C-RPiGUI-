from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

#Hardware
ledRed = LED(14)
ledGreen = LED(15)
ledBlue = LED(18)

#GUI Definitions
win = Tk()
win.title("LED Operator")
myFont = tkinter.font.Font(family = 'Arial', size = 12, weight = "bold")

#Event Functions
def ledOff():
    ledRed.off()
    ledGreen.off()
    ledBlue.off()

def close():
    RPi.GPIO.cleanup()
    win.destroy()

def onRed():
    ledOff()
    ledRed.on()

def onGreen():
    ledOff()
    ledGreen.on()

def onBlue():
    ledOff()
    ledBlue.on()

#Widgets
var = IntVar()
redRB = Radiobutton(win, text = "Red LED", variable=var,value=0,command = onRed, font = myFont)
redRB.grid(row=0, column=0)
greenRB = Radiobutton(win, text = "Green LED", variable=var,value=1,command = onGreen, font = myFont)
greenRB.grid(row=0, column=1)
blueRB = Radiobutton(win, text = "Blue LED", variable=var,value=2,command = onBlue, font = myFont)
blueRB.grid(row=0, column=2)

exitButton = Button(win, text = "Exit", font = myFont, command = close, bg = 'red')
exitButton.grid(row=1, column=1)
win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()
