import PySimpleGUI as pg

layout = [[pg.Text("Hello World")], [pg.Button("OK")]]
testLayout = [[pg.Text("Hello World")]]
window = pg.Window("Test", layout)

pg.popup(title="Hello World", custom_text= 'This is a pop up, welcome to my test program', background_color= "White", auto_close_duration= 10) 

while True:
    event, values = window.read()

    if event == "OK" or event == pg.WIN_CLOSED:
        break

window.close()