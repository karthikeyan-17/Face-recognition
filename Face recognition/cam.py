import PySimpleGUI as sg
from faceLandmark import get_ratio
import cv2

sg.theme("Material2")

layout = [


    [sg.Image("logo.png" , size = (800 , 160) )],
    [sg.Text("Give Access to your Camera" , font = ( "Simplified Arabic Fixed" , 11 ) , pad = (215,30) , key = 'text')],
    [sg.Button("Yes" , font = ("Simplified Arabic" , 12) , size = (15 , 0) , pad = (270,30), key = 'done')],
    [sg.Button("Back" , font = ("Simplified Arabic" , 12)  ,size = (5,0), key = 'exit')]
]


def get_cam():
    global layout
    window = sg.Window("Hello", layout, size=(700, 550))
    while True:
        event, value = window.Read()

        if event == 'done':
            get_ratio(1, "")

        elif event == 'exit':
            cv2.destroyAllWindows()
            layout = [

                [sg.Image("grn.png", size=(800, 160))],
                [sg.Text("Give Access to your Camera", font=("Simplified Arabic Fixed", 11), pad=(215, 30),
                         key='text')],
                [sg.Button("Yes", font=("Simplified Arabic", 12), size=(15, 0), pad=(270, 30), key='done')],
                [sg.Button("Back", font=("Simplified Arabic", 12), size=(5, 0), key='exit')]
            ]
            break

    window.Close()