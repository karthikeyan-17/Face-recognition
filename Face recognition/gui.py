import PySimpleGUI as sg
from image import get_image
from cam import get_cam

sg.theme("Material2")

layout = [

    # title page
    [sg.Image("logo.png", size = (800 , 160))],
    [sg.Text("Golden Ratio ", font=("Simplified Arabic Fixed", 17), pad=(255, 20), key='home')],
    [sg.Text("A Tool to help Plastic Surgeons ", font=("Simplified Arabic Fixed", 12), pad=(185, 20), key='home')],
    [sg.Button("Use an Image ", font=("Simplified Arabic", 13), size=(40, 0), pad=(185, 18), key='image')],
    [sg.Button("Live Camera Feed ", font=("Simplified Arabic", 13), size=(40, 0), pad=(185, 18), key='cam')]
]

window = sg.Window("Hello", layout, size=(700, 550))
while True:
    event, value = window.Read()

    if event == 'image':
        get_image()

    elif event == 'cam':
        get_cam()

    else:
        break

window.Close()
