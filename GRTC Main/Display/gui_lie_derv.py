################### GUI - LIE DERIVATIVE ###################


import PySimpleGUI as sg
from sympy import preview, sympify

from Equations.lie_derv_eqn_prod import *
from Display.image_resizer import re_size_ld_image


################### LIE DERIVATIVE - 4D ###################


def gui_ld_4D(coord_sys, desired_ld_object):
    """
    The main process of the GUI that produces the images of lie derivative 
    for a given metric and coordinate system in 4D.

    Args:
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.).
        desired_cd_object [str]: The type of the field (scalar, vector, tensorial) choosen by the user.
    """
    if desired_ld_object == 'Scalar Field':
        layout_ld_scalar_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)), 
                                     sg.Image(r'Display\Input Images\LX_scalar_field.png')],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\scalar_field.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='Scalar Field', font=('Verdana', 12))],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\LX0.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX1.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX2.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX3.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='X', font=('Verdana', 12))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_ld_scalar_field = sg.Window('GRTC', layout_ld_scalar_field)
        while True:
            event, values = window_ld_scalar_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                scalar_field = sympify(values[2])
                X = [sympify(values[i]) for i in range(4, 12, 2)]
                scalar_field_eqn = ld_scalar_field_eqn_producer(coord_sys, X, scalar_field)
                preview(scalar_field_eqn, viewer='file', filename=r'Display\Output Images\ld_scalar_field.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_ld_image(desired_ld_object)
                layout_ld_scalar_field_result = [
                                                [sg.Image(r'Display\Output Images\ld_scalar_field.png')],
                                                ]
                window_ld_scalar_field_result = sg.Window('GRTC', layout_ld_scalar_field_result)
                while True:
                    event, values = window_ld_scalar_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
    
    elif desired_ld_object == 'Type (1,0) Vector Field':
        layout_ld_vector_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)), 
                                     sg.Image(r'Display\Input Images\LX_V_10.png')],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\vector_field_10_0.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\vector_field_10_1.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\vector_field_10_2.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\vector_field_10_3.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='Type (1,0) Vector Field', font=('Verdana', 12))],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\LX0.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX1.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX2.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX3.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='X', font=('Verdana', 12))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_ld_vector_field = sg.Window('GRTC', layout_ld_vector_field)
        while True:
            event, values = window_ld_vector_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                vector_field = [sympify(values[i]) for i in range(2, 10, 2)]
                X = [sympify(values[i]) for i in range(10, 18, 2)]
                vector_field_10_eqn = ld_vector_field_eqn_producer(coord_sys, X, vector_field, 'u') 
                preview(vector_field_10_eqn, viewer='file', filename=r'Display\Output Images\ld_vector_field_10.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_ld_image(desired_ld_object)
                layout_ld_vector_field_result = [
                                                [sg.Image(r'Display\Output Images\ld_vector_field_10.png')],
                                                ]
                window_ld_vector_field_result = sg.Window('GRTC', layout_ld_vector_field_result)
                while True:
                    event, values = window_ld_vector_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
    
    elif desired_ld_object == 'Type (0,1) Vector Field':
        layout_ld_vector_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)), 
                                     sg.Image(r'Display\Input Images\LX_V_01.png')],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\vector_field_01_0.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\vector_field_01_1.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\vector_field_01_2.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\vector_field_01_3.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='Type (0,1) Vector Field', font=('Verdana', 12))],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\LX0.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX1.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX2.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX3.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='X', font=('Verdana', 12))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_ld_vector_field = sg.Window('GRTC', layout_ld_vector_field)
        while True:
            event, values = window_ld_vector_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                vector_field = [sympify(values[i]) for i in range(2, 10, 2)]
                X = [sympify(values[i]) for i in range(10, 18, 2)]
                vector_field_01_eqn = ld_vector_field_eqn_producer(coord_sys, X, vector_field, 'd') 
                preview(vector_field_01_eqn, viewer='file', filename=r'Display\Output Images\ld_vector_field_01.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_ld_image(desired_ld_object)
                layout_ld_vector_field_result = [
                                                [sg.Image(r'Display\Output Images\ld_vector_field_01.png')],
                                                ]
                window_ld_vector_field_result = sg.Window('GRTC', layout_ld_vector_field_result)
                while True:
                    event, values = window_ld_vector_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
                    
    elif desired_ld_object == 'Type (2,0) Tensor Field':
        layout_ld_tensor_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)),
                                     sg.Image(r'Display\Input Images\LX_T_20.png')],
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
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\LX0.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX1.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX2.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX3.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='X', font=('Verdana', 12))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_ld_tensor_field = sg.Window('GRTC', layout_ld_tensor_field)
        while True:
            event, values = window_ld_tensor_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                tensor_field = [[sympify(values[i+j]) for i in range(4)] for j in range(2, 22, 5)]
                X = [sympify(values[i]) for i in range(22, 30, 2)]
                tensor_field_20_eqn = ld_tensor_field_eqn_producer(coord_sys, X, tensor_field, 'uu')
                preview(tensor_field_20_eqn, viewer='file', filename=r'Display\Output Images\ld_tensor_field_20.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_ld_image(desired_ld_object)
                layout_ld_tensor_field_result = [
                                                [sg.Image(r'Display\Output Images\ld_tensor_field_20.png')],
                                                ]
                window_ld_tensor_field_result = sg.Window('GRTC', layout_ld_tensor_field_result)
                while True:
                    event, values = window_ld_tensor_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
    
    elif desired_ld_object == 'Type (1,1) Tensor Field':
        layout_ld_tensor_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)),
                                     sg.Image(r'Display\Input Images\LX_T_11.png')],
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
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\LX0.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX1.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX2.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX3.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='X', font=('Verdana', 12))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_ld_tensor_field = sg.Window('GRTC', layout_ld_tensor_field)
        while True:
            event, values = window_ld_tensor_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                tensor_field = [[sympify(values[i+j]) for i in range(4)] for j in range(2, 22, 5)]
                X = [sympify(values[i]) for i in range(22, 30, 2)]
                tensor_field_11_eqn = ld_tensor_field_eqn_producer(coord_sys, X, tensor_field, 'ud')
                preview(tensor_field_11_eqn, viewer='file', filename=r'Display\Output Images\ld_tensor_field_11.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_ld_image(desired_ld_object)
                layout_ld_tensor_field_result = [
                                                [sg.Image(r'Display\Output Images\ld_tensor_field_11.png')],
                                                ]
                window_ld_tensor_field_result = sg.Window('GRTC', layout_ld_tensor_field_result)
                while True:
                    event, values = window_ld_tensor_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
    
    elif desired_ld_object == 'Type (0,2) Tensor Field':
        layout_ld_tensor_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)),
                                     sg.Image(r'Display\Input Images\LX_T_02.png')],
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
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\LX0.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX1.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX2.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX3.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='X', font=('Verdana', 12))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_ld_tensor_field = sg.Window('GRTC', layout_ld_tensor_field)
        while True:
            event, values = window_ld_tensor_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                tensor_field = [[sympify(values[i+j]) for i in range(4)] for j in range(2, 22, 5)]
                X = [sympify(values[i]) for i in range(22, 30, 2)]
                tensor_field_02_eqn = ld_tensor_field_eqn_producer(coord_sys, X, tensor_field, 'dd')
                preview(tensor_field_02_eqn, viewer='file', filename=r'Display\Output Images\ld_tensor_field_02.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_ld_image(desired_ld_object)
                layout_ld_tensor_field_result = [
                                                [sg.Image(r'Display\Output Images\ld_tensor_field_02.png')],
                                                ]
                window_ld_tensor_field_result = sg.Window('GRTC', layout_ld_tensor_field_result)
                while True:
                    event, values = window_ld_tensor_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
                    
                    
################### LIE DERIVATIVE - 3D ###################


def gui_ld_3D(coord_sys, desired_ld_object):
    """
    The main process of the GUI that produces the images of lie derivative 
    for a given metric and coordinate system in 4D.

    Args:
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.).
        desired_cd_object [str]: The type of the field (scalar, vector, tensorial) choosen by the user.
    """
    if desired_ld_object == 'Scalar Field':
        layout_ld_scalar_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)), 
                                     sg.Image(r'Display\Input Images\LX_scalar_field.png')],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\scalar_field.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='Scalar Field', font=('Verdana', 12))],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\LX0.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX1.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX2.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='X', font=('Verdana', 12))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_ld_scalar_field = sg.Window('GRTC', layout_ld_scalar_field)
        while True:
            event, values = window_ld_scalar_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                scalar_field = sympify(values[2])
                X = [sympify(values[i]) for i in range(4, 10, 2)]
                scalar_field_eqn = ld_scalar_field_eqn_producer(coord_sys, X, scalar_field)
                preview(scalar_field_eqn, viewer='file', filename=r'Display\Output Images\ld_scalar_field.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_ld_image(desired_ld_object)
                layout_ld_scalar_field_result = [
                                                [sg.Image(r'Display\Output Images\ld_scalar_field.png')],
                                                ]
                window_ld_scalar_field_result = sg.Window('GRTC', layout_ld_scalar_field_result)
                while True:
                    event, values = window_ld_scalar_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
    
    elif desired_ld_object == 'Type (1,0) Vector Field':
        layout_ld_vector_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)), 
                                     sg.Image(r'Display\Input Images\LX_V_10.png')],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\vector_field_10_0.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\vector_field_10_1.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\vector_field_10_2.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='Type (1,0) Vector Field', font=('Verdana', 12))],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\LX0.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX1.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX2.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='X', font=('Verdana', 12))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_ld_vector_field = sg.Window('GRTC', layout_ld_vector_field)
        while True:
            event, values = window_ld_vector_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                vector_field = [sympify(values[i]) for i in range(2, 8, 2)]
                X = [sympify(values[i]) for i in range(8, 14, 2)]
                vector_field_10_eqn = ld_vector_field_eqn_producer(coord_sys, X, vector_field, 'u') 
                preview(vector_field_10_eqn, viewer='file', filename=r'Display\Output Images\ld_vector_field_10.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_ld_image(desired_ld_object)
                layout_ld_vector_field_result = [
                                                [sg.Image(r'Display\Output Images\ld_vector_field_10.png')],
                                                ]
                window_ld_vector_field_result = sg.Window('GRTC', layout_ld_vector_field_result)
                while True:
                    event, values = window_ld_vector_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
    
    elif desired_ld_object == 'Type (0,1) Vector Field':
        layout_ld_vector_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)), 
                                     sg.Image(r'Display\Input Images\LX_V_01.png')],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\vector_field_01_0.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\vector_field_01_1.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\vector_field_01_2.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='Type (0,1) Vector Field', font=('Verdana', 12))],
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\LX0.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX1.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX2.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='X', font=('Verdana', 12))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_ld_vector_field = sg.Window('GRTC', layout_ld_vector_field)
        while True:
            event, values = window_ld_vector_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                vector_field = [sympify(values[i]) for i in range(2, 8, 2)]
                X = [sympify(values[i]) for i in range(8, 14, 2)]
                vector_field_01_eqn = ld_vector_field_eqn_producer(coord_sys, X, vector_field, 'd') 
                preview(vector_field_01_eqn, viewer='file', filename=r'Display\Output Images\ld_vector_field_01.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_ld_image(desired_ld_object)
                layout_ld_vector_field_result = [
                                                [sg.Image(r'Display\Output Images\ld_vector_field_01.png')],
                                                ]
                window_ld_vector_field_result = sg.Window('GRTC', layout_ld_vector_field_result)
                while True:
                    event, values = window_ld_vector_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
                    
    elif desired_ld_object == 'Type (2,0) Tensor Field':
        layout_ld_tensor_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)),
                                     sg.Image(r'Display\Input Images\LX_T_20.png')],
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
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\LX0.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX1.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX2.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='X', font=('Verdana', 12))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_ld_tensor_field = sg.Window('GRTC', layout_ld_tensor_field)
        while True:
            event, values = window_ld_tensor_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                tensor_field = [[sympify(values[i+j]) for i in range(3)] for j in range(2, 14, 4)]
                X = [sympify(values[i]) for i in range(14, 20, 2)]
                tensor_field_20_eqn = ld_tensor_field_eqn_producer(coord_sys, X, tensor_field, 'uu')
                preview(tensor_field_20_eqn, viewer='file', filename=r'Display\Output Images\ld_tensor_field_20.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_ld_image(desired_ld_object)
                layout_ld_tensor_field_result = [
                                                [sg.Image(r'Display\Output Images\ld_tensor_field_20.png')],
                                                ]
                window_ld_tensor_field_result = sg.Window('GRTC', layout_ld_tensor_field_result)
                while True:
                    event, values = window_ld_tensor_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
    
    elif desired_ld_object == 'Type (1,1) Tensor Field':
        layout_ld_tensor_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)),
                                     sg.Image(r'Display\Input Images\LX_T_11.png')],
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
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\LX0.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX1.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX2.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='X', font=('Verdana', 12))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_ld_tensor_field = sg.Window('GRTC', layout_ld_tensor_field)
        while True:
            event, values = window_ld_tensor_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                tensor_field = [[sympify(values[i+j]) for i in range(3)] for j in range(2, 14, 4)]
                X = [sympify(values[i]) for i in range(14, 20, 2)]
                tensor_field_11_eqn = ld_tensor_field_eqn_producer(coord_sys, X, tensor_field, 'ud')
                preview(tensor_field_11_eqn, viewer='file', filename=r'Display\Output Images\ld_tensor_field_11.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_ld_image(desired_ld_object)
                layout_ld_tensor_field_result = [
                                                [sg.Image(r'Display\Output Images\ld_tensor_field_11.png')],
                                                ]
                window_ld_tensor_field_result = sg.Window('GRTC', layout_ld_tensor_field_result)
                while True:
                    event, values = window_ld_tensor_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
    
    elif desired_ld_object == 'Type (0,2) Tensor Field':
        layout_ld_tensor_field = [
                                    [sg.Text('Calculating', font=('Georgia', 14)),
                                     sg.Image(r'Display\Input Images\LX_T_02.png')],
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
                                    [sg.Frame(layout=[
                                        [sg.Image(r'Display\Input Images\LX0.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX1.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'Display\Input Images\LX2.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='X', font=('Verdana', 12))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_ld_tensor_field = sg.Window('GRTC', layout_ld_tensor_field)
        while True:
            event, values = window_ld_tensor_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                tensor_field = [[sympify(values[i+j]) for i in range(3)] for j in range(2, 14, 4)]
                X = [sympify(values[i]) for i in range(14, 20, 2)]
                tensor_field_02_eqn = ld_tensor_field_eqn_producer(coord_sys, X, tensor_field, 'dd')
                preview(tensor_field_02_eqn, viewer='file', filename=r'Display\Output Images\ld_tensor_field_02.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_ld_image(desired_ld_object)
                layout_ld_tensor_field_result = [
                                                [sg.Image(r'Display\Output Images\ld_tensor_field_02.png')],
                                                ]
                window_ld_tensor_field_result = sg.Window('GRTC', layout_ld_tensor_field_result)
                while True:
                    event, values = window_ld_tensor_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
                    
############################################################################