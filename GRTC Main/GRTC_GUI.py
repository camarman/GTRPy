################### GRTC GUI ###################


import PySimpleGUI as sg
from sympy import sympify, symbols

from Display.gui_cov_derv import *
from Display.gui_GR_tensors import *
from Display.gui_lie_derv import *


# Color theme option provided by the PySimpleGUI
sg.ChangeLookAndFeel('LightGrey')


################### INPUT OPTIONS ###################


# Tensor Names
tensor_name = [
                'Metric Tensor', 'Inverse Metric Tensor', 'Christoffel Symbol', 
                'Riemann Tensor', 'Ricci Tensor', 'Ricci Scalar', 
                'Weyl Tensor', 'Traceless Ricci Tensor', 'Einstein Tensor', 
                'Kretschmann Scalar'
               ]


# Tensor types
tensor_type2 = ['(0,2)', '(1,1)', '(2,0)']
tensor_type3 = ['(0,3)', '(1,2)', '(2,1)', '(3,0)']
tensor_type4 = ['(0,4)', '(1,3)', '(2,2)', '(3,1)', '(4,0)']


# Covariant Derivative 
field_objects = [
              'Scalar Field', 'Type (1,0) Vector Field', 'Type (0,1) Vector Field', 
              'Type (2,0) Tensor Field', 'Type (1,1) Tensor Field', 'Type (0,2) Tensor Field'
            ]


# Defining most commonly used coordinate system symbols
coordinates = ['t', 'x', 'y', 'z', 'r', 'theta', 'phi', 'rho']


################### GUI MAIN PAGE ###################


