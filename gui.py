import PySimpleGUI as sg

layout = [
        [sg.Text('Welcome to XSum!', 20,justification="C")],
        [sg.Text("First number here...")],
        [sg.InputText()]
]
window = sg.Window('XSum', layout)
while True:                             # The Event Loop
    event, values = window.read()
    print("You entered ", values[0]) #debug
    if event in (None, 'Exit', 'Cancel'):
        break
window.close()