import PySimpleGUI as sg
from faceLandmark import get_ratio
import cv2

sg.theme("Material2")

layout = [


    [sg.Image("logo.png" , size = (800 , 160) )],
    [sg.Text("Please select the Image" , font = ( "Simplified Arabic Fixed" , 11 ) , pad = (235,30) , key = 'text')],
    [sg.In(key='val', pad=((170,10), (10,10))) , sg.FileBrowse(file_types=(("Text Files", "*.png *.jpeg *.jpg"),))],
    # [sg.FileBrowse(file_types=(("Text Files", "*.png"),), pad = (310,0) )],
    [sg.Button("Done" , font = ("Simplified Arabic" , 12) , size = (15 , 0) , pad = (270,30), key = 'done')],
    [sg.Button("Back" , font = ("Simplified Arabic" , 12)  ,size = (5,0), key = 'exit')]
]


def get_image():
    global layout
    window = sg.Window("Hello", layout, size=(700, 550))
    while True:
        event, value = window.Read()

        if event == 'done':
            get_ratio(2, value['val'])

        elif event == 'exit':
            cv2.destroyAllWindows()
            layout = [

                [sg.Image("grn.png", size=(800, 160))],
                [sg.Text("Please select the Image", font=("Simplified Arabic Fixed", 11), pad=(235, 30), key='text')],
                [sg.In(key='val', pad=((170, 10), (10, 10))), sg.FileBrowse(file_types=(("Text Files", "*.png"),))],
                # [sg.FileBrowse(file_types=(("Text Files", "*.png"),), pad = (310,0) )],
                [sg.Button("Done", font=("Simplified Arabic", 12), size=(15, 0), pad=(270, 30), key='done')],
                [sg.Button("Back", font=("Simplified Arabic", 12), size=(5, 0), key='exit')]
            ]
            break

    window.Close()