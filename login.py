import tkinter as tk
from tkinter import *
from tkinter import ttk

def signin_click(event):
    pass

window = Tk()
window.geometry("440x640")
window.title("Sign In")
window.config(background="#2E2E2E")

window.resizable(False, False)


fields_pos =(6, 100)

ttk.Label(window, text="Welcome to", font=("Fredoka Bold",34), background="#2E2E2E", foreground="white").place(x=25, y=fields_pos[1]-40)
ttk.Label(window, text="X", font=("Fredoka Bold",34), background="#2E2E2E", foreground="#6F0CBD").place(x=290, y=fields_pos[1]-40)
ttk.Label(window, text="Sum", font=("Fredoka Bold",34), background="#2E2E2E", foreground="white").place(x=325, y=fields_pos[1]-40)

ttk.Label(window, text="Username or email", 
        font=("Fredoka Bold",16), 
        background="#2E2E2E", 
        foreground="white").place(x=fields_pos[0], y=fields_pos[1]+200-35)

login = Entry(window, font=("Fredoka Bold", 20), width=28)
login.place(x=fields_pos[0], y=fields_pos[1]+200)

ttk.Label(window, text="Password",
        font=("Fredoka Bold",16),
        background="#2E2E2E", 
        foreground="white").place(x=fields_pos[0], y=fields_pos[1]+290-35)

password = Entry(window, font=("Fredoka Bold", 20), width=28)
password.place(x=fields_pos[0], y=fields_pos[1]+290)



signin = Label(window, text="Sign up", 
        font=("Fredoka Bold",16), 
        background="#2E2E2E", 
        foreground="#8E8E8E")
signin.place(x=440-80, y=fields_pos[1]+290+40)
signin.bind("<Button-1>", signin_click)

ttk.Label(window, text="Have no account?", 
        font=("Fredoka Bold",16), 
        background="#2E2E2E", 
        foreground="white").place(x=fields_pos[0] + 180, y=fields_pos[1]+290+40)

window.mainloop()