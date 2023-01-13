# ========== GRTC GUI ==========
import PySimpleGUI as sg

from display.display3D.mainpage import grtc_gui3d
from display.display4D.mainpage import grtc_gui4d


# ========== PySimpleGUI Color Theme ==========

# Color theme option, provided by the PySimpleGUI. You can look at themes from:
# https://www.pysimplegui.org/en/latest/#themes-automatic-coloring-of-your-windows

sg.ChangeLookAndFeel('SandyBeach')


# ========== DIMENSIONS ==========

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


# ====================
# The code block below will delete all the .pyc files and __pycache__ directories.
# If you want to try it, download the pyclean package, and uncomment the lines below

# try:
#     import os
#     os.system('pyclean .')
#     print('The cleaning successfully ended.')
# except:
#     print('Something went wrong during the cleaning process!')
