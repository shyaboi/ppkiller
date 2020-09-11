# package imports
from tkinter import *
from playsound import playsound
import os, signal, subprocess, sys
# local imports
from subpp import process_exists
from chromekiller import chromeKillSub
from adobekiller import adobeKillSub
# from nvidiakiller import nvidiaKillsub
from tunnelbearkiller import tunnelBearKillSub

# local global variables
shyaboi = "shyaboi.mp3"
#tk root function and atributes
root = Tk()
root.title("PPkiller")
root.iconbitmap("logo.ico")
# child process fork
# pid = os.fork()
def chromeKill():
    chromeKillMessage = Label(root, text=f"Some google things were unning......wait no.....I killed them")
    chromeKillSub()
    chromeKillMessage.pack()
    return

def adobeKill():
    adobeKillMessage = Label(root, text=f"Some Adobe things were unning......wait no.....I killed them")
    adobeKillSub()
    adobeKillMessage.pack()
    return

# def nvidiaKill():
#     nvidiaKillMessage = Label(root, text=f"Some Adobe things were unning......wait no.....I killed them")
#     nvidiaKillsub()
#     nvidiaKillMessage.pack()
#     return
def tunnelBearKill():
    tbKillMessage = Label(root, text=f"Some Adobe things were unning......wait no.....I killed them")
    tunnelBearKillSub()
    tbKillMessage.pack()
    return
def enterKey(event):
    print("You hit return.")
    click()
root.bind('<Return>', enterKey)


def click():
    # shyaboi

    playsound(shyaboi)
    # text from entry
    killCommand = e.get()
    # check if sometrhing is running
    running = process_exists(killCommand+'.exe')
    if killCommand == "google":
        chromeKill()
        return
    if killCommand == "adobe":
        adobeKill()
        return

    if running == True:
                
        thing = Label(root, text=f"{killCommand} running......wait no.....I killed it")
        os.system(f'taskkill /IM {killCommand}.exe /F')
        thing.pack()
        return
    else:
        thingNot = Label(root, text=f"can't find any related processes to {killCommand} running right now")
        thingNot.pack()
        return
#things to put on screen
aButt = Button(root, text="Adobe Killer", padx=5, pady=5, command=adobeKill)
gButt = Button(root, text="Google Killer", padx=5, pady=5, command=chromeKill)
# nButt = Button(root, text="Nvidia Killer", padx=5, pady=5, command=nvidiaKill)
tbButt = Button(root, text="TunnelBear Killer", padx=5, pady=5, command=tunnelBearKill)
butt = Button(root, text="Input Killer", padx=5, pady=5, command=click)
e = Entry(root, width=50 )
entryQ = Label(root, text="What program do you want to kill with python today?")

#putting on screen functions
aButt.pack()
# nButt.pack()
gButt.pack()
tbButt.pack()
entryQ.pack()
e.pack()
butt.pack()

#main loop
root.mainloop()