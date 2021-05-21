from tkinter.constants import VERTICAL
from merge import check_file, merge_pdf, open_file
import PySimpleGUI as sg

if __name__=='__main__':
    sg.theme('DarkAmber') #Color theme
    #Alles innerhalb des Fensters
    layout = [  [sg.Text('First PDF path:'), sg.InputText()],
                [sg.Text('Second PDF path:'), sg.InputText()],
                [sg.Button('Merge'), sg.Button('Cancel')]
    ]
    #Create the window
    window = sg.Window('PDF Merger', layout)
    #Event loop
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

        if check_file([values[0], values[1]]) is True:
            merge_pdf([values[0], values[1]], "out.pdf")
            open_file("out.pdf")
            break    

    window.close()