import random
from tkinter import *
import sys
import tkinter
from tkinter import messagebox

myList = []

def randomPerson():
    person = Entry.get(peopleEnt)
    if person == "":
        Entry.delete(peopleEnt, first=0, last=9999)
        Entry.insert(peopleEnt, 0 , "Error")
    else:
        global myList
        myList.append(person)
        messagebox.showinfo("Added", person + " has been added")
        Entry.delete(peopleEnt, first=0, last=9999)

def randomGenerate():
    listLen = len(myList)
    randNum = random.randrange(0, listLen)
    generateRandLabel.configure(text=myList[randNum])

app = Tk()
app.title("People picker")
app.geometry("900x450")

peopleLabel = Label(app, text="Add person(s)", font='Helvetica 14 bold', pady=10, padx=10)
peopleLabel.grid(column=0, row=0)
peopleEnt = Entry(app, bd=5)
peopleEnt.grid(column=0, row=1)
peopleBtn = Button(app, command=randomPerson, text="Submit")
peopleBtn.grid(column=0, row=2)

allPeople = Label(app, text="",font='Helvetica 8 bold')
allPeople.grid(column=0, row=3)

generateRandBtn = Button(app, text="Generate Random", command=randomGenerate)
generateRandBtn.grid(column=0, row=4)
generateRandLabel = Label(app, text="", font='Helvetica 10 bold', pady=20)
generateRandLabel.grid(column=0, row=5)

app.mainloop()