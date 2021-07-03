################### GUI - COVARIANT DERIVATIVE ###################


import PySimpleGUI as sg
from sympy import preview, sympify

from Equations.cov_derv_eqn_prod import *
from Display.image_resizer import re_size_cd_image


################### COVARIANT DERIVATIVE - 4D ###################


def gui_cd_4D(diag_comp, coord_sys, desired_cd_object):
    """
    The main process of the GUI that produces the images of covariant derivatives 
    for a given metric and coordinate system (for 4D).

    Args:
        diag_comp [list]: Diagonal components of the metric tensor.
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.).
        desired_cd_object [str]: The type of the field (scalar, vector, tensorial) choosen by the user.
    """
    if desired_cd_object == 'Scalar Field':
        layout_cd_scalar_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)),
                                     sg.Image(r'Display\Input Images\cov_scalar_field.png')],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\scalar_field.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='Scalar Field', font=('Verdana', 12))],
                                    [sg.Image(r'Display\Input Images\gamma.png'),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_cd_scalar_field = sg.Window('GRTC', layout_cd_scalar_field)
        while True:
            event, values = window_cd_scalar_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                scalar_field = values[2]
                index_symbol = values[4]
                scalar_field_eqn = cd_scalar_field_eqn_producer(coord_sys, scalar_field, index_symbol)
                preview(scalar_field_eqn, viewer='file', filename=r'Display\Output Images\cd_scalar_field.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_cd_image(desired_cd_object)
                layout_cd_scalar_field_result = [
                                                [sg.Image(r'Display\Output Images\cd_scalar_field.png')],
                                                ]
                window_cd_scalar_field_result = sg.Window('GRTC', layout_cd_scalar_field_result)
                while True:
                    event, values = window_cd_scalar_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
                    
    elif desired_cd_object == 'Type (1,0) Vector Field':
        layout_cd_vector_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)), 
                                     sg.Image(r'Display\Input Images\cov_V_10.png')],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\vector_field_10_0.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\vector_field_10_1.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\vector_field_10_2.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\vector_field_10_3.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='Type (1,0) Vector Field', font=('Verdana', 12))],
                                    [sg.Image(r'Display\Input Images\gamma.png'),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_cd_vector_field = sg.Window('GRTC', layout_cd_vector_field)
        while True:
            event, values = window_cd_vector_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                vector_field = [sympify(values[i]) for i in range(2, 10, 2)]
                index_symbol = values[10] 
                vector_field_10_eqn = cd_vector_field_eqn_producer(diag_comp, coord_sys, vector_field, 'u', index_symbol) 
                preview(vector_field_10_eqn, viewer='file', filename=r'Display\Output Images\cd_vector_field_10.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_cd_image(desired_cd_object)
                layout_cd_vector_field_result = [
                                                [sg.Image(r'Display\Output Images\cd_vector_field_10.png')],
                                                ]
                window_cd_vector_field_result = sg.Window('GRTC', layout_cd_vector_field_result)
                while True:
                    event, values = window_cd_vector_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
                    
    elif desired_cd_object == 'Type (0,1) Vector Field':
        layout_cd_vector_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)),
                                     sg.Image(r'Display\Input Images\cov_V_01.png')],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\vector_field_01_0.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\vector_field_01_1.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\vector_field_01_2.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\vector_field_01_3.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='Type (0,1) Vector Field', font=('Verdana', 12))],
                                    [sg.Image(r'Display\Input Images\gamma.png'),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_cd_vector_field = sg.Window('GRTC', layout_cd_vector_field)
        while True:
            event, values = window_cd_vector_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                vector_field = [sympify(values[i]) for i in range(2, 10, 2)]
                index_symbol = values[10] 
                vector_field_01_eqn = cd_vector_field_eqn_producer(diag_comp, coord_sys, vector_field, 'd', index_symbol) 
                preview(vector_field_01_eqn, viewer='file', filename=r'Display\Output Images\cd_vector_field_01.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_cd_image(desired_cd_object)
                layout_cd_vector_field_result = [
                                                [sg.Image(r'Display\Output Images\cd_vector_field_01.png')],
                                                ]
                window_cd_vector_field_result = sg.Window('GRTC', layout_cd_vector_field_result)
                while True:
                    event, values = window_cd_vector_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
                    
    elif desired_cd_object == 'Type (2,0) Tensor Field':
        layout_cd_tensor_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)),
                                     sg.Image(r'Display\Input Images\cov_T_20.png')],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\tensor_field_20_0.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\tensor_field_20_1.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15 , 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\tensor_field_20_2.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\tensor_field_20_3.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))]], title='Type (2,0) Tensor Field', font=('Verdana', 12))],
                                    [sg.Image(r'Display\Input Images\gamma.png'),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_cd_tensor_field = sg.Window('GRTC', layout_cd_tensor_field)
        while True:
            event, values = window_cd_tensor_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                tensor_field = [[sympify(values[i+j]) for i in range(4)] for j in range(2, 22, 5)]
                index_symbol = values[22]
                tensor_field_20_eqn = cd_tensor_field_eqn_producer(diag_comp, coord_sys, tensor_field, 'uu', index_symbol)
                preview(tensor_field_20_eqn, viewer='file', filename=r'Display\Output Images\cd_tensor_field_20.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_cd_image(desired_cd_object)
                layout_cd_tensor_field_result = [
                                                [sg.Image(r'Display\Output Images\cd_tensor_field_20.png')],
                                                ]
                window_cd_tensor_field_result = sg.Window('GRTC', layout_cd_tensor_field_result)
                while True:
                    event, values = window_cd_tensor_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
        
    elif desired_cd_object == 'Type (1,1) Tensor Field':
        layout_cd_tensor_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)),
                                     sg.Image(r'Display\Input Images\cov_T_11.png')],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\tensor_field_11_0.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\tensor_field_11_1.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15 , 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\tensor_field_11_2.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\tensor_field_11_3.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))]], title='Type (1,1) Tensor Field', font=('Verdana', 12))],
                                    [sg.Image(r'Display\Input Images\gamma.png'),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_cd_tensor_field = sg.Window('GRTC', layout_cd_tensor_field)
        while True:
            event, values = window_cd_tensor_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                tensor_field = [[sympify(values[i+j]) for i in range(4)] for j in range(2, 22, 5)]
                index_symbol = values[22]
                tensor_field_11_eqn = cd_tensor_field_eqn_producer(diag_comp, coord_sys, tensor_field, 'ud', index_symbol)
                preview(tensor_field_11_eqn, viewer='file', filename=r'Display\Output Images\cd_tensor_field_11.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_cd_image(desired_cd_object)
                layout_cd_tensor_field_result = [
                                                [sg.Image(r'Display\Output Images\cd_tensor_field_11.png')],
                                                ]
                window_cd_tensor_field_result = sg.Window('GRTC', layout_cd_tensor_field_result)
                while True:
                    event, values = window_cd_tensor_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
                    
    elif desired_cd_object == 'Type (0,2) Tensor Field':
        layout_cd_tensor_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)),
                                     sg.Image(r'Display\Input Images\cov_T_02.png')],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\tensor_field_02_0.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\tensor_field_02_1.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15 , 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\tensor_field_02_2.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\tensor_field_02_3.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))]], title='Type (0,2) Tensor Field', font=('Verdana', 12))],
                                    [sg.Image(r'Display\Input Images\gamma.png'),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_cd_tensor_field = sg.Window('GRTC', layout_cd_tensor_field)
        while True:
            event, values = window_cd_tensor_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                tensor_field = [[sympify(values[i+j]) for i in range(4)] for j in range(2, 22, 5)]
                index_symbol = values[22]
                tensor_field_02_eqn = cd_tensor_field_eqn_producer(diag_comp, coord_sys, tensor_field, 'dd', index_symbol)
                preview(tensor_field_02_eqn, viewer='file', filename=r'Display\Output Images\cd_tensor_field_02.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_cd_image(desired_cd_object)
                layout_cd_tensor_field_result = [
                                                [sg.Image(r'Display\Output Images\cd_tensor_field_02.png')],
                                                ]
                window_cd_tensor_field_result = sg.Window('GRTC', layout_cd_tensor_field_result)
                while True:
                    event, values = window_cd_tensor_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
        

################### COVARIANT DERIVATIVE - 3D ###################


def gui_cd_3D(diag_comp, coord_sys, desired_cd_object):
    """
    The main process of the GUI that produces the images of covariant derivatives 
    for a given metric and coordinate system in 3D.

    Args:
        diag_comp [list]: Diagonal components of the metric tensor.
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.).
        desired_cd_object [str]: The type of the field (scalar, vector, tensorial) choosen by the user.
    """
    if desired_cd_object == 'Scalar Field':
        layout_cd_scalar_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)),
                                     sg.Image(r'Display\Input Images\cov_scalar_field.png')],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\scalar_field.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='Scalar Field', font=('Verdana', 12))],
                                    [sg.Image(r'Display\Input Images\gamma.png'),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_cd_scalar_field = sg.Window('GRTC', layout_cd_scalar_field)
        while True:
            event, values = window_cd_scalar_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                scalar_field = values[2]
                index_symbol = values[4]
                scalar_field_eqn = cd_scalar_field_eqn_producer(coord_sys, scalar_field, index_symbol)
                preview(scalar_field_eqn, viewer='file', filename=r'Display\Output Images\cd_scalar_field.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_cd_image(desired_cd_object)
                layout_cd_scalar_field_result = [
                                                [sg.Image(r'Display\Output Images\cd_scalar_field.png')],
                                                ]
                window_cd_scalar_field_result = sg.Window('GRTC', layout_cd_scalar_field_result)
                while True:
                    event, values = window_cd_scalar_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
                    
    elif desired_cd_object == 'Type (1,0) Vector Field':
        layout_cd_vector_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)), 
                                     sg.Image(r'Display\Input Images\cov_V_10.png')],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\vector_field_10_0.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\vector_field_10_1.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\vector_field_10_2.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='Type (1,0) Vector Field', font=('Verdana', 12))],
                                    [sg.Image(r'Display\Input Images\gamma.png'),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_cd_vector_field = sg.Window('GRTC', layout_cd_vector_field)
        while True:
            event, values = window_cd_vector_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                vector_field = [sympify(values[i]) for i in range(2, 8, 2)]
                index_symbol = values[8] 
                vector_field_10_eqn = cd_vector_field_eqn_producer(diag_comp, coord_sys, vector_field, 'u', index_symbol) 
                preview(vector_field_10_eqn, viewer='file', filename=r'Display\Output Images\cd_vector_field_10.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_cd_image(desired_cd_object)
                layout_cd_vector_field_result = [
                                                [sg.Image(r'Display\Output Images\cd_vector_field_10.png')],
                                                ]
                window_cd_vector_field_result = sg.Window('GRTC', layout_cd_vector_field_result)
                while True:
                    event, values = window_cd_vector_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
                    
    elif desired_cd_object == 'Type (0,1) Vector Field':
        layout_cd_vector_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)),
                                     sg.Image(r'Display\Input Images\cov_V_01.png')],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\vector_field_01_0.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\vector_field_01_1.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\vector_field_01_2.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='Type (0,1) Vector Field', font=('Verdana', 12))],
                                    [sg.Image(r'Display\Input Images\gamma.png'),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_cd_vector_field = sg.Window('GRTC', layout_cd_vector_field)
        while True:
            event, values = window_cd_vector_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                vector_field = [sympify(values[i]) for i in range(2, 8, 2)]
                index_symbol = values[8] 
                vector_field_01_eqn = cd_vector_field_eqn_producer(diag_comp, coord_sys, vector_field, 'd', index_symbol) 
                preview(vector_field_01_eqn, viewer='file', filename=r'Display\Output Images\cd_vector_field_01.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_cd_image(desired_cd_object)
                layout_cd_vector_field_result = [
                                                [sg.Image(r'Display\Output Images\cd_vector_field_01.png')],
                                                ]
                window_cd_vector_field_result = sg.Window('GRTC', layout_cd_vector_field_result)
                while True:
                    event, values = window_cd_vector_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
                    
    elif desired_cd_object == 'Type (2,0) Tensor Field':
        layout_cd_tensor_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)),
                                     sg.Image(r'Display\Input Images\cov_T_20.png')],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\tensor_field_20_0.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\tensor_field_20_1.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)),  
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\tensor_field_20_2.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))]], title='Type (2,0) Tensor Field', font=('Verdana', 12))],
                                    [sg.Image(r'Display\Input Images\gamma.png'),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_cd_tensor_field = sg.Window('GRTC', layout_cd_tensor_field)
        while True:
            event, values = window_cd_tensor_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                tensor_field = [[sympify(values[i+j]) for i in range(3)] for j in range(2, 14, 4)]
                index_symbol = values[14]
                tensor_field_20_eqn = cd_tensor_field_eqn_producer(diag_comp, coord_sys, tensor_field, 'uu', index_symbol)
                preview(tensor_field_20_eqn, viewer='file', filename=r'Display\Output Images\cd_tensor_field_20.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_cd_image(desired_cd_object)
                layout_cd_tensor_field_result = [
                                                [sg.Image(r'Display\Output Images\cd_tensor_field_20.png')],
                                                ]
                window_cd_tensor_field_result = sg.Window('GRTC', layout_cd_tensor_field_result)
                while True:
                    event, values = window_cd_tensor_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
        
    elif desired_cd_object == 'Type (1,1) Tensor Field':
        layout_cd_tensor_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)),
                                     sg.Image(r'Display\Input Images\cov_T_11.png')],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\tensor_field_11_0.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)),
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\tensor_field_11_1.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\tensor_field_11_2.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)),
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))]], title='Type (1,1) Tensor Field', font=('Verdana', 12))],
                                    [sg.Image(r'Display\Input Images\gamma.png'),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_cd_tensor_field = sg.Window('GRTC', layout_cd_tensor_field)
        while True:
            event, values = window_cd_tensor_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                tensor_field = [[sympify(values[i+j]) for i in range(3)] for j in range(2, 14, 4)]
                index_symbol = values[14]
                tensor_field_11_eqn = cd_tensor_field_eqn_producer(diag_comp, coord_sys, tensor_field, 'ud', index_symbol)
                preview(tensor_field_11_eqn, viewer='file', filename=r'Display\Output Images\cd_tensor_field_11.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_cd_image(desired_cd_object)
                layout_cd_tensor_field_result = [
                                                [sg.Image(r'Display\Output Images\cd_tensor_field_11.png')],
                                                ]
                window_cd_tensor_field_result = sg.Window('GRTC', layout_cd_tensor_field_result)
                while True:
                    event, values = window_cd_tensor_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
                    
    elif desired_cd_object == 'Type (0,2) Tensor Field':
        layout_cd_tensor_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)),
                                     sg.Image(r'Display\Input Images\cov_T_02.png')],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\tensor_field_02_0.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)),
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\tensor_field_02_1.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\tensor_field_02_2.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)),  
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))]], title='Type (0,2) Tensor Field', font=('Verdana', 12))],
                                    [sg.Image(r'Display\Input Images\gamma.png'),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_cd_tensor_field = sg.Window('GRTC', layout_cd_tensor_field)
        while True:
            event, values = window_cd_tensor_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                tensor_field = [[sympify(values[i+j]) for i in range(3)] for j in range(2, 14, 4)]
                index_symbol = values[14]
                tensor_field_02_eqn = cd_tensor_field_eqn_producer(diag_comp, coord_sys, tensor_field, 'dd', index_symbol)
                preview(tensor_field_02_eqn, viewer='file', filename=r'Display\Output Images\cd_tensor_field_02.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_cd_image(desired_cd_object)
                layout_cd_tensor_field_result = [
                                                [sg.Image(r'Display\Output Images\cd_tensor_field_02.png')],
                                                ]
                window_cd_tensor_field_result = sg.Window('GRTC', layout_cd_tensor_field_result)
                while True:
                    event, values = window_cd_tensor_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
                    
############################################################################