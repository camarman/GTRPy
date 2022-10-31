#---------- GRTC GUI ----------#

import PySimpleGUI as sg

from display3D.mainpage import grtc_gui3d
from display4D.mainpage import grtc_gui4d


# Color theme option, provided by the PySimpleGUI
sg.ChangeLookAndFeel('SandyBeach')


#---------- GRTC GUI - DIMENSIONS PAGE ----------#


layout_dimension = [
                        [sg.Text('General Relativity Tensor Calculator (GRTC)', font=('Georgia', 14))],
                        [sg.Text('Please enter the number of dimensions:', font=('Tahoma', 11)),
                         sg.InputCombo([3, 4], size=(8, 1), default_value='4', font=('Tahoma', 11))],
                        [sg.Submit(button_color='blue'), sg.Exit(button_color='red')]
                    ]

window_dim = sg.Window('GRTC', layout_dimension)
event, values = window_dim.read()
ndim = values[0]
if event == sg.WIN_CLOSED or event == 'Exit':
    window_dim.close()
if event == 'Submit':
    window_dim.close()
    if ndim == 4:
        grtc_gui4d()   # if the dimension is 4
    else:
        grtc_gui3d()   # if the dimension is 3

