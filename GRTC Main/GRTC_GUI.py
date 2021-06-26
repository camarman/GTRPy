################### GRTC GUI ###################


import PySimpleGUI as sg
from GRTC_GUI_eqn_prod import *
from GRTC_GUI_image_prod import *
from sympy import sympify, symbols


# Color theme option provided by the PySimpleGUI
sg.ChangeLookAndFeel('Material1')


################### INPUT OPTIONS ###################


# Tensor Names
tensor_name = [
                'Metric Tensor', 'Inverse Metric Tensor', 'Christoffel Symbol', 'Riemann Tensor', 
                'Ricci Tensor', 'Ricci Scalar', 'Traceless Ricci Tensor', 
                'Weyl Tensor', 'Einstein Tensor', 'Kretschmann Scalar'
               ]


# Tensor types
tensor_type2 = ['(0,2)', '(1,1)', '(2,0)']
tensor_type3 = ['(0,3)', '(1,2)', '(2,1)', '(3,0)']
tensor_type4 = ['(0,4)', '(1,3)', '(2,2)', '(3,1)', '(4,0)']


# Covariant Derivative 
cd_objects = ['Scalar Field', 'Type (1,0) Vector Field', 'Type (0,1) Vector Field', 
              'Type (2,0) Tensor Field', 'Type (1,1) Tensor Field', 'Type (0,2) Tensor Field']


################### IMPORTANT VARIABLES ###################


# Turning tensor types into strings in terms of 'u' and 'd'
type_dict = {
            '(0,2)':'dd', '(1,1)':'ud', '(2,0)':'uu',
            '(0,3)':'ddd', '(1,2)':'udd', '(2,1)':'uud','(3,0)':'uuu',
            '(0,4)':'dddd', '(1,3)':'uddd', '(2,2)':'uudd', '(3,1)':'uuud', '(4,0)':'uuuu'
            }


# Classifying some of the tensors that will be used with the tensor types
tensor2d = ['Metric Tensor', 'Ricci Tensor', 'Traceless Ricci Tensor', 'Einstein Tensor']
scalars = ['Ricci Scalar', 'Kretschmann Scalar']


# Defining most commonly used coordinate system symbols
coordinates = ['t', 'x', 'y', 'z', 'r', 'theta', 'phi', 'rho']


