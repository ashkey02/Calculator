#Ash Garcia
#01-25-2022
#The Reckoner - Calculator

#import libraries
from tkinter import *

#the main GUI
class MainGUI(Frame):
    #the constructer
    def __init__(self, parent):
        #sets up big white screen at the top
        Frame.__init__(self, parent, bg="white")
        #parent.attributes("-fullscreen", True)
        self.setupGUI()

    #sets up the GUI
    def setupGUI(self):
        #the calculator uses the TexGyreAdvento font
        self.display = Label(self, text="", anchor=E, bg="white", fg = "black", height=2, font=("Times", 50))
        self.display.grid(row=0, column=0, columnspan=4, sticky=E+W+N+S)
        #0-5
        for row in range(6):
            Grid.rowconfigure(self, row, weight=1)
        #0-3
        for col in range(4):
            Grid.columnconfigure(self, col, weight=1)

        #first row
        #fetch and store image
        img = PhotoImage(file="images/lpr.gif")
        #create the button
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("("))
        #set the buttons image
        button.image = img
        #adjust button to place it where it belongs
        button.grid(row=1, column=0, sticky=N+S+E+W)
        img = PhotoImage(file="images/rpr.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process(")"))
        button.image = img
        button.grid(row=1, column=1, sticky=N+S+E+W)
 
        #AC
        img = PhotoImage(file="images/clr.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("AC"))
        button.image = img
        button.grid(row=1,column=2, sticky=N+S+E+W)
 
        #**
        img = PhotoImage(file="images/pow.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("**"))
        button.image =img
        button.grid(row=1, column=3, sticky=N+S+E+W)
 
        #second row
        #7
        img = PhotoImage(file="images/7.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("7"))
        button.img = img
        button.grid(row=2, column=0, sticky=N+S+E+W)
 
        #8
        img = PhotoImage(file="images/8.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("8"))
        button.img = img
        button.grid(row=2, column=1, sticky=N+S+E+W)
 
        #9
        img = PhotoImage(file="images/9.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("9"))
        button.img = img
        button.grid(row=2, column=2, sticky=N+S+E+W)
 
        #/
        img = PhotoImage(file="images/div.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("/"))
        button.img = img
        button.grid(row=2, column=3, sticky=N+S+E+W)
 
        #third row
        #4
        img = PhotoImage(file="images/4.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("4"))
        button.img = img
        button.grid(row=3, column=0, sticky=N+S+E+W)
 
        #5
        img = PhotoImage(file="images/5.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("5"))
        button.img = img
        button.grid(row=3, column=1, sticky=N+S+E+W)
 
        #6
        img = PhotoImage(file="images/6.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("6"))
        button.img = img
        button.grid(row=3, column=2, sticky=N+S+E+W)
 
        #*
        img = PhotoImage(file="images/mul.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("*"))
        button.img = img
        button.grid(row=3, column=3, sticky=N+S+E+W)
 
        #fourth row
        #1
        img = PhotoImage(file="images/1.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("1"))
        button.img = img
        button.grid(row=4, column=0, sticky=N+S+E+W)
 
        #2
        img = PhotoImage(file="images/2.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("2"))
        button.img = img
        button.grid(row=4, column=1, sticky=N+S+E+W)
 
        #3
        img = PhotoImage(file="images/3.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("3"))
        button.img = img
        button.grid(row=4, column=2, sticky=N+S+E+W)
 
        #-
        img = PhotoImage(file="images/sub.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("-"))
        button.img = img
        button.grid(row=4, column=3, sticky=N+S+E+W)
 
        #fifth row
        #0
        img = PhotoImage(file="images/0.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("0"))
        button.img = img
        button.grid(row=5, column=0, sticky=N+S+E+W)
 
        #.
        img = PhotoImage(file="images/dot.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("."))
        button.img = img
        button.grid(row=5, column=1, sticky=N+S+E+W)
 
        #=
        img = PhotoImage(file="images/eql.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("="))
        button.img = img
        button.grid(row=5, column=2, sticky=N+S+E+W)
 
        #+
        img = PhotoImage(file="images/add.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("+"))
        button.img = img
        button.grid(row=5, column=3, sticky=N+S+E+W)
 
        #pack the GUI
        self.pack(fill=BOTH, expand=1)
 
    #processes button presses
    def process(self, button):
        #AC clears the display
        if(button == "AC"):
            #clear the display
            self.display["text"] = ""
        #= starts an evauationof whatever is on the display
        elif(button == "="):
            #get the expression in the display
            expr = self.display["text"]
            #if the evaluation returns an error
            try:
                #evaluate the expression
                result = eval(expr)
                #store the result to the display
                self.display["text"] = str(result)
            #handles if an error occurs during the evaluation
            except:
                #note the error in the display
                self.display["text"] = "ERROR"
        #otherwise it will just tack on the appropriate
        #operand/operator
        else:
            self.display["text"] += button

##############################
#the main part of the program#
##############################

#create the window
window = Tk()
#set the window title
window.title("The Reckoner")
#generate the GUI
p = MainGUI(window)
#display the GUI and wait for user interaction
window.mainloop()