layout_dimension = [
                    [sg.Text('General Relativity Tensorial Calculations (GRTC)', font=('Georgia', 14))],
                    [sg.Text('Please Enter the Dimension of the Space:', font=('Tahoma', 11)),
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
    if ndim == 4:  # if the dimesion is 4    
        layout_4dim = [
                        [sg.Frame(layout=[
                            [sg.Image(r'Display\Input Images\x0.png'), 
                            sg.InputCombo(coordinates, size=(6, 1), default_value='t', font=('Tahoma', 11)),
                            sg.Image(r'Display\Input Images\x1.png'), 
                            sg.InputCombo(coordinates, size=(6, 1), default_value='r', font=('Tahoma', 11)),
                            sg.Image(r'Display\Input Images\x2.png'), 
                            sg.InputCombo(coordinates, size=(6, 1), default_value='theta', font=('Tahoma', 11)),
                            sg.Image(r'Display\Input Images\x3.png'), 
                            sg.InputCombo(coordinates, size=(6, 1), default_value='phi', font=('Tahoma', 11))]], title='Coordinate System', font=('Georgia', 14))],
                        [sg.Frame(layout = [
                            [sg.Image(r'Display\Input Images\g00.png'), 
                            sg.InputText(default_text='-1',font=('Tahoma', 11))],
                            [sg.Image(r'Display\Input Images\g11.png'), 
                            sg.InputText(default_text='1', font=('Tahoma', 11))],
                            [sg.Image(r'Display\Input Images\g22.png'), 
                            sg.InputText(default_text='r**2', font=('Tahoma', 11))],
                            [sg.Image(r'Display\Input Images\g33.png'), 
                            sg.InputText(default_text='r**2*sin(theta)**2', font=('Tahoma', 11))]], title='Metric Tensor', font=('Georgia', 14))],
                        [sg.Frame(layout=[
                            [sg.Text('Tensors:', font=('Tahoma', 11)), 
                            sg.InputCombo(tensor_name, size=(20, 1), default_value='Metric Tensor', font=('Tahoma', 11)), 
                            sg.Submit(button_color='blue')],
                            [sg.Text('Covariant Derivative:', font=('Tahoma', 11)), 
                            sg.InputCombo(field_objects, size=(20, 1), default_value='Scalar Field', font=('Tahoma', 11)), 
                            sg.Submit(button_color='blue')],
                            [sg.Text('Lie Derivative:', font=('Tahoma', 11)), 
                            sg.InputCombo(field_objects, size=(20, 1), default_value='Scalar Field', font=('Tahoma', 11)), 
                            sg.Submit(button_color='blue')]], title='Operations', font=('Georgia', 14))],
                        [sg.Exit(button_color='red')]
                        ]
        window_4dim = sg.Window('GRTC', layout_4dim)
        while True:
            event, values = window_4dim.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break

            if event == 'Submit':   # Tensorial Operations
                diag_comp = [sympify(values[i]) for i in range(9, 17, 2)] # getting the diagonal components
                coord_sys = symbols(values[1] + ' ' + values[3] + ' ' + values[5] + ' ' + values[7]) # getting the coordinate system
                desired_tensor = values[16] # getting the desired tensor type
                gui_tensor(diag_comp, coord_sys, desired_tensor)

            if event == 'Submit0':   # Calculating the Covariant Derivative
                diag_comp = [sympify(values[i]) for i in range(9, 17, 2)] # getting the diagonal components
                coord_sys = symbols(values[1] + ' ' + values[3] + ' ' + values[5] + ' ' + values[7]) # getting the coordinate system
                desired_cd_object = values[17]
                gui_cd_4D(diag_comp, coord_sys, desired_cd_object)
                
            if event == 'Submit1':   # Calculating the Lie Derivative
                coord_sys = symbols(values[1] + ' ' + values[3] + ' ' + values[5] + ' ' + values[7]) # getting the coordinate system
                desired_ld_object = values[18]
                gui_ld_4D(coord_sys, desired_ld_object)
                
    elif ndim == 3:  # if the dimesion is 3
        layout_3dim = [
                        [sg.Frame(layout=[
                            [sg.Image(r'Display\Input Images\x0.png'), 
                            sg.InputCombo(coordinates, size=(6, 1), default_value='r', font=('Tahoma', 11)),
                            sg.Image(r'Display\Input Images\x1.png'), 
                            sg.InputCombo(coordinates, size=(6, 1), default_value='theta', font=('Tahoma', 11)),
                            sg.Image(r'Display\Input Images\x2.png'), 
                            sg.InputCombo(coordinates, size=(6, 1), default_value='phi', font=('Tahoma', 11))]], title='Coordinate System', font=('Georgia', 14))],
                        [sg.Frame(layout = [
                            [sg.Image(r'Display\Input Images\g00.png'), 
                            sg.InputText(default_text='1',font=('Tahoma', 11))],
                            [sg.Image(r'Display\Input Images\g11.png'), 
                            sg.InputText(default_text='r**2', font=('Tahoma', 11))],
                            [sg.Image(r'Display\Input Images\g22.png'), 
                            sg.InputText(default_text='r**2*sin(theta)**2', font=('Tahoma', 11))]], title='Metric Tensor', font=('Georgia', 14))],
                        [sg.Frame(layout=[
                            [sg.Text('Tensors:', font=('Tahoma', 11)), 
                            sg.InputCombo(tensor_name, size=(20, 1), default_value='Metric Tensor', font=('Tahoma', 11)), 
                            sg.Submit(button_color='blue')],
                            [sg.Text('Covariant Derivative:', font=('Tahoma', 11)), 
                            sg.InputCombo(field_objects, size=(20, 1), default_value='Scalar Field', font=('Tahoma', 11)), 
                            sg.Submit(button_color='blue')],
                            [sg.Text('Lie Derivative:', font=('Tahoma', 11)), 
                            sg.InputCombo(field_objects, size=(20, 1), default_value='Scalar Field', font=('Tahoma', 11)), 
                            sg.Submit(button_color='blue')]], title='Operations', font=('Georgia', 14))],
                        [sg.Exit(button_color='red')]
                        ]
        window_3dim = sg.Window('GRTC', layout_3dim)
        while True:
            event, values = window_3dim.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break

            if event == 'Submit':   # Tensorial Operations
                diag_comp = [sympify(values[i]) for i in range(7, 13, 2)] # getting the diagonal components
                coord_sys = symbols(values[1] + ' ' + values[3] + ' ' + values[5]) # getting the coordinate system
                desired_tensor = values[12] # getting the desired tensor type
                gui_tensor(diag_comp, coord_sys, desired_tensor)
            
            if event == 'Submit0':   # Calculating the Covariant Derivative
                diag_comp = [sympify(values[i]) for i in range(7, 13, 2)] # getting the diagonal components
                coord_sys = symbols(values[1] + ' ' + values[3] + ' ' + values[5]) # getting the coordinate system
                desired_cd_object = values[13]
                gui_cd_3D(diag_comp, coord_sys, desired_cd_object)
            
            if event == 'Submit1':   # Calculating the Lie Derivative
                coord_sys = symbols(values[1] + ' ' + values[3] + ' ' + values[5]) # getting the coordinate system
                desired_ld_object = values[14]
                gui_ld_3D(coord_sys, desired_ld_object)
            
############################################################################