from tkinter import * # noqa: F401, F403
import math # noqa: F401

import tkinter.messagebox  # noqa: F401


#========================Window Settings======================#

#Creating New Application Window
root =Tk()  # noqa: F405
#Setting Title of the Window
root.title("Scientific Calculator")
#Setting Background of the Window
root.configure(background="#008080")
#Preventing Resize of the Window
root.resizable(width=False, height=False)
#setting size of the window
root.geometry("485x535+0+0")

calc=Frame(root)  # noqa: F405
calc.grid()

class Calc():
    def __init__(self):
        self.total=0
        self.current=""
        self.input_value=True
        self.check_sum=False
        self.op=""
        self.result=False
        
    #handle the entry of numbers into the calculator.
    def numberEnter(self,num):
        """
        A function to process user input numbers and update the display accordingly.
        
        Parameters:
            num (int): The number input by the user.
        
        Returns:
            None
        """
        #indicating that there's no result calculated yet.
        self.result=False
        #retrieves the current value displayed in the calculator using the get() method of the Entry widget.
        firstnum=txtDisplay.get()
        #converts the entered number num to a string and stores it in secondnum.
        secondnum=str(num)
        #calculator is currently waiting for a new input
        #sets self.current to the entered number secondnum and sets self.input_value to False.
        if self.input_value:
            self.current = secondnum
            self.input_value=False
        else:
            #calculator already has a value (firstnum), it concatenates the entered number secondnum to the current value to form a new value (self.current)
            if secondnum=='.':
                if secondnum in firstnum:
                    return
            self.current=firstnum+secondnum
        #updates the display with the current value
        self.display(self.current)
    
    #Function to handle equals button press
    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum:
            self.valid_function()
        else:
            self.total=float(txtDisplay.get())
        
        
        
    def display(self,value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0,value)    

    def valid_function(self):
        if self.op=="add":
            self.total+=self.current
        if self.op=="sub":
            self.total-=self.current
        if self.op=="multi":
            self.total*=self.current
        if self.op=="divide":
            self.total/=self.current
        if self.op=="mod":
            self.total%=self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)
        
    def operation(self,op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False

    def Clear_Entry(self):
        self.result=False
        self.current="0"
        self.display(0)
        self.input_value=True
        
    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total=0
        
    def mathsPM(self):
        self.result=False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)
        
    def squared(self):
        self.result=False
        self.current=math.sqrt(float(txtDisplay.get()))
        self.display(self.current)
        
    def pi(self):
        self.result=False
        self.current=math.pi
        self.display(self.current)
        
        
    def tau(self):
        self.result=False
        self.current=math.tau
        self.display(self.current)
        
    def e(self):
        self.result=False
        self.current=math.e
        self.display(self.current)
    
    def sin(self):
        self.result=False
        self.current=math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def sinh(self):
        self.result=False
        self.current=math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def cos(self):
        self.result=False
        self.current=math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def cosh(self):
        self.result=False
        self.current=math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def tan(self):
        self.result=False
        self.current=math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    
    def tanh(self):
        self.result=False
        self.current=math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def asinh(self):
        self.result=False
        self.current=math.asinh(float(txtDisplay.get()))
        self.display(self.current)
        
    def acosh(self):
        self.result=False
        self.current=math.acosh(float(txtDisplay.get()))
        self.display(self.current)
        

    def log(self):
        self.result=False
        self.current=math.log(float(txtDisplay.get()))
        self.display(self.current)
        
    def log2(self):
        self.result=False
        self.current=math.log2(float(txtDisplay.get()))
        self.display(self.current)
        
    def log10(self):
        self.result=False
        self.current=math.log10(float(txtDisplay.get()))
        self.display(self.current)
    
    def log1p(self):
        self.result=False
        self.current=math.log1p(float(txtDisplay.get()))
        self.display(self.current)
        
    def expm1(self):
        self.result=False
        self.current=math.expm1(float(txtDisplay.get()))
        self.display(self.current)
    
    def lgamma(self):
        self.result=False
        self.current=math.lgamma(float(txtDisplay.get()))
        self.display(self.current)
    
    def degrees(self):
        self.result=False
        self.current=math.degrees(float(txtDisplay.get()))
        self.display(self.current)
        
    def Exp(self):
        self.result=False
        self.current=math.exp(float(txtDisplay.get()))
        self.display(self.current)
    
    

