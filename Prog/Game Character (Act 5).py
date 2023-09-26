import tkinter as tk
from tkinter import messagebox
from tkinter import *

PLAYER = ["Wizard", "Knight", "Archer", "Assassin"]
WEAPON = ["1. Wizard Staff", "2. Sword", "3. Bow and Arrow", "4. Katar"]
Wizard_Ability = ["1. Energy Ball","2. Dragon Breath","3. Crowns of Flame", "4. Hail Strom"]
Knight_Ability = ["1. Fire Slash", "2. Power Slash", "3. Gigantic Storm", "4. Chaotic Disaster"]
Archer_Ability = ["1. Take Aim","2. Quick Shot","3. Blazing Arrow","4. Frost Arrow"]
Assassin_Ability = ["1. Cloaking","2. Enchant Poisom","3. Sonic Acceleration","4. Meteor Assault"]
window = Tk()
class character(Frame):

    def __init__(self): 

        window.geometry('700x800')
        

        Frame. __init__(self)
        self.master.title("Game Character")
        self.pack()

        self.label = Label(self, text = "GAME CHARACTER", font = ("TimesNewRoman 20 bold italic"))
        self.label.pack(pady = 30)

        self.label = Label(self, text = "Choose only one character", font = ("Arial 12 italic"))
        self.label.pack(pady=20)
        self.btn = Button(self, text = PLAYER[0], command = self.select_ability1)
        self.btn.pack(pady = 10)
        self.btn = Button(self, text = PLAYER[1], command = self.select_ability2)
        self.btn.pack(pady = 10)
        self.btn = Button(self, text = PLAYER[2], command = self.select_ability3)
        self.btn.pack(pady = 10)
        self.btn = Button(self, text = PLAYER[3], command = self.select_ability4)
        self.btn.pack(pady = 10)
        
        self.entry = Label (self, text = "Note: For the next category choose only 3 abilities and input 1-4 only.", font = ("Arial 10 italic"))
        self.entry.pack(pady = 2)

    def select_ability1(self):
        self.entry = Label (self, text = Wizard_Ability[:4], font = ("Georgia 13 italic"))
        self.entry.pack(pady=20)
        self.variable = Variable()
        self.entry = Entry(self, font = ("Arial 15"), textvariable = self.variable)
        self.entry.pack(padx = 5)
        self.variable = Variable()
        self.entry = Entry(self, font = ("Arial 15"), textvariable = self.variable)
        self.entry.pack(padx = 5)
        self.variable = Variable()
        self.entry = Entry(self, font = ("Arial 15"), textvariable = self.variable)
        self.entry.pack(padx = 5)
        self.btn = Button(self, text = "ENTER", fg ="blue", font = ("TimesNewRoman 12 bold"), command = self.weapon_select)
        self.btn.pack(pady = 10)
    
    def select_ability2(self):
        self.entry = Label (self, text = Knight_Ability[:4], font = ("Georgia 13 italic"))
        self.entry.pack(pady=20) 
        self.variable = Variable()
        self.entry = Entry(self, font = ("Arial 15"), textvariable = self.variable)
        self.entry.pack(padx = 5)
        self.variable = Variable()
        self.entry = Entry(self, font = ("Arial 15"), textvariable = self.variable)
        self.entry.pack(padx = 5)
        self.variable = Variable()
        self.entry = Entry(self, font = ("Arial 15"), textvariable = self.variable)
        self.entry.pack(padx = 5)
        self.btn = Button(self, text = "ENTER", fg ="blue", font = ("TimesNewRoman 12 bold"), command = self.weapon_select)
        self.btn.pack(pady = 10)

    def select_ability3(self):
        self.entry = Label (self, text = Archer_Ability[:4], font = ("Georgia 13 italic"))
        self.entry.pack(pady=20) 
        self.variable = Variable()
        self.entry = Entry(self, font = ("Arial 15"), textvariable = self.variable)
        self.entry.pack(padx = 5)
        self.variable = Variable()
        self.entry = Entry(self, font = ("Arial 15"), textvariable = self.variable)
        self.entry.pack(padx = 5)
        self.variable = Variable()
        self.entry = Entry(self, font = ("Arial 15"), textvariable = self.variable)
        self.entry.pack(padx = 5)
        self.btn = Button(self, text = "ENTER", fg ="blue", font = ("TimesNewRoman 12 bold"), command = self.weapon_select)
        self.btn.pack(pady = 10)

    def select_ability4(self):
        self.entry = Label (self, text = Assassin_Ability[:4], font = ("Georgia 13 italic"))
        self.entry.pack(pady=20) 
        self.variable = Variable()
        self.entry = Entry(self, font = ("Arial 15"), textvariable = self.variable)
        self.entry.pack(padx = 5)
        self.variable = Variable()
        self.entry = Entry(self, font = ("Arial 15"), textvariable = self.variable)
        self.entry.pack(padx = 5)
        self.variable = Variable()
        self.entry = Entry(self, font = ("Arial 15"), textvariable = self.variable)
        self.entry.pack(padx = 5)
        self.btn = Button(self, text = "ENTER", fg ="blue", font = ("TimesNewRoman 12 bold"), command = self.weapon_select)
        self.btn.pack(pady = 10)

    
    def weapon_select(self):
            self.variable = Variable()
            self.entry = Label (self, text = "Note: Choose from 1-4 only.", font = ("Arial 10 italic"))
            self.entry.pack(pady = 2)
            self.entry = Label (self, text = WEAPON[:4], font = ("Georgia 13 italic"))
            self.entry.pack(pady=20)
            self.entry = Entry(self, font = ("Arial 15"), textvariable = self.variable)
            self.entry.pack(padx = 10)
            self.btn = Button(self, text = "ENTER", fg ="blue", font = ("TimesNewRoman 12 bold"), command = self.message)
            self.btn.pack(pady = 10)

    def message(self):
            messagebox.showinfo("Game Character", "Success on creating your character")
            exit()

def main():

    character().mainloop()

main()