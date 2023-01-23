import PySimpleGUI as pg

layout = [[pg.Text("Hello World")], [pg.Button("OK")]]

window = pg.Window("Test", layout)

while True:
    event, values = window.read()

    if event == "OK" or event == pg.WIN_CLOSED:
        break

window.close()