################### TENSOR OPERATIONS ###################

 
def gui_tensor(diag_comp, coord_sys, desired_tensor):
    """
    The main process of the GUI that produces the images of tensor 
    for a given metric and coordinate system.

    Args:
        diag_comp [list]: Diagonal components of the metric tensor.
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.).
        desired_tensor [str]: Tensor chosen by the user.
    """
    tensor_equation = tensor_eqn_producer(diag_comp, coord_sys, desired_tensor)
    tensor_component_equation = tensor_component_eqn_producer(diag_comp, coord_sys, desired_tensor)
    produce_image_tensor(tensor_equation, tensor_component_equation, desired_tensor)
    if desired_tensor in tensor2d:  
        layout_tensor_type = [
                                [sg.Frame(layout=[
                                    [sg.Text('Tensor Type (p,q):', font=('Tahoma', 11)), 
                                     sg.InputCombo(tensor_type2, size=(10, 1), default_value='(0,2)')], 
                                    [sg.Image(r'GUI Tensor Images\tensor.png', key='-TENSOR-')]], title = desired_tensor, font=('Bookman', 14))],
                                [sg.Frame(layout=[
                                    [sg.Text('Tensor Component:', font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))], 
                                    [sg.Image(r'GUI Tensor Images\tensor_component.png', key='-TENSOR-COMP-')]], title=desired_tensor + ' Component', font=('Bookman', 14))],
                                [sg.Submit(button_color='blue')]
                            ]
        window_tensor_type = sg.Window('GRTC', layout_tensor_type)
        while True:
            event, values = window_tensor_type.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                desired_tensor_type = type_dict[values[0]]   # new type of the tensor
                components = [values[1], values[2]]   # the components of new tensor
                tensor_equation = tensor_eqn_producer(diag_comp, coord_sys, desired_tensor, desired_tensor_type)
                tensor_component_equation = tensor_component_eqn_producer(diag_comp, coord_sys, desired_tensor, desired_tensor_type, components)
                produce_image_tensor(tensor_equation, tensor_component_equation, desired_tensor, desired_tensor_type)
                # updating the images with the new ones
                window_tensor_type.Element('-TENSOR-').Update(r'GUI Tensor Images\tensor.png')
                window_tensor_type.Element('-TENSOR-COMP-').Update(r'GUI Tensor Images\tensor_component.png')
    
    if desired_tensor == 'Inverse Metric Tensor':
        layout_tensor_type = [
                                [sg.Frame(layout=[
                                    [sg.Image(r'GUI Tensor Images\tensor.png')]], title='Inverse Metric Tensor', font=('Bookman', 14))],
                                [sg.Frame(layout=[
                                    [sg.Text('Tensor Component:', font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Image(r'GUI Tensor Images\tensor_component.png', key='-TENSOR-COMP-')]], title='Inverse Metric Tensor Component', font=('Bookman', 14))],
                                [sg.Submit(button_color='blue')]
                             ]       
        window_tensor_type = sg.Window('GRTC', layout_tensor_type)
        while True:
            event, values = window_tensor_type.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                components = [values[1], values[2]]
                tensor_component_equation = tensor_component_eqn_producer(diag_comp, coord_sys, desired_tensor, component = components)
                preview(tensor_component_equation, viewer='file', filename=r'GUI Tensor Images\tensor_component.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_tensor_component()
                window_tensor_type.Element('-TENSOR-COMP-').Update(r'GUI Tensor Images\tensor_component.png')
    
    if desired_tensor == 'Christoffel Symbol':
        layout_tensor_type = [
                                [sg.Frame(layout=[
                                    [sg.Text('Tensor Type (p,q):', font=('Tahoma', 11)), 
                                     sg.InputCombo(tensor_type3, size=(10, 1), default_value='(1,2)', font=('Tahoma', 11))],
                                    [sg.Image(r'GUI Tensor Images\tensor.png', key='-TENSOR-')]], title='Christoffel Symbol', font=('Bookman', 14))],
                                [sg.Frame(layout = [
                                    [sg.Text('Tensor Component:', font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)),  
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Image(r'GUI Tensor Images\tensor_component.png', key='-TENSOR-COMP-')]], title='Christoffel Symbol Component', font=('Bookman', 14))],
                                [sg.Submit(button_color='blue')]
                            ]
        window_tensor_type = sg.Window('GRTC', layout_tensor_type)
        while True:
            event, values = window_tensor_type.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                desired_tensor_type = type_dict[values[0]]
                components = [values[1], values[2], values[3]]
                tensor_equation = tensor_eqn_producer(diag_comp, coord_sys, desired_tensor, desired_tensor_type)
                tensor_component_equation = tensor_component_eqn_producer(diag_comp, coord_sys, desired_tensor, desired_tensor_type, components)
                produce_image_tensor(tensor_equation, tensor_component_equation, desired_tensor)
                window_tensor_type.Element('-TENSOR-').Update(r'GUI Tensor Images\tensor.png')
                window_tensor_type.Element('-TENSOR-COMP-').Update(r'GUI Tensor Images\tensor_component.png') 
    
    if desired_tensor == 'Riemann Tensor':
        layout_tensor_type = [
                                [sg.Frame(layout=[
                                    [sg.Text('Tensor Type (p,q):', font=('Tahoma', 11)), 
                                     sg.InputCombo(tensor_type4, size=(10, 1), default_value='(1,3)', font=('Tahoma', 11))],
                                    [sg.Image(r'GUI Tensor Images\tensor.png', key='-TENSOR-')]], title = 'Riemann Tensor', font=('Bookman', 14))],
                                [sg.Frame(layout = [
                                    [sg.Text('Tensor Component:', font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)),  
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Image(r'GUI Tensor Images\tensor_component.png', key='-TENSOR-COMP-')]], title='Riemann Tensor Component', font=('Bookman', 14))],
                                [sg.Submit(button_color='blue')]
                            ]
        window_tensor_type = sg.Window('GRTC', layout_tensor_type)
        while True:
            event, values = window_tensor_type.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                desired_tensor_type = type_dict[values[0]]
                components = [values[1], values[2], values[3], values[4]]
                tensor_equation = tensor_eqn_producer(diag_comp, coord_sys, desired_tensor, desired_tensor_type)
                tensor_component_equation = tensor_component_eqn_producer(diag_comp, coord_sys, desired_tensor, desired_tensor_type, components)
                produce_image_tensor(tensor_equation, tensor_component_equation, desired_tensor)
                window_tensor_type.Element('-TENSOR-').Update(r'GUI Tensor Images\tensor.png')
                window_tensor_type.Element('-TENSOR-COMP-').Update(r'GUI Tensor Images\tensor_component.png')
    
    if desired_tensor == 'Weyl Tensor':
        layout_tensor_type = [
                                [sg.Frame(layout=[
                                    [sg.Text('Tensor Type (p,q):', font=('Tahoma', 11)), 
                                     sg.InputCombo(tensor_type4, size=(10, 1), default_value='(0,4)', font=('Tahoma', 11))],
                                    [sg.Image(r'GUI Tensor Images\tensor.png', key='-TENSOR-')]], title='Weyl Tensor', font=('Bookman', 14))],
                                [sg.Frame(layout=[
                                    [sg.Text('Tensor Component:', font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)),  
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Image(r'GUI Tensor Images\tensor_component.png', key='-TENSOR-COMP-')]], title='Weyl Tensor Component', font=('Bookman', 14))],
                                [sg.Submit(button_color='blue')]
                            ]
        window_tensor_type = sg.Window('GRTC', layout_tensor_type)
        while True:
            event, values = window_tensor_type.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                desired_tensor_type = type_dict[values[0]]
                components = [values[1], values[2], values[3], values[4]]
                tensor_equation = tensor_eqn_producer(diag_comp, coord_sys, desired_tensor, desired_tensor_type)
                tensor_component_equation = tensor_component_eqn_producer(diag_comp, coord_sys, desired_tensor, desired_tensor_type, components)
                produce_image_tensor(tensor_equation, tensor_component_equation, desired_tensor)
                window_tensor_type.Element('-TENSOR-').Update(r'GUI Tensor Images\tensor.png')
                window_tensor_type.Element('-TENSOR-COMP-').Update(r'GUI Tensor Images\tensor_component.png')
    
    if desired_tensor in scalars:
        layout_tensor_type = [
                                [sg.Frame(layout=[[sg.Image(r'GUI Tensor Images\tensor.png', key='-TENSOR-')]], title=desired_tensor, font=('Bookman', 14))]
                            ]
        window_tensor_type = sg.Window('GRTC', layout_tensor_type)
        while True:
            event, values = window_tensor_type.read()
            if event == sg.WIN_CLOSED:
                break    


