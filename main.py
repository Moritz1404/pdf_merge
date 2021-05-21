from tkinter.constants import VERTICAL
from traceback import clear_frames
from merge import check_file, merge_pdf, open_file
import PySimpleGUI as sg

if __name__=='__main__':
    sg.theme('DarkAmber') #Color theme
    #Alles innerhalb des Fensters
    layout = [  [sg.Text('First PDF path:'), sg.InputText(key='Input1')],
                [sg.Text('Second PDF path:'), sg.InputText(key='Input2')],
                [sg.Button('Merge'), sg.Button('Cancel')]
    ]
    #Create the window
    window = sg.Window('PDF Merger', layout)
    #Event loop
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

        if check_file([values['Input1'], values['Input2']]) is True:
            merge_pdf([values['Input1'], values['Input2']], "out.pdf")
            open_file("out.pdf")
            break
        else:
            sg.popup('Wrong Path', 'Enter a valid path')    
            window['Input1'].update('')
            window['Input2'].update('')

    window.close()