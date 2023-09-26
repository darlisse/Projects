from tkinter import *
from tkinter import messagebox

class Cryptography(Frame):

    def __init__(self):

        Frame.__init__(self)
        self.master.title("Crypto")
        self.pack()

        self.label = Label(self, text = "Cryptography", font = ("TimesNewRoman 20 bold italic"))
        self.label.pack(pady = 30)
     
        self.entry = Label (self, text = "Note: Input Letter.", font = ("Arial 10 italic"))
        self.entry.pack(pady = 2)
        self.entry = Entry(self, font = ("Arial 15 bold"))   
        self.entry.pack(pady = 30)

        self.variable = IntVar()
        self.entry1 = Label (self, text = "Note: Input Number.", font = ("Arial 10 italic"))
        self.entry1.pack(pady = 2)
        self.entry1 = Entry(self, font = ("Arial 15 bold"), textvariable = self.variable)
        self.entry1.pack(padx = 10)
        self.entry1.pack(pady = 30)

        #self.btn = Button(self, text = "Encrypt", fg = "blue", font = ("Georgia 15 bold"), command = self.encryption)
        #self.btn.pack(pady = 20)

        self.btn = Button(self, text = "Decrypt", fg = "red", font = ("Georgia 15 bold"), command = self.decryption)
        self.btn.pack(pady = 30)

    def encryption(self):
        try:
            content = self.entry.get()
            n = int(self.variable.get())
            code = ""
            for x in content:
                ordVal = ord(x) 
                cipherVal = ordVal + n
                if cipherVal > ord('z'):
                    cipherVal = ord('a') + n - \
                (ord('z') - ordVal + 1)
                code += chr(cipherVal) 
                print("ch: ", x)
                print("oc: ", ordVal)
                print("cV: ", cipherVal)
            print(code)

            messagebox.showinfo("Your encrypted messaged is", f"The message is: {code}") 
       
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid message.") 

    def decryption(self):
        try:
            content = self.entry.get()
            n = int(self.variable.get())
            text = ""
            for x in content:
                ordVal = ord(x)
                cipherVal = ordVal - n
                if cipherVal < ord('a'):
                    cipherVal = ord('z') - \
                (n - (ord('a') - ordVal + 1 ))
                text += chr(cipherVal)
                print("ch: ", x)
                print("oc: ", ordVal)
                print("cV: ", cipherVal)
            print(text)
            
            messagebox.showinfo("Your decrypted messaged is", f"The message is: {text}")
        except ValueError:
         messagebox.showerror("Error", "Please enter a valid message.")
def main():

    Cryptography().mainloop()
main()