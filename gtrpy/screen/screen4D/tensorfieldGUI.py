import importlib
import PySimpleGUI as sg

from sympy import preview, sympify

from gtrpy.equations.tensorfieldEP import *
from gtrpy.tools.image_resizer_fields4D import *


# Image Path
resPATH = importlib.machinery.PathFinder().find_module("gtrpy").get_filename()[:-11] + 'res'


def tensorfield_gui4d(event, metric_tensor, coord_sys):
    """
    The main process of the GUI that produces the image of a tensor field
    for a given metric tensor and coordinate system in 4D

    Args:
        event               : Events read from Tensor Field GUI
        metric_tensor [list]: The metric tensor, provided by the user
        coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])
    """
    if event == 'Type (2,0) Tensor Field':
        tensor_field_20_layout =  [
                                    [sg.Image(resPATH + r'/images4D/tensorfield_20_0.png'),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1), font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1), font=('Tahoma', 11))],
                                    [sg.Image(resPATH + r'/images4D/tensorfield_20_1.png'),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15 , 1), font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1), font=('Tahoma', 11))],
                                    [sg.Image(resPATH + r'/images4D/tensorfield_20_2.png'),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1), font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1), font=('Tahoma', 11))],
                                    [sg.Image(resPATH + r'/images4D/tensorfield_20_3.png'),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1), font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1), font=('Tahoma', 11))],

                                    [sg.Frame(layout=[
                                        [sg.Button('Calculate', button_color='purple'),
                                        sg.Image(resPATH + r'/images4D/cov_tensorfield_20.png'),
                                        sg.Text('for', font=('Verdana', 11)),
                                        sg.Image(resPATH + r'/images4D/gamma.png'),
                                        sg.InputCombo(coord_sys, default_value=coord_sys[0])]],
                                    title='Covariant Derivative', font=('Verdana', 12), expand_x=True, element_justification='center', title_location='n')],

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
                                        sg.Image(resPATH + r'/images4D/LX_tensorfield_20.png')]],
                                    title='Lie Derivative', font=('Verdana', 12), expand_x=True, element_justification='center', title_location='n')]
                                    ]
        windows_tensor_field = sg.Window('Tensor Field', tensor_field_20_layout)
        while True:
            event, values = windows_tensor_field.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            else:
                tensor_field = [[sympify(values[i+j]) for i in range(4)] for j in range(1, 21, 5)]   # Obtaining the tensor field

                # Calculation of the covariant derivative
                if event == 'Calculate':
                    index_symbol = values[22]
                    cd_tensor_field_eqn = cd_tensorfield20_ep(metric_tensor, coord_sys, tensor_field, index_symbol)
                    preview(cd_tensor_field_eqn, viewer='file', filename=r'logs/cd_tensor_field_20.png', euler=True,
                            dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                    resize_cd_image4d('Type (2,0) Tensor Field')
                    layout_cd_tensor_field_result = [
                                                        [sg.Image(r'logs/cd_tensor_field_20.png')],
                                                    ]
                    window_cd_tensor_field_result = sg.Window('Tensor Field', layout_cd_tensor_field_result)
                    while True:
                        event, values = window_cd_tensor_field_result.read()
                        if event == sg.WIN_CLOSED:
                            break

                # Calculation of the Lie derivative
                elif event == 'Calculate0':
                    X = [sympify(values[i]) for i in range(24, 32, 2)]
                    ld_tensor_field_eqn = ld_tensorfield20_ep(metric_tensor, coord_sys, tensor_field, X)
                    preview(ld_tensor_field_eqn, viewer='file', filename=r'logs/ld_tensor_field_20.png', euler=True,
                            dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                    resize_ld_image4d('Type (2,0) Tensor Field')
                    layout_ld_tensor_field_result = [
                                                        [sg.Image(r'logs/ld_tensor_field_20.png')],
                                                    ]
                    window_ld_tensor_field_result = sg.Window('Tensor Field', layout_ld_tensor_field_result)
                    while True:
                        event, values = window_ld_tensor_field_result.read()
                        if event == sg.WIN_CLOSED:
                            break

    elif event == 'Type (1,1) Tensor Field':
        tensor_field_11_layout =  [
                                    [sg.Image(resPATH + r'/images4D/tensorfield_11_0.png'),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1), font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1), font=('Tahoma', 11))],
                                    [sg.Image(resPATH + r'/images4D/tensorfield_11_1.png'),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15 , 1), font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1), font=('Tahoma', 11))],
                                    [sg.Image(resPATH + r'/images4D/tensorfield_11_2.png'),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1), font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1), font=('Tahoma', 11))],
                                    [sg.Image(resPATH + r'/images4D/tensorfield_11_3.png'),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1), font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1), font=('Tahoma', 11))],

                                    [sg.Frame(layout=[
                                        [sg.Button('Calculate', button_color='purple'),
                                        sg.Image(resPATH + r'/images4D/cov_tensorfield_11.png'),
                                        sg.Text('for', font=('Verdana', 11)),
                                        sg.Image(resPATH + r'/images4D/gamma.png'),
                                        sg.InputCombo(coord_sys, default_value=coord_sys[0])]],
                                    title='Covariant Derivative', font=('Verdana', 12), expand_x=True, element_justification='center', title_location='n')],

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
                                        sg.Image(resPATH + r'/images4D/LX_tensorfield_11.png')]],
                                    title='Lie Derivative', font=('Verdana', 12), expand_x=True, element_justification='center', title_location='n')]
                                    ]
        windows_tensor_field = sg.Window('Tensor Field', tensor_field_11_layout)
        while True:
            event, values = windows_tensor_field.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            else:
                tensor_field = [[sympify(values[i+j]) for i in range(4)] for j in range(1, 21, 5)]   # Obtaining the tensor field

                # Calculation of the covariant derivative
                if event == 'Calculate':
                    index_symbol = values[22]
                    cd_tensor_field_eqn = cd_tensorfield11_ep(metric_tensor, coord_sys, tensor_field, index_symbol)
                    preview(cd_tensor_field_eqn, viewer='file', filename=r'logs/cd_tensor_field_11.png', euler=True,
                            dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                    resize_cd_image4d('Type (1,1) Tensor Field')
                    layout_cd_tensor_field_result = [
                                                        [sg.Image(r'logs/cd_tensor_field_11.png')],
                                                    ]
                    window_cd_tensor_field_result = sg.Window('Tensor Field', layout_cd_tensor_field_result)
                    while True:
                        event, values = window_cd_tensor_field_result.read()
                        if event == sg.WIN_CLOSED:
                            break

                # Calculation of the Lie derivative
                elif event == 'Calculate0':
                    X = [sympify(values[i]) for i in range(24, 32, 2)]
                    ld_tensor_field_eqn = ld_tensorfield11_ep(metric_tensor, coord_sys, tensor_field, X)
                    preview(ld_tensor_field_eqn, viewer='file', filename=r'logs/ld_tensor_field_11.png', euler=True,
                            dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                    resize_ld_image4d('Type (1,1) Tensor Field')
                    layout_ld_tensor_field_result = [
                                                        [sg.Image(r'logs/ld_tensor_field_11.png')],
                                                    ]
                    window_ld_tensor_field_result = sg.Window('Tensor Field', layout_ld_tensor_field_result)
                    while True:
                        event, values = window_ld_tensor_field_result.read()
                        if event == sg.WIN_CLOSED:
                            break
    else:
        tensor_field_02_layout =  [
                                    [sg.Image(resPATH + r'/images4D/tensorfield_02_0.png'),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1), font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1), font=('Tahoma', 11))],
                                    [sg.Image(resPATH + r'/images4D/tensorfield_02_1.png'),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15 , 1), font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1), font=('Tahoma', 11))],
                                    [sg.Image(resPATH + r'/images4D/tensorfield_02_2.png'),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1), font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1), font=('Tahoma', 11))],
                                    [sg.Image(resPATH + r'/images4D/tensorfield_02_3.png'),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1),  font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1), font=('Tahoma', 11)),
                                        sg.InputText(default_text='0', size=(15, 1), font=('Tahoma', 11))],

                                    [sg.Frame(layout=[
                                        [sg.Button('Calculate', button_color='purple'),
                                        sg.Image(resPATH + r'/images4D/cov_tensorfield_02.png'),
                                        sg.Text('for', font=('Verdana', 11)),
                                        sg.Image(resPATH + r'/images4D/gamma.png'),
                                        sg.InputCombo(coord_sys, default_value=coord_sys[0])]],
                                    title='Covariant Derivative', font=('Verdana', 12), expand_x=True, element_justification='center', title_location='n')],

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
                                        sg.Image(resPATH + r'/images4D/LX_tensorfield_02.png')]],
                                    title='Lie Derivative', font=('Verdana', 12), expand_x=True, element_justification='center', title_location='n')]
                                    ]
        windows_tensor_field = sg.Window('Tensor Field', tensor_field_02_layout)
        while True:
            event, values = windows_tensor_field.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            else:
                tensor_field = [[sympify(values[i+j]) for i in range(4)] for j in range(1, 21, 5)]   # Obtaining the tensor field

                # Calculation of the covariant derivative
                if event == 'Calculate':
                    index_symbol = values[22]
                    cd_tensor_field_eqn = cd_tensorfield02_ep(metric_tensor, coord_sys, tensor_field, index_symbol)
                    preview(cd_tensor_field_eqn, viewer='file', filename=r'logs/cd_tensor_field_02.png', euler=True,
                            dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                    resize_cd_image4d('Type (0,2) Tensor Field')
                    layout_cd_tensor_field_result = [
                                                        [sg.Image(r'logs/cd_tensor_field_02.png')],
                                                    ]
                    window_cd_tensor_field_result = sg.Window('Tensor Field', layout_cd_tensor_field_result)
                    while True:
                        event, values = window_cd_tensor_field_result.read()
                        if event == sg.WIN_CLOSED:
                            break

                # Calculation of the Lie derivative
                elif event == 'Calculate0':
                    X = [sympify(values[i]) for i in range(24, 32, 2)]
                    ld_tensor_field_eqn = ld_tensorfield02_ep(metric_tensor, coord_sys, tensor_field, X)
                    preview(ld_tensor_field_eqn, viewer='file', filename=r'logs/ld_tensor_field_02.png', euler=True,
                            dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                    resize_ld_image4d('Type (0,2) Tensor Field')
                    layout_ld_tensor_field_result = [
                                                        [sg.Image(r'logs/ld_tensor_field_02.png')],
                                                    ]
                    window_ld_tensor_field_result = sg.Window('Tensor Field', layout_ld_tensor_field_result)
                    while True:
                        event, values = window_ld_tensor_field_result.read()
                        if event == sg.WIN_CLOSED:
                            break