#========================Display Section||Input Field======================#
added_value=Calc()
txtDisplay= Entry(calc,font=('MS Sans Serif',20,'bold'),bg="#008080",fg="#fdffff",bd=10,width=31,justify=RIGHT)  # noqa: F405
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

#=======================Standard Buttons=======================================#

#=======================Number Buttons=======================================#
numberpad="789456123"
i = 0
btn=[]
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6,height=2,bg="#c3c3c3",fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4,text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=2,)
        btn[i]["command"]=lambda x=numberpad[i]:added_value.numberEnter(x)
        i+=1
#================================Clear Buttons========================================#
#Clear [C] Btn
btnClear=Button(calc,text=chr(67),width=6,height=2,bg="#818181", command=added_value.Clear_Entry,fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=1,column=0,pady=1)

#ClearAll [CE] Btn
btnAllClear=Button(calc,text=chr(67)+chr(69),width=6,height=2,bg="#818181",command=added_value.all_Clear_Entry ,fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=1,column=1,pady=1)


#######################Action Buttons############################
#Sqrt [√] Btn
btnSq=Button(calc,text='√',width=6,height=2,bg="#818181",command=added_value.squared,fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=1,column=2,pady=1)

#Add [+] Btn
btnAdd=Button(calc,text="+",width=6,height=2,bg="#818181",command=lambda:added_value.operation("add"),fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=1,column=3,pady=1)
#Sub [-] Btn
btnSub=Button(calc,text="-",width=6,height=2,bg="#818181",command=lambda:added_value.operation("sub"),fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=2,column=3,pady=1)
#Div [÷] Btn
btnDiv=Button(calc,text=chr(247),width=6,height=2,bg="#818181",command=lambda:added_value.operation("divide"),fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=3,column=3,pady=1)
#Mult [x] Btn
btnMult=Button(calc,text="x",width=6,height=2,bg="#818181",command=lambda:added_value.operation("multi"),fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=4,column=3,pady=1)

#========================Secondary Buttons==================================#
#Dot [.] Btn
btnDot=Button(calc,text=".",width=6,height=2,bg="#818181",fg="#000000",command=lambda:added_value.numberEnter("."),font=('MS Sans Serif',20,'bold'),bd=4).grid(row=5,column=0,pady=1)
#Zero [0] Btn
btnZero=Button(calc,text="0",width=6,height=2,bg="#c3c3c3",command=lambda:added_value.numberEnter(0),fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=5,column=1,pady=1)



#PlusMinus [+-] Btn
btnPM=Button(calc,text=chr(177),width=6,height=2,bg="#818181",command=added_value.mathsPM,fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=5,column=2,pady=1)
#Equals [=] Btn
btnEquals=Button(calc,text="=",width=6,height=2,bg="#818181",command=added_value.sum_of_total,fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=5,column=3,pady=1)



#=======================================Scientific Buttons============================#
#Pi [π] Btn
btnPi=Button(calc,text="π",width=6,height=2,bg="#818181",command=added_value.pi,fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=1,column=4,pady=1)

#Cos [cos] Btn
btnCos=Button(calc,text="cos",width=6,height=2,bg="#818181",command=added_value.cos,fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=1,column=5,pady=1)

#Tan [tan] Btn
btnTan=Button(calc,text="tan",width=6,height=2,bg="#818181",fg="#000000",command=added_value.tan,font=('MS Sans Serif',20,'bold'),bd=4).grid(row=1,column=6,pady=1)

#Sin [sin] Btn
btnSin=Button(calc,text="sin",width=6,height=2,bg="#818181",command=added_value.sin,fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=1,column=7,pady=1)

#==================================================================================#
#2Pi [2π] Btn
btnPi=Button(calc,text="2π",width=6,height=2,bg="#818181",command=added_value.tau,fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=2,column=4,pady=1)

