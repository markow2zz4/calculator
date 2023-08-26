import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()

window.geometry("440x640")
window.title("XSum | Let's calculate it!")
window.config(background="#2E2E2E")

window.resizable(False, False)

tk.Text()

ttk.Label(text="X", background="#2E2E2E",foreground="#6F0CBD",font=("Fredoka Bold", 40)).place(x=280, y=40)
ttk.Label(text="Sum", background="#2E2E2E",foreground="White",font=("Fredoka Bold", 40)).place(x=320, y=40)
entry_field = Entry(width=22,justify="right",font=("Fredoka Bold", 24), state="normal")
entry_field.place(x=23, y=110)


bx = 60
by = 180

#tasks


btn = [PhotoImage(file="btns/percent.png"),
            PhotoImage(file = "btns/ce.png"),
            PhotoImage(file = "btns/c.png"),
            PhotoImage(file = "btns/--.png"),
            PhotoImage(file = "btns/1divx.png"),
            PhotoImage(file = "btns/x2.png"),
            PhotoImage(file = "btns/rad.png"),
            PhotoImage(file = "btns/div.png"),
            PhotoImage(file = "btns/7.png"),
            PhotoImage(file = "btns/8.png"),
            PhotoImage(file = "btns/9.png"),
            PhotoImage(file = "btns/x.png"),
            PhotoImage(file = "btns/4.png"),
            PhotoImage(file = "btns/5.png"),
            PhotoImage(file = "btns/6.png"),
            PhotoImage(file = "btns/-.png"),
            PhotoImage(file = "btns/1.png"),
            PhotoImage(file = "btns/2.png"),
            PhotoImage(file = "btns/3.png"),
            PhotoImage(file = "btns/+.png"),
            PhotoImage(file = "btns/+-.png"),
            PhotoImage(file = "btns/0.png"),
            PhotoImage(file = "btns/,.png"),
            PhotoImage(file = "btns/=.png")]

bx = 55
by = 180

nums = ["%","CE", "C", "<", "1/x", "x2", "√","÷","7",
        '8', '9', 'x', '4', '5', '6', '-', '1', '2', 
        '3', "+", "+/-", "0", ",", "="]
counter = 0

btns = list()

#remove
def entrySet(event):
    global dic
    global entry_field

    if(Button(dic["btn_3"]).focus()):
        entry_field.delete(0, END)


dic = {}

for i in range(6):
    for j in range(4):

        dic["btn_" + str(counter)] = Button(window, width=70, height=50, borderwidth=0,
                                            background="#2E2E2E",image=btn[counter])
        dic[f"btn_{counter}"].place(x=bx, y=by)
        counter+=1
        bx += 100
    bx = 55
    by += 70

def clearLast():
    """ for CE func (completed) """
    chis = entry_field.get()
    number = 0
    counter = len(chis)

    try:
        while type(int(chis[counter-1])) == int:
            entry_field.delete(len(entry_field.get())-1)
            counter -= 1
        print(chis)
        
    except:
        pass

def eq():
    try:
        chis = entry_field.get()
        if(chis.find("//") == True or chis.find("**") == True or chis.find("%%") == True):
            raise Exception("Error")
        else:
            entry_field.delete(0, END)

            if("," in chis):
                chis = chis.replace(",", ".")
                
            example = eval(chis)

            if example == float(f'{int(example)}.0'):
                example = int(example)
            else:
                example = float(f'{example:.6}')
                entry_field.delete(0, END)
            entry_field.insert(0, example)
                
    except Exception as e:
        
        if(chis == "Error" or chis == ""):
            entry_field.delete(0, END)
        
        else:
            entry_field.delete(0, END)
            entry_field.insert(0, "Error")

def percent():
    entry_field.insert(END, "%")
    chis = entry_field.get()
    if("%%" in chis):
        entry_field.delete(0, END)
        entry_field.insert(0, "Error")

def divx():
    chis = entry_field.get()
    if(chis.isdigit() != True):
        entry_field.delete(0, END)
        entry_field.insert(0, "Error")
    else:
        example = eval("1/" + str(chis))
        
        entry_field.delete(0, END)
        entry_field.insert(0, f'{example:.6}')

def x2():
    chis = entry_field.get()
    if(chis.isdigit() != True or len(str(int(chis) * int(chis))) >= 4000):
        entry_field.delete(0, END)
        entry_field.insert(0, "Error")
    else:
        
        entry_field.delete(0, END)
        entry_field.insert(0, int(chis) * int(chis))

def rad():
    chis = entry_field.get()
    if(chis.isdigit() != True):
        entry_field.delete(0, END)
        entry_field.insert(0, "Error")
    else:
        example = int(chis) ** 0.5
        if example == float(f'{int(example)}.0'):
            example = int(example)
        else:
            example = float(f'{example:.6}')
        entry_field.delete(0, END)
        entry_field.insert(0, example)

