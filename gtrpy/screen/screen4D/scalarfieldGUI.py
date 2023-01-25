import importlib
import PySimpleGUI as sg

from sympy import preview, sympify

from gtrpy.equations.scalarfieldEP import *
from gtrpy.tools.image_resizer_fields4D import *
from gtrpy.tools.latex_output import *


# Image Path
resPATH = importlib.machinery.PathFinder().find_module("gtrpy").get_filename()[:-11] + 'res'


def scalarfield_gui4d(coord_sys):
    """
    The main process of the GUI that produces the image of a scalar field
    for a given coordinate system in 4D

    Args:
        coord_sys [list]: The coordinate system given as a list (e.g., [t,x,y,z])
    """
    scalar_field_layout = [
                            [sg.Image(resPATH + r'/images4D/scalarfield.png'),
                                sg.Input('0')],

                            [sg.Frame(layout=[
                                [sg.Button('Calculate', button_color='purple'),
                                    sg.Image(resPATH + r'/images4D/cov_scalarfield.png'),
                                    sg.Text('for', font=('Verdana', 11)),
                                    sg.Image(resPATH + r'/images4D/gamma.png'),
                                    sg.InputCombo(coord_sys, default_value=coord_sys[0])]],
                            title='Covariant Derivative', font=('Verdana', 12), expand_x=True,
                            element_justification='center', title_location='n')],

                            [sg.Frame(layout=[
                                [sg.Image(resPATH + r'/images4D/LX0.png'),
                                sg.InputText(default_text='0', font=('Tahoma', 11))],
                                [sg.Image(resPATH + r'/images4D/LX1.png'),
                                    sg.InputText(default_text='0', font=('Tahoma', 11))],
                                [sg.Image(resPATH + r'/images4D/LX2.png'),
                                    sg.InputText(default_text='0', font=('Tahoma', 11))],
                                [sg.Image(resPATH + r'/images4D/LX3.png'),
                                    sg.InputText(default_text='0', font=('Tahoma', 11))],
                                [sg.Button('Calculate', button_color='purple'),
                                    sg.Image(resPATH + r'/images4D/LX_scalarfield.png')]],
                            title='Lie Derivative', font=('Verdana', 12), expand_x=True,
                            element_justification='center', title_location='n')]
                            ]
    windows_scalar_field = sg.Window('Scalar Field', scalar_field_layout)
    while True:
        event, values = windows_scalar_field.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        else:
            scalar_field = values[1]   # Obtaining the scalar field
            # Calculation of the covariant derivative
            if event == 'Calculate':
                index_symbol = values[4]
                cd_scalar_field_eqn = cd_scalarfield_ep(coord_sys, scalar_field, index_symbol)
                preview(cd_scalar_field_eqn, viewer='file', filename=r'logs/cd_scalar_field.png', euler=True,
                        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                resize_cd_image4d('Scalar Field')
                layout_cd_scalar_field_result = [
                                                    [sg.Image(r'logs/cd_scalar_field.png')],
                                                    [sg.Button('Get LaTeX', button_color='orange')]
                                                ]
                window_cd_scalar_field_result = sg.Window('Scalar Field', layout_cd_scalar_field_result)
                while True:
                    event, values = window_cd_scalar_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
                    if event == 'Get LaTeX':
                        latex_output_scalar_field(cd_scalar_field_eqn)

            # Calculation of the Lie derivative
            if event == 'Calculate0':
                X = [sympify(values[i]) for i in range(6, 14, 2)]
                ld_scalar_field_eqn = ld_scalarfield_ep(coord_sys, scalar_field, X)
                preview(ld_scalar_field_eqn, viewer='file', filename=r'logs/ld_scalar_field.png', euler=True,
                        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                resize_ld_image4d('Scalar Field')
                layout_ld_scalar_field_result = [
                                                    [sg.Image(r'logs/ld_scalar_field.png')],
                                                    [sg.Button('Get LaTeX', button_color='orange')]
                                                ]
                window_ld_scalar_field_result = sg.Window('Scalar Field', layout_ld_scalar_field_result)
                while True:
                    event, values = window_ld_scalar_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
                    if event == 'Get LaTeX':
                        latex_output_scalar_field(ld_scalar_field_eqn)
