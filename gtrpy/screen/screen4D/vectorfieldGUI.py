import importlib
import PySimpleGUI as sg

from sympy import preview, sympify

from gtrpy.equations.vectorfieldEP import *
from gtrpy.tools.image_resizer_fields4D import *
from gtrpy.tools.latex_output import *


# Image Path
resPATH = importlib.machinery.PathFinder().find_module("gtrpy").get_filename()[:-11] + 'res'


def vectorfield_gui4d(event, metric_tensor, coord_sys):
    """
    The main process of the GUI that produces the image of a vector field
    for a given metric tensor and coordinate system in 4D

    Args:
        event               : Events read from Vector Field GUI
        metric_tensor [list]: The metric tensor, provided by the user
        coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])
    """
    if event == 'Type (1,0) Vector Field':
        vector_field_10_layout = [
                                    [sg.Image(resPATH + r'/images4D/vectorfield_10_0.png'),
                                    sg.InputText(default_text='0', font=('Tahoma', 11))],
                                    [sg.Image(resPATH + r'/images4D/vectorfield_10_1.png'),
                                    sg.InputText(default_text='0', font=('Tahoma', 11))],
                                    [sg.Image(resPATH + r'/images4D/vectorfield_10_2.png'),
                                    sg.InputText(default_text='0', font=('Tahoma', 11))],
                                    [sg.Image(resPATH + r'/images4D/vectorfield_10_3.png'),
                                    sg.InputText(default_text='0', font=('Tahoma', 11))],

                                    [sg.Frame(layout=[
                                        [sg.Button('Calculate', button_color='purple'),
                                        sg.Image(resPATH + r'/images4D/vectorfield_01.png')]],
                                    title='Vary Type', font=('Verdana', 12), expand_x=True,
                                    element_justification='center', title_location='n')],

                                    [sg.Frame(layout=[
                                        [sg.Button('Calculate', button_color='purple'),
                                        sg.Image(resPATH + r'/images4D/cov_vectorfield_10.png'),
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
                                        sg.Image(resPATH + r'/images4D/LX_vectorfield_10.png')]],
                                    title='Lie Derivative', font=('Verdana', 12), expand_x=True,
                                    element_justification='center', title_location='n')],

                                    [sg.Frame(layout=[
                                        [sg.Button('Check', button_color='purple'),
                                            sg.Image(resPATH + r'/images4D/killingvector.png')]],
                                    title='Killing Field Condition', font=('Verdana', 12), expand_x=True,
                                    element_justification='center', title_location='n')]
                                    ]
        windows_vector_field = sg.Window('Vector Field', vector_field_10_layout)
        while True:
            event, values = windows_vector_field.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            else:
                vector_field = [sympify(values[i]) for i in range(1, 9, 2)]   # Obtaining the vector field

                # Varying the type of the vector field
                if event == 'Calculate':
                    vry_vector_field_eqn = vry_vectorfield10_ep(metric_tensor, coord_sys, vector_field)
                    preview(vry_vector_field_eqn, viewer='file', filename=r'logs/vry_vector_field_10.png', euler=True,
                            dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                    resize_vry_type_image4d('Type (1,0) Vector Field')
                    layout_vry_vector_field_result = [
                                                        [sg.Image(r'logs/vry_vector_field_10.png')],
                                                        [sg.Button('Get LaTeX', button_color='orange')]
                                                    ]
                    window_vry_vector_field_result = sg.Window('Vector Field', layout_vry_vector_field_result)
                    while True:
                        event, values = window_vry_vector_field_result.read()
                        if event == sg.WIN_CLOSED:
                            break
                        if event == 'Get LaTeX':
                            latex_output_vector_field(vry_vector_field_eqn)

                # Calculation of the covariant derivative
                if event == 'Calculate0':
                    index_symbol = values[11]
                    cd_vector_field_eqn = cd_vectorfield10_ep(metric_tensor, coord_sys, vector_field, index_symbol)
                    preview(cd_vector_field_eqn, viewer='file', filename=r'logs/cd_vector_field_10.png', euler=True,
                            dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                    resize_cd_image4d('Type (1,0) Vector Field')
                    layout_cd_vector_field_result = [
                                                        [sg.Image(r'logs/cd_vector_field_10.png')],
                                                        [sg.Button('Get LaTeX', button_color='orange')]
                                                    ]
                    window_cd_vector_field_result = sg.Window('Vector Field', layout_cd_vector_field_result)
                    while True:
                        event, values = window_cd_vector_field_result.read()
                        if event == sg.WIN_CLOSED:
                            break
                        if event == 'Get LaTeX':
                            latex_output_vector_field(cd_vector_field_eqn)

                # Calculation of the Lie derivative
                elif event == 'Calculate1':
                    X = [sympify(values[i]) for i in range(13, 21, 2)]
                    ld_vector_field_eqn = ld_vectorfield10_ep(metric_tensor, coord_sys, vector_field, X)
                    preview(ld_vector_field_eqn, viewer='file', filename=r'logs/ld_vector_field_10.png', euler=True,
                            dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                    resize_ld_image4d('Type (1,0) Vector Field')
                    layout_ld_vector_field_result = [
                                                        [sg.Image(r'logs/ld_vector_field_10.png')],
                                                        [sg.Button('Get LaTeX', button_color='orange')]
                                                    ]
                    window_ld_vector_field_result = sg.Window('Vector Field', layout_ld_vector_field_result)
                    while True:
                        event, values = window_ld_vector_field_result.read()
                        if event == sg.WIN_CLOSED:
                            break
                        if event == 'Get LaTeX':
                            latex_output_vector_field(ld_vector_field_eqn)

                # Checking Killing Field Condition
                elif event == 'Check':
                    killingfield_eqn = killingfield10_ep(metric_tensor, coord_sys, vector_field)
                    preview(killingfield_eqn, viewer='file', filename=r'logs/killing_field_10.png', euler=True,
                            dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                    resize_killing_image4d('Type (1,0) Vector Field')
                    layout_killing_field_result = [
                                                        [sg.Image(r'logs/killing_field_10.png')]
                                                ]
                    window_killing_field_result = sg.Window('Vector Field', layout_killing_field_result)
                    while True:
                        event, values = window_killing_field_result.read()
                        if event == sg.WIN_CLOSED:
                            break
    else:
        vector_field_01_layout = [
                                    [sg.Image(resPATH + r'/images4D/vectorfield_01_0.png'),
                                        sg.InputText(default_text='0', font=('Tahoma', 11))],
                                    [sg.Image(resPATH + r'/images4D/vectorfield_01_1.png'),
                                        sg.InputText(default_text='0', font=('Tahoma', 11))],
                                    [sg.Image(resPATH + r'/images4D/vectorfield_01_2.png'),
                                        sg.InputText(default_text='0', font=('Tahoma', 11))],
                                    [sg.Image(resPATH + r'/images4D/vectorfield_01_3.png'),
                                        sg.InputText(default_text='0', font=('Tahoma', 11))],

                                    [sg.Frame(layout=[
                                        [sg.Button('Calculate', button_color='purple'),
                                        sg.Image(resPATH + r'/images4D/vectorfield_10.png')]],
                                    title='Vary Type', font=('Verdana', 12), expand_x=True,
                                    element_justification='center', title_location='n')],

                                    [sg.Frame(layout=[
                                        [sg.Button('Calculate', button_color='purple'),
                                        sg.Image(resPATH + r'/images4D/cov_vectorfield_01.png'),
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
                                        sg.Image(resPATH + r'/images4D/LX_vectorfield_01.png')]],
                                    title='Lie Derivative', font=('Verdana', 12), expand_x=True,
                                    element_justification='center', title_location='n')],

                                    [sg.Frame(layout=[
                                        [sg.Button('Check', button_color='purple'),
                                        sg.Image(resPATH + r'/images4D/killingvector.png')]],
                                    title='Killing Field Condition', font=('Verdana', 12), expand_x=True,
                                    element_justification='center', title_location='n')]
                                ]
        windows_vector_field = sg.Window('Vector Field', vector_field_01_layout)
        while True:
            event, values = windows_vector_field.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            else:
                vector_field = [sympify(values[i]) for i in range(1, 9, 2)]   # Obtaining the vector field

                # Varying the type of the vector field
                if event == 'Calculate':
                    vry_vector_field_eqn = vry_vectorfield01_ep(metric_tensor, coord_sys, vector_field)
                    preview(vry_vector_field_eqn, viewer='file', filename=r'logs/vry_vector_field_01.png', euler=True,
                            dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                    resize_vry_type_image4d('Type (0,1) Vector Field')
                    layout_vry_vector_field_result = [
                                                        [sg.Image(r'logs/vry_vector_field_01.png')],
                                                        [sg.Button('Get LaTeX', button_color='orange')]
                                                    ]
                    window_vry_vector_field_result = sg.Window('Vector Field', layout_vry_vector_field_result)
                    while True:
                        event, values = window_vry_vector_field_result.read()
                        if event == sg.WIN_CLOSED:
                            break
                        if event == 'Get LaTeX':
                            latex_output_vector_field(vry_vector_field_eqn)

                # Calculation of the covariant derivative
                if event == 'Calculate0':
                    index_symbol = values[11]
                    cd_vector_field_eqn = cd_vectorfield01_ep(metric_tensor, coord_sys, vector_field, index_symbol)
                    preview(cd_vector_field_eqn, viewer='file', filename=r'logs/cd_vector_field_01.png', euler=True,
                            dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                    resize_cd_image4d('Type (0,1) Vector Field')
                    layout_cd_vector_field_result = [
                                                        [sg.Image(r'logs/cd_vector_field_01.png')],
                                                        [sg.Button('Get LaTeX', button_color='orange')]
                                                    ]
                    window_cd_vector_field_result = sg.Window('Vector Field', layout_cd_vector_field_result)
                    while True:
                        event, values = window_cd_vector_field_result.read()
                        if event == sg.WIN_CLOSED:
                            break
                        if event == 'Get LaTeX':
                            latex_output_vector_field(cd_vector_field_eqn)

                # Calculation of the Lie derivative
                elif event == 'Calculate1':
                    X = [sympify(values[i]) for i in range(13, 21, 2)]
                    ld_vector_field_eqn = ld_vectorfield01_ep(metric_tensor, coord_sys, vector_field, X)
                    preview(ld_vector_field_eqn, viewer='file', filename=r'logs/ld_vector_field_01.png', euler=True,
                            dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                    resize_ld_image4d('Type (0,1) Vector Field')
                    layout_ld_vector_field_result = [
                                                        [sg.Image(r'logs/ld_vector_field_01.png')],
                                                        [sg.Button('Get LaTeX', button_color='orange')]
                                                    ]
                    window_ld_vector_field_result = sg.Window('Vector Field', layout_ld_vector_field_result)
                    while True:
                        event, values = window_ld_vector_field_result.read()
                        if event == sg.WIN_CLOSED:
                            break
                        if event == 'Get LaTeX':
                            latex_output_vector_field(ld_vector_field_eqn)

                # Checking Killing Field Condition
                elif event == 'Check':
                    killingfield_eqn = killingfield01_ep(metric_tensor, coord_sys, vector_field)
                    preview(killingfield_eqn, viewer='file', filename=r'logs/killing_field_01.png', euler=True,
                            dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                    resize_killing_image4d('Type (0,1) Vector Field')
                    layout_killing_field_result = [
                                                        [sg.Image(r'logs/killing_field_01.png')]
                                                ]
                    window_killing_field_result = sg.Window('Vector Field', layout_killing_field_result)
                    while True:
                        event, values = window_killing_field_result.read()
                        if event == sg.WIN_CLOSED:
                            break
