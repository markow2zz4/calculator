import PySimpleGUI as sg

#sg.theme_previewer()

btn_size = 4
ttk = "Fredoka.ttf"
sg.theme("DarkGrey13")
sg.set_options(font=ttk, border_width=3)

layout = [
        [sg.Text('Welcome to XSum!', 26, font="Arial")],
        [sg.InputText(size=40)],
        [sg.Button("%", size=btn_size), sg.Button("CE", size=btn_size),
         sg.Button("C", size=btn_size), sg.Button("<", size=btn_size)],

        [sg.Button("1/x", size=btn_size), sg.Button("x2", size=btn_size),
         sg.Button("√", size=btn_size),sg.Button("÷", size=btn_size) ],

        [sg.Button("7",  size=btn_size), sg.Button("8",  size=btn_size),
         sg.Button("9",  size=btn_size),sg.Button("x",  size=btn_size) ],

        [sg.Button("5",  size=btn_size), sg.Button("7",  size=btn_size),
         sg.Button("6",  size=btn_size),sg.Button("-",  size=btn_size) ],

        [sg.Button("1",  size=btn_size), sg.Button("2",  size=btn_size),
         sg.Button("3",  size=btn_size),sg.Button("+",  size=btn_size) ],

        [sg.Button("+/-",  size=btn_size), sg.Button("0",  size=btn_size),
         sg.Button(",",  size=btn_size),sg.Button("=", size=btn_size) ],

]
window = sg.Window('XSum', layout)
while True:                             # The Event Loop
    event, values = window.read()
    print("You entered ", values[0]) #debug
    if event in (None, 'Exit', 'Cancel'):
        break
window.close()