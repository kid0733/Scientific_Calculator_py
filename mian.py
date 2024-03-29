from tkinter import * # noqa: F401, F403
import math # noqa: F401

import tkinter.messagebox  # noqa: F401


#Window Settings

#Creating New Application Window
root =Tk()  # noqa: F405
#Setting Title of the Window
root.title("Scientific Calculator")
#Setting Background of the Window
root.configure(background="#008080")
#Preventing Resize of the Window
root.resizable(width=False, height=False)
#setting size of the window
root.geometry("480x568+0+0")

calc=Frame(root)  # noqa: F405
calc.grid()

#Menu Section 1 ||| The menu parameter is used to specify the menu bar for the root window
menubar=Menu(calc)

filemenu=Menu(menubar,tearoff=0)
#setting the cascade drop down menu
menubar.add_cascade(label="File",menu=filemenu)
#options within the file menu
filemenu.add_command(label="Standard")
filemenu.add_command(label="Scientific")
#adding a horizontal line
filemenu.add_separator()
#Exit  Option
filemenu.add_command(label="Exit",command=exit)

#Menu Section 2
editmenu=Menu(menubar,tearoff=0)
#setting the cascade drop down menu
menubar.add_cascade(label="Edit",menu=editmenu)
#options within the edit menu
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")



#Menu Section 3
helpmenu=Menu(menubar,tearoff=0)
#setting the cascade drop down menu
menubar.add_cascade(label="Help",menu=helpmenu)
#options within the edit menu
helpmenu.add_command(label="View Help")


#Running the Code
# Displaying the Menu|||the menu parameter is used to specify the menu bar for the root window
root.config(menu=menubar)
#Display GUI |||| starts the Tkinter event loop, which listens for events 
root.mainloop() 