#Cosh [cosh] Btn
btnCosh=Button(calc,text="cosh",width=6,height=2,bg="#c3c3c3",command=added_value.cosh,fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=2,column=5,pady=1)

#Tanh [tanh] Btn
btnTanh=Button(calc,text="tanh",width=6,height=2,bg="#c3c3c3",command=added_value.tanh,fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=2,column=6,pady=1)

#Sinh [sinh] Btn
btnSinh=Button(calc,text="sinh",width=6,height=2,bg="#c3c3c3",command=added_value.sinh,fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=2,column=7,pady=1)

#==================================================================================#
#log [log] Btn
btnlog=Button(calc,text="log",width=6,height=2,bg="#818181",command=added_value.log,fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=3,column=4,pady=1)

#Exp [exp] Btn
btnExp=Button(calc,text="Exp",width=6,height=2,bg="#c3c3c3",command=added_value.Exp,fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=3,column=5,pady=1)

#Mod [Mod] Btn
btnMod=Button(calc,text="Mod",width=6,height=2,bg="#c3c3c3",command=lambda:added_value.operation("mod"),fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=3,column=6,pady=1)

#BtnE [e] Btn
btnE=Button(calc,text="e",width=6,height=2,bg="#c3c3c3", command=added_value.e,fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=3,column=7,pady=1)

#==================================================================================#
#log2 [log2] Btn
btnlog2=Button(calc,text="log2",width=6,height=2,bg="#818181",command=added_value.log2,fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=4,column=4,pady=1)

#deg [deg] Btn
btndeg=Button(calc,text="deg",width=6,height=2,bg="#c3c3c3",command=added_value.degrees,fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=4,column=5,pady=1)

#acosh [acpsh] Btn
btnacosh=Button(calc,text="acosh",width=6,height=2,bg="#c3c3c3", command=added_value.acosh,fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=4,column=6,pady=1)

#asinh [asinh] Btn
btnasinh=Button(calc,text="asinh",width=6,height=2,bg="#c3c3c3", command=added_value.asinh,fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=4,column=7,pady=1)

#==================================================================================#
#log10 [log10] Btn
btnlog10=Button(calc,text="log10",width=6,height=2,bg="#818181",command=added_value.log10,fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=5,column=4,pady=1)

#log1p [log1p] Btn
btnCos=Button(calc,text="log1p",width=6,height=2,bg="#818181",command=added_value.log1p,fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=5,column=5,pady=1)

#Mod [Mod] Btn
btnaexpm1=Button(calc,text="expm1",width=6,height=2,bg="#818181",command=added_value.expm1,fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=5,column=6,pady=1)

#lGamma [lgamma] Btn
btnlgamma=Button(calc,text="lgamma",width=6,height=2,bg="#818181",command=added_value.lgamma,fg="#000000",font=('MS Sans Serif',20,'bold'),bd=4).grid(row=5,column=7,pady=1)

lblDisplay=Label(calc,text="Scientific Calculator",font=('MS Sans Serif',30,'bold'), bg="#008080",fg="#fdffff", width=20,justify=CENTER)

lblDisplay.grid(row=0,column=4,columnspan=4)
#========================Menu and Functions==============================#
#Functions
#EXIT FUNCTIONS

def iExit():
    iExit=tkinter.messagebox.askyesno("Scientific Calculator","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

##Filemenu Functions
def Scientific():
    root.resizable(width=False, height=False)
    #setting size of the window
    root.geometry("970x568+0+0")
    
def Standard():
    root.resizable(width=False, height=False)
    #setting size of the window
    root.geometry("480x535+0+0")

#Menu Section 1 ||| The menu parameter is used to specify the menu bar for the root window
menubar=Menu(calc)

filemenu=Menu(menubar,tearoff=0)
#setting the cascade drop down menu
menubar.add_cascade(label="File",menu=filemenu)
#options within the file menu
filemenu.add_command(label="Standard", command=Standard)
filemenu.add_command(label="Scientific", command=Scientific)
#adding a horizontal line
filemenu.add_separator()
#Exit  Option
filemenu.add_command(label="Exit",command=iExit)

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