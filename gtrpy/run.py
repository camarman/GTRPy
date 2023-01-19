# ========== GTRPy ==========
import os
import PySimpleGUI as sg

from gtrpy.screen.screen3D.mainpage import gtrpy_3d
from gtrpy.screen.screen4D.mainpage import gtrpy_4d

# ========== Creating logs directory ==========
current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'logs')
if not os.path.exists(final_directory):
    os.makedirs(final_directory)

# ========== PySimpleGUI Color Theme ==========
# Color theme option, provided by the PySimpleGUI. You can look at themes from:
# https://www.pysimplegui.org/en/latest/#themes-automatic-coloring-of-your-windows

sg.ChangeLookAndFeel('SandyBeach')

# ========== Welcome Page ==========
layout_dimension = [
                        [sg.Text('Welcome to GTRPy', font=('Georgia', 14))],
                        [sg.Text('Please choose the number of dimensions:', font=('Tahoma', 11)),
                            sg.InputCombo([3, 4], size=(8, 1), default_value='4', font=('Tahoma', 11))],
                        [sg.Submit(button_color='blue'), sg.Exit(button_color='red')]
                    ]

window_dim = sg.Window('GTRPy', layout_dimension)
event, values = window_dim.read()
ndim = values[0]
if event == sg.WIN_CLOSED or event == 'Exit':
    window_dim.close()
if event == 'Submit':
    window_dim.close()
    if ndim == 4:
        gtrpy_4d()
    else:
        gtrpy_3d()
