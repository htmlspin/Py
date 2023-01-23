#Image Viewer

import PySimpleGUI as pg
import os.path

#Window Layout

file_list_column = [

    [
        pg.Text("Image Folder"),
        pg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
        pg.FolderBrowse(),

    ],

    [
        pg.Listbox(
            values=[], enable_events=True, size=(40,20), key="-FILE LIST-"
        )
    ],
]

image_viewer_column = [

    [pg.Text("Choose an image from the list on the left:")],
    [pg.Text(size=(40,1), key="-TOUT-")],
    [pg.Image(key="-IMAGE-")],

]

#LAYOUT

layout = [

    [

        pg.Column(file_list_column),
        pg.VSeperator(),
        pg.Column(image_viewer_column),

    ]
]

window = pg.Window("Image Viewer Test", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == pg.WIN_CLOSED:
        break


#List of Files

    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder,f))
            and f.lower().endswith((".png", ".jpg",".gif"))
        ]
        window["-FILE LIST-"].update(fnames)

    elif event == "-FILE LIST-":
        try:
            filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
        except:
            pass

window.close()