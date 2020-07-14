from random import randrange
from tkinter import *

rollNum = 0
numHold = 0
numLast = 0


class Dice:
    def __init__(self):
        global rollNum
        global numHold
        global numLast

        self.root = Tk()  # the object for the Tkinter
        self.root.geometry("200x200")
        self.root.title("Dice Roller")

        # LABEL INSTRUCTIONS
        self.labelInstr = Label(self.root,
                                text="Select Dice and Roll",
                                font=("Helvetica", 10,))
        self.labelInstr.place(relx=0.5,
                              rely=0.2,
                              anchor='center')
        # LABEL FOR ROLL
        self.labelRoll = Label(self.root,
                               text=rollNum,
                               font=("Helvetica", 25, 'bold'))
        self.labelRoll.place(relx=0.5,
                             rely=0.4,
                             anchor='center')

        # ROLL BUTTON
        reRoll = Button(self.root, text="roll", command=self.roll, font="Helvetica", height=2, width=8)
        reRoll.place(x=60, y=140)

        # DROP-DOWN MENU
        menuList = [2, 4, 6, 8, 12, 16, 20]
        self.var = StringVar()
        self.var.set(menuList[2])
        self.menuSel = OptionMenu(self.root,
                                  self.var,
                                  *menuList)
        self.menuSel.place(x=61,
                           y=10)

        # LABEL FOR LAST ROLL
        self.labelLast = Label(self.root)

        # PACKING AND RUNNING
        self.menuSel.pack()
        self.root.mainloop()

    def roll(self):
        global rollNum
        global numHold
        global numLast

        self.labelLast.destroy()

        numHold = rollNum
        rollNum = str(randrange(int(self.var.get())) + 1)  # the number that is rolled and held to print
        self.labelRoll.configure(text=rollNum)

        # LABEL FOR LAST ROLL
        numLast = numHold
        self.labelLast = Label(self.root,
                               text="last roll: " + str(numLast),
                               font=("Helvetica", 10, 'bold'))
        self.labelLast.place(relx=0.5,
                             rely=0.6,
                             anchor='center')


Dice()
