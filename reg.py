import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import ImageTk, Image
import random


def signin_click(event):
    pass

def change(event):
    colors = ["#5B950C","#6647C4","#036935","#3F9549","#E82D42",
              "#5836E1","#B8106A","#FE5F23","#50AAEA","#C30323",
              "#587ED3","#A47312","#64FD4F","#5E401D","#19F9F4",
              "#11D305","#3F3191","#091C3D","#14BCC4","#16061C",
              "#872BEB","#F6A97B","#ABA032","#9F51A6","#FD15B2",
              "#F900A6","#90078F","#41BF6C","#0F2F62","#68F559"]
    # for i in range(30):
    #     colors.append('#%06X' % random.randint(0, 0xFFFFFF))
    #     print(f'"{colors[i]}"',end=',')
    signin_btn['foreground'] = random.choice(colors)


def registration_click(event):
    change(event)
    pass


window = Tk()
window.geometry("440x640")
window.title("Sign up")
window.config(background="#2E2E2E")

window.resizable(False, False)
#tasks

#create anim with greeting []
#make a reg page (verst) [√]
#make a signin_click func []
#make fields control []
#make signin btn []



fields_pos =(6, 100)

ttk.Label(window, text="Welcome to", font=("Fredoka Bold",34), background="#2E2E2E", foreground="white").place(x=25, y=fields_pos[1]-40)
ttk.Label(window, text="X", font=("Fredoka Bold",34), background="#2E2E2E", foreground="#6F0CBD").place(x=290, y=fields_pos[1]-40)
ttk.Label(window, text="Sum", font=("Fredoka Bold",34), background="#2E2E2E", foreground="white").place(x=325, y=fields_pos[1]-40)

ttk.Label(window, text="Name", 
        font=("Fredoka Bold",16), 
        background="#2E2E2E", 
        foreground="white").place(x=fields_pos[0], y=fields_pos[1] + 110-35)

name = Entry(window, font=("Fredoka Bold", 20), width=28)
name.place(x=fields_pos[0], y=fields_pos[1]+110)

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



signin = Label(window, text="Sign in", 
        font=("Fredoka Bold",16), 
        background="#2E2E2E", 
        foreground="#44E729")
signin.place(x=440-75, y=fields_pos[1]+290+40)
signin.bind("<Button-1>", signin_click)

ttk.Label(window, text="Already have an account?", 
        font=("Fredoka Bold",16), 
        background="#2E2E2E", 
        foreground="white").place(x=fields_pos[0] + 100, y=fields_pos[1]+290+40)


img = ImageTk.PhotoImage(Image.open('btns/ver2.png').resize((150, 150)))

st = Style()

signin_btn = Label(window, text="Sign Up", 
                background="#2E2E2E",
                font=("Fredoka Bold", 18), foreground="white")
signin_btn.place(x=190, y=520)
signin_btn.bind("<Button-1>", registration_click)

window.mainloop()