# package imports
from tkinter import *
import os
from playsound import playsound
# local imports
from subpp import process_exists
# local global variables
shyaboi = "shyaboi.mp3"
#tk root function
root = Tk()
# child process fork
# pid = os.fork()

import os, signal, subprocess
import sys
   
def click():
    # shyaboi
    playsound(shyaboi)
    # text from entry
    killCommand = e.get()
    # check if sometrhing is running
    running = process_exists(killCommand+'.exe')
    if killCommand == "google":
        print("there is many google things")
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
butt = Button(root, text="hot butt", padx=50, pady=50, command=click)
e = Entry(root, width=50 )
entryQ = Label(root, text="What process do you want to kill with python today?")

#putting on screen functions
butt.pack()
entryQ.pack()
e.pack()

#main loop
root.mainloop()