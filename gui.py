import tkinter as tk
from tkinter import*
from tkinter import ttk



font = "Fredoka"

window = tk.Tk()

window.geometry("440x640")
window.title("XSum | Let's calculate it!")
window.config(background="#2E2E2E")

window.resizable(False, False)

tk.Text()

ttk.Label(text="X", background="#2E2E2E",foreground="#6F0CBD",font=("Fredoka Bold", 40)).place(x=280, y=40)
ttk.Label(text="Sum", background="#2E2E2E",foreground="White",font=("Fredoka Bold", 40)).place(x=320, y=40)
ttk.Entry(width=22,justify="right",font=("Fredoka Bold", 24)).place(x=23, y=110)


bx = 60
by = 180

btn = PhotoImage(file = "btn.png")
eq_btn = PhotoImage(file="eq.png")




bx = 55
by = 180

btns = list()

for i in range(6):
    for j in range(4):
        Button(window, width=70, height=50, borderwidth=0,background="#2E2E2E",image=btn).place(x=bx, y=by)
        bx += 100
    bx = 55
    by += 70
    
equals_btn = Button(window, width=70, height=50, background="#2E2E2E",borderwidth=0,image=eq_btn).place(x=355, y=530)
window.mainloop()