################### COVARIANT DERIVATIVE OPERATIONS ###################


def gui_cd(diag_comp, coord_sys, desired_cd_object):
    """
    The main process of the GUI that produces the images of covariant derivatives 
    for a given metric and coordinate system.

    Args:
        diag_comp [list]: Diagonal components of the metric tensor.
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.).
        desired_cd_object [str]: The type of the field (scalar, vector, tensorial) choosen by the user.
    """
    if desired_cd_object == 'Scalar Field':
        layout_cd_scalar_field = [
                                    [sg.Frame(layout=[
                                        [sg.Image(r'GUI Input Images\scalar_field.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='Scalar Field', font=('Bookman', 14))],
                                    [sg.Text('Covariant Derivative Tensor Component:', font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_cd_scalar_field = sg.Window('GRTC', layout_cd_scalar_field)
        while True:
            event, values = window_cd_scalar_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                scalar_field = values[1]
                index_symbol = values[2]
                scalar_field_eqn = cd_scalar_field_eqn_producer(coord_sys, scalar_field, index_symbol)
                preview(scalar_field_eqn, viewer='file', filename=r'GUI Tensor Images\cd_scalar_field.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_cd(desired_cd_object)
                layout_cd_scalar_field_result = [
                                                [sg.Image(r'GUI Tensor Images\cd_scalar_field.png')],
                                                ]
                window_cd_scalar_field_result = sg.Window('GRTC', layout_cd_scalar_field_result)
                while True:
                    event, values = window_cd_scalar_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
                    
    if desired_cd_object == 'Type (1,0) Vector Field':
        layout_cd_vector_field = [
                                    [sg.Frame(layout=[
                                        [sg.Image(r'GUI Input Images\vector_field_10_0.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'GUI Input Images\vector_field_10_1.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'GUI Input Images\vector_field_10_2.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'GUI Input Images\vector_field_10_3.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='Type (1,0) Vector Field', font=('Bookman', 14))],
                                    [sg.Text('Covariant Derivative Tensor Component:', font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_cd_vector_field = sg.Window('GRTC', layout_cd_vector_field)
        while True:
            event, values = window_cd_vector_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                vector_field = [sympify(values[i]) for i in range(1, 9, 2)]
                index_symbol = values[8] 
                vector_field_10_eqn = cd_vector_field_eqn_producer(diag_comp, coord_sys, vector_field, 'u', index_symbol) 
                preview(vector_field_10_eqn, viewer='file', filename=r'GUI Tensor Images\cd_vector_field_10.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_cd(desired_cd_object)
                layout_cd_vector_field_result = [
                                                [sg.Image(r'GUI Tensor Images\cd_vector_field_10.png')],
                                                ]
                window_cd_vector_field_result = sg.Window('GRTC', layout_cd_vector_field_result)
                while True:
                    event, values = window_cd_vector_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
                    
    if desired_cd_object == 'Type (0,1) Vector Field':
        layout_cd_vector_field = [
                                    [sg.Frame(layout=[
                                        [sg.Image(r'GUI Input Images\vector_field_01_0.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'GUI Input Images\vector_field_01_1.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'GUI Input Images\vector_field_01_2.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))],
                                        [sg.Image(r'GUI Input Images\vector_field_01_3.png'), 
                                         sg.InputText(default_text='', font=('Tahoma', 11))]], title='Type (0,1) Vector Field', font=('Bookman', 14))],
                                    [sg.Text('Covariant Derivative Tensor Component:', font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_cd_vector_field = sg.Window('GRTC', layout_cd_vector_field)
        while True:
            event, values = window_cd_vector_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                vector_field = [sympify(values[i]) for i in range(1, 9, 2)]
                index_symbol = values[8] 
                vector_field_01_eqn = cd_vector_field_eqn_producer(diag_comp, coord_sys, vector_field, 'd', index_symbol) 
                preview(vector_field_01_eqn, viewer='file', filename=r'GUI Tensor Images\cd_vector_field_01.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_cd(desired_cd_object)
                layout_cd_vector_field_result = [
                                                [sg.Image(r'GUI Tensor Images\cd_vector_field_01.png')],
                                                ]
                window_cd_vector_field_result = sg.Window('GRTC', layout_cd_vector_field_result)
                while True:
                    event, values = window_cd_vector_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
                    
    if desired_cd_object == 'Type (2,0) Tensor Field':
        layout_cd_tensor_field = [
                                    [sg.Frame(layout=[
                                        [sg.Image(r'GUI Input Images\tensor_field_20_0.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'GUI Input Images\tensor_field_20_1.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15 , 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'GUI Input Images\tensor_field_20_2.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'GUI Input Images\tensor_field_20_3.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))]], title='Type (2,0) Tensor Field', font=('Bookman', 14))],
                                    [sg.Text('Covariant Derivative Tensor Component:', font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_cd_tensor_field = sg.Window('GRTC', layout_cd_tensor_field)
        while True:
            event, values = window_cd_tensor_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                tensor_field = [[sympify(values[i+j]) for i in range(4)] for j in range(1, 20, 5)]
                index_symbol = values[20]
                tensor_field_20_eqn = cd_tensor_field_eqn_producer(diag_comp, coord_sys, tensor_field, 'uu', index_symbol)
                preview(tensor_field_20_eqn, viewer='file', filename=r'GUI Tensor Images\cd_tensor_field_20.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_cd(desired_cd_object)
                layout_cd_tensor_field_result = [
                                                [sg.Image(r'GUI Tensor Images\cd_tensor_field_20.png')],
                                                ]
                window_cd_tensor_field_result = sg.Window('GRTC', layout_cd_tensor_field_result)
                while True:
                    event, values = window_cd_tensor_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
        
    if desired_cd_object == 'Type (1,1) Tensor Field':
        layout_cd_tensor_field = [
                                    [sg.Frame(layout=[
                                        [sg.Image(r'GUI Input Images\tensor_field_11_0.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'GUI Input Images\tensor_field_11_1.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15 , 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'GUI Input Images\tensor_field_11_2.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'GUI Input Images\tensor_field_11_3.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))]], title='Type (1,1) Tensor Field', font=('Bookman', 14))],
                                    [sg.Text('Covariant Derivative Tensor Component:', font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_cd_tensor_field = sg.Window('GRTC', layout_cd_tensor_field)
        while True:
            event, values = window_cd_tensor_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                tensor_field = [[sympify(values[i+j]) for i in range(4)] for j in range(1, 20, 5)]
                index_symbol = values[20]
                tensor_field_11_eqn = cd_tensor_field_eqn_producer(diag_comp, coord_sys, tensor_field, 'ud', index_symbol)
                preview(tensor_field_11_eqn, viewer='file', filename=r'GUI Tensor Images\cd_tensor_field_11.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_cd(desired_cd_object)
                layout_cd_tensor_field_result = [
                                                [sg.Image(r'GUI Tensor Images\cd_tensor_field_11.png')],
                                                ]
                window_cd_tensor_field_result = sg.Window('GRTC', layout_cd_tensor_field_result)
                while True:
                    event, values = window_cd_tensor_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
                    
    if desired_cd_object == 'Type (0,2) Tensor Field':
        layout_cd_tensor_field = [
                                    [sg.Frame(layout=[
                                        [sg.Image(r'GUI Input Images\tensor_field_02_0.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'GUI Input Images\tensor_field_02_1.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15 , 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'GUI Input Images\tensor_field_02_2.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))],
                                        [sg.Image(r'GUI Input Images\tensor_field_02_3.png'), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1),  font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11)), 
                                         sg.InputText(default_text='', size=(15, 1), font=('Tahoma', 11))]], title='Type (0,2) Tensor Field', font=('Bookman', 14))],
                                    [sg.Text('Covariant Derivative Tensor Component:', font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Submit(button_color='blue')]
                                ]
        window_cd_tensor_field = sg.Window('GRTC', layout_cd_tensor_field)
        while True:
            event, values = window_cd_tensor_field.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                tensor_field = [[sympify(values[i+j]) for i in range(4)] for j in range(1, 20, 5)]
                index_symbol = values[20]
                tensor_field_02_eqn = cd_tensor_field_eqn_producer(diag_comp, coord_sys, tensor_field, 'dd', index_symbol)
                preview(tensor_field_02_eqn, viewer='file', filename=r'GUI Tensor Images\cd_tensor_field_02.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_cd(desired_cd_object)
                layout_cd_tensor_field_result = [
                                                [sg.Image(r'GUI Tensor Images\cd_tensor_field_02.png')],
                                                ]
                window_cd_tensor_field_result = sg.Window('GRTC', layout_cd_tensor_field_result)
                while True:
                    event, values = window_cd_tensor_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
        

################### GUI MAIN PAGE ###################


layout_dimension = [
                    [sg.Text('General Relativity Tensorial Calculations (GRTC)', justification='center', font=('Georgia', 14))],
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
                            [sg.Image(r'GUI Input Images\x0.png'), 
                            sg.InputCombo(coordinates, size=(6, 1), default_value='t', font=('Tahoma', 11)),
                            sg.Image(r'GUI Input Images\x1.png'), 
                            sg.InputCombo(coordinates, size=(6, 1), default_value='r', font=('Tahoma', 11)),
                            sg.Image(r'GUI Input Images\x2.png'), 
                            sg.InputCombo(coordinates, size=(6, 1), default_value='theta', font=('Tahoma', 11)),
                            sg.Image(r'GUI Input Images\x3.png'), 
                            sg.InputCombo(coordinates, size=(6, 1), default_value='phi', font=('Tahoma', 11))]], title='Coordinate System', font=('Georgia', 14))],
                        [sg.Frame(layout = [
                            [sg.Image(r'GUI Input Images\g00.png'), 
                            sg.InputText(default_text='-1',font=('Tahoma', 11))],
                            [sg.Image(r'GUI Input Images\g11.png'), 
                            sg.InputText(default_text='1', font=('Tahoma', 11))],
                            [sg.Image(r'GUI Input Images\g22.png'), 
                            sg.InputText(default_text='r**2', font=('Tahoma', 11))],
                            [sg.Image(r'GUI Input Images\g33.png'), 
                            sg.InputText(default_text='r**2*sin(theta)**2', font=('Tahoma', 11))]], title='Metric Tensor', font=('Georgia', 14))],
                        [sg.Frame(layout=[
                            [sg.Text('Tensors:', font=('Tahoma', 11)), 
                            sg.InputCombo(tensor_name, size=(20, 1), default_value='Metric Tensor', font=('Tahoma', 11)), 
                            sg.Submit(button_color='blue')],
                            [sg.Text('Covariant Derivative:', font=('Tahoma', 11)), 
                            sg.InputCombo(cd_objects, size=(20, 1), default_value='Scalar Field', font=('Tahoma', 11)), 
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
                gui_cd(diag_comp, coord_sys, desired_cd_object)
    
    elif ndim == 3:  # if the dimesion is 3
        layout_3dim = [
                        [sg.Frame(layout=[
                            [sg.Image(r'GUI Input Images\x0.png'), 
                            sg.InputCombo(coordinates, size=(6, 1), default_value='r', font=('Tahoma', 11)),
                            sg.Image(r'GUI Input Images\x1.png'), 
                            sg.InputCombo(coordinates, size=(6, 1), default_value='theta', font=('Tahoma', 11)),
                            sg.Image(r'GUI Input Images\x2.png'), 
                            sg.InputCombo(coordinates, size=(6, 1), default_value='phi', font=('Tahoma', 11))]], title='Coordinate System', font=('Georgia', 14))],
                        [sg.Frame(layout = [
                            [sg.Image(r'GUI Input Images\g00.png'), 
                            sg.InputText(default_text='1',font=('Tahoma', 11))],
                            [sg.Image(r'GUI Input Images\g11.png'), 
                            sg.InputText(default_text='r**2', font=('Tahoma', 11))],
                            [sg.Image(r'GUI Input Images\g22.png'), 
                            sg.InputText(default_text='r**2*sin(theta)**2', font=('Tahoma', 11))]], title='Metric Tensor', font=('Georgia', 14))],
                        [sg.Frame(layout=[
                            [sg.Text('Tensors:', font=('Tahoma', 11)), 
                            sg.InputCombo(tensor_name, size=(20, 1), default_value='Metric Tensor', font=('Tahoma', 11)), 
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

############################################################################
