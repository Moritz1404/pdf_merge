from tkinter.constants import VERTICAL
from traceback import clear_frames
from merge import check_file, merge_pdf, open_file
import PySimpleGUI as sg

if __name__=='__main__':
    sg.theme('LightGrey1') #Color theme
    #Alles innerhalb des Fensters
    layout = [  [sg.Text('First PDF path:'), sg.InputText(key='Input1')],
                [sg.Text('Second PDF path:'), sg.InputText(key='Input2')],
                [sg.Text('Save to:'), sg.InputText(key='Input3')],
                [sg.Button('Merge'), sg.Button('Cancel')]
    ]
    #Create the window
    window = sg.Window('PDF Merger', layout)
    #Event loop
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

        if check_file([values['Input1'], values['Input2'], values['Input3']]) is True:
            merge_pdf([values['Input1'], values['Input2']], values['Input3'])
            open_file(values['Input3'])
            break
        else:
            sg.popup('Wrong Path', 'Enter a valid path')    
            window['Input1'].update('')
            window['Input2'].update('')
            window['Input3'].update('')

    window.close()