def multiple():
    chis = entry_field.get()

    if(chis[len(chis) -1] in "*+-%/"):
        #solve a much multiples
        entry_field.delete(len(entry_field.get())-1)
        entry_field.insert(END, "*")
    else:
        entry_field.insert(END, "*")

def plus():
    chis = entry_field.get()


    if(chis[len(chis) -1] in "*+-%/"):
        #solve a much pluses
        entry_field.delete(len(entry_field.get())-1)
        entry_field.insert(END, "+")
    else:
        entry_field.insert(END, "+")

def comma():
    chis = entry_field.get()
    if(chis[len(chis) -1] not in "*+-%/,"):
        entry_field.insert(END, ",")
    else:
        entry_field.insert(END, "")

def change_sign2():
    chis = entry_field.get()
    number = ""

    counter = len(chis)
    temp = 0
        
    if("(" in chis and ")" in chis): chis = chis.replace("(", "").replace(")","")
    try:
        while chis[counter - 1].isdigit() == True:
            print("shicso - ", chis[counter - 1])
            number += chis[counter - 1]
            counter -= 1
            temp += 1
    except:
        #kostyl
        pass
        # entry_field.delete(0, END)
        # entry_field.insert(entry_field.get().replace("-", "+"))

    if chis.isdigit():
        number = int(chis)
        entry_field.delete(0, END)
        entry_field.insert(0, number)
    else:
        for i in range(temp+1+2):
            entry_field.delete(len(entry_field.get()) - 1)


        
        chis = chis.replace("-", "", 1).replace("-", "+")
        
        entry_field.delete(0, END)
        entry_field.insert(0, chis)
        

def change_sign():
    chis = entry_field.get()
    counter = len(chis)
    number = 0
    if(chis[len(chis) - 1] == "0"):
        number = 1
    else:
        number = 0

    if("(" in chis and ")" in chis):
        chis = chis.replace("(", "").replace(")","")
        print(chis)

    try:
        #not completed
        if(str(int(chis) * -1).isdigit() == True or chis.isdigit() == True):
            number = int(chis)

            entry_field.delete(0, END)
            

            if(abs(int(number)) > 0):
                entry_field.insert(END, f'{int(number) * -1}')
            else:
                entry_field.insert(END, f'({int(number) * -1})')

        else:

            if(abs(int(number)) > 0):
                entry_field.insert(END, f'{int(number) * -1}')
            else:
                entry_field.insert(END, f'({int(number) * -1})')

            while type(int(chis[counter-1])) == int:
                number += int(chis[counter-1])
                #solve with 1number
                entry_field.delete(len(entry_field.get())-1)
                
                number*=10
                print(number)
                counter -= 1
            number/=10
            number = str(int(number))[::-1]
            
            
        
    
    except:
        pass
#-----------------------------BTNS-----------------------------#
dic["btn_0"].config(command=percent)
dic["btn_1"].config(command=clearLast)
dic["btn_2"].config(command=lambda: entry_field.delete(0, END))
dic["btn_3"].config(command=lambda: entry_field.delete(len(entry_field.get())-1))

dic["btn_4"].config(command=divx)
dic["btn_5"].config(command=x2)
dic["btn_6"].config(command=rad)
dic["btn_7"].config(command=lambda: entry_field.insert(END, "/"))

dic["btn_8"].config(command=lambda: entry_field.insert(END, "7"))
dic["btn_9"].config(command=lambda: entry_field.insert(END, "8"))
dic["btn_10"].config(command=lambda: entry_field.insert(END, "9"))

dic["btn_11"].config(command=multiple)

dic["btn_12"].config(command=lambda: entry_field.insert(END, "4"))
dic["btn_13"].config(command=lambda: entry_field.insert(END, "5"))
dic["btn_14"].config(command=lambda: entry_field.insert(END, "6"))
dic["btn_15"].config(command=lambda: entry_field.insert(END, "-"))
dic["btn_16"].config(command=lambda: entry_field.insert(END, "1"))
dic["btn_17"].config(command=lambda: entry_field.insert(END, "2"))
dic["btn_18"].config(command=lambda: entry_field.insert(END, "3"))

dic["btn_19"].config(command=plus)
dic["btn_20"].config(command=change_sign2)
dic["btn_21"].config(command=lambda: entry_field.insert(END, "0"))
dic["btn_22"].config(command=comma)
#-----------------------------BTNS-end-----------------------------#

equals = Button(window, width=70, height=50, borderwidth=0,background="#2E2E2E",image=btn[len(btn) - 1], command=eq)
equals.place(x=355, y=by-70)

window.mainloop()