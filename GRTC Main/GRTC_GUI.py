#### General Relativity Tensorial Calculations - Graphical User Interface (GUI) ###


import PySimpleGUI as sg
from PIL import Image
from sympy import *
from GUI_eqn_producer import *
from GRTC_image_producer import *


# Color theme option provided by the PySimpleGUI
sg.ChangeLookAndFeel('Material1')


# Defining the used tensors in the GRTC
tensor_name = ['Metric Tensor', 'Inverse Metric Tensor', 'Christoffel Symbol',
               'Riemann Tensor', 'Ricci Tensor', 'Ricci Scalar', 
               'Traceless Ricci Tensor', 'Weyl Tensor', 'Einstein Tensor',
               'Kretschmann Scalar'
               ]


# Defining the tensor types
tensor_type2 = ['dd', 'ud', 'uu']
tensor_type3 = ['ddd', 'udd', 'uud', 'uuu']
tensor_type4 = ['dddd', 'uddd', 'uudd', 'uuud', 'uuuu']


# Classifying some of the tensors that will be used with the tensor types
tensor2d = ['Metric Tensor', 'Ricci Tensor', 'Traceless Ricci Tensor', 'Einstein Tensor']
scalars = ['Ricci Scalar', 'Kretschmann Scalar']


# Defining the most commonly used coordinate system symbols
coordinates = ['t', 'x', 'y', 'z', 'r', 'theta', 'phi', 'rho']


def gui_main_process(diag_comp, coord_sys, desired_tensor):
    """
    The main process of the GUI that produces the images for a given metric and coordinate system

    Args:
        diag_comp [list]: Diagonal components of the metric tensor
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.)
        desired_tensor [str]: Tensor chosen by the user
    """
    tensor_equation = tensor_producer(diag_comp, coord_sys, desired_tensor)
    tensor_component_equation = tensor_component_producer(diag_comp, coord_sys, desired_tensor)
    produce_image(tensor_equation, tensor_component_equation, desired_tensor)
    # tensors with 2-dimension and has various types
    if desired_tensor in tensor2d:  
        layout_tensor_type = [
                                [sg.Text(desired_tensor, size=(35, 1), justification='center', font=('Inconsolota', 20), relief=sg.RELIEF_RIDGE)],
                                [sg.Text('Tensor Type:',), sg.InputCombo(tensor_type2, size=(20, 1), default_value='dd')],
                                [sg.Image('tensor.png', key='-TENSOR-')],
                                [sg.Text('Tensor Component:'), sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0]), sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0])],
                                [sg.Image('tensor_component.png', key='-TENSOR-COMP-')],
                                [sg.Submit()]
                            ]
        window_tensor_type = sg.Window('GRTC', layout_tensor_type)
        while True:
            event, values = window_tensor_type.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                desired_tensor_type = values[0] # new type of the tensor
                components = [values[1], values[2]] # the components of new tensor
                tensor_equation = tensor_producer(diag_comp, coord_sys, desired_tensor, desired_tensor_type)
                tensor_component_equation = tensor_component_producer(diag_comp, coord_sys, desired_tensor, components, desired_tensor_type)
                produce_image(tensor_equation, tensor_component_equation, desired_tensor, desired_tensor_type)
                # updating the images with the new ones
                window_tensor_type.Element('-TENSOR-').Update('tensor.png')
                window_tensor_type.Element('-TENSOR-COMP-').Update('tensor_component.png')
    
    if desired_tensor == 'Inverse Metric Tensor':
        layout_tensor_type = [
                                [sg.Text(desired_tensor, size=(35, 1), justification='center', font=('Inconsolota', 20), relief=sg.RELIEF_RIDGE)],
                                [sg.Image('tensor.png')],
                                [sg.Text('Tensor Component:'), sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0]), sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0])],
                                [sg.Image('tensor_component.png', key='-TENSOR-COMP-')],
                                [sg.Submit()]
                            ]
        window_tensor_type = sg.Window('GRTC', layout_tensor_type)
        while True:
            event, values = window_tensor_type.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                components = [values[1], values[2]]
                tensor_component_equation = tensor_component_producer(diag_comp, coord_sys, desired_tensor, components)
                preview(tensor_component_equation, viewer='file', filename='tensor_component.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 600', '-bg', 'Transparent'])
                re_size_component()
                window_tensor_type.Element('-TENSOR-COMP-').Update('tensor_component.png')
    
    if desired_tensor == 'Christoffel Symbol':
        layout_tensor_type = [
                                [sg.Text(desired_tensor, size=(35, 1), justification='center', font=('Inconsolota', 20), relief=sg.RELIEF_RIDGE)],
                                [sg.Text('Tensor Type:',), sg.InputCombo(tensor_type3, size=(20, 1), default_value='udd')],
                                [sg.Image('tensor.png', key='-TENSOR-')],
                                [sg.Text('Tensor Component:'), sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0]), sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0]),  sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0])],
                                [sg.Image('tensor_component.png', key='-TENSOR-COMP-')],
                                [sg.Submit()]
                            ]
        window_tensor_type = sg.Window('GRTC', layout_tensor_type)
        while True:
            event, values = window_tensor_type.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                desired_tensor_type = values[0]
                components = [values[1], values[2], values[3]]
                tensor_equation = tensor_producer(diag_comp, coord_sys, desired_tensor, desired_tensor_type)
                tensor_component_equation = tensor_component_producer(diag_comp, coord_sys, desired_tensor, components, desired_tensor_type)
                produce_image(tensor_equation, tensor_component_equation, desired_tensor)
                window_tensor_type.Element('-TENSOR-').Update('tensor.png')
                window_tensor_type.Element('-TENSOR-COMP-').Update('tensor_component.png') 
    
    if desired_tensor == 'Riemann Tensor':
        layout_tensor_type = [
                                [sg.Text(desired_tensor, size=(35, 1), justification='center', font=('Inconsolota', 20), relief=sg.RELIEF_RIDGE)],
                                [sg.Text('Tensor Type:',), sg.InputCombo(tensor_type4, size=(20, 1), default_value='uddd')],
                                [sg.Image('tensor.png', key='-TENSOR-')],
                                [sg.Text('Tensor Component:'), sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0]), sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0]),  sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0]), sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0])],
                                [sg.Image('tensor_component.png', key='-TENSOR-COMP-')],
                                [sg.Submit()]
                            ]
        window_tensor_type = sg.Window('GRTC', layout_tensor_type)
        while True:
            event, values = window_tensor_type.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                desired_tensor_type = values[0]
                components = [values[1], values[2], values[3], values[4]]
                tensor_equation = tensor_producer(diag_comp, coord_sys, desired_tensor, desired_tensor_type)
                tensor_component_equation = tensor_component_producer(diag_comp, coord_sys, desired_tensor, components, desired_tensor_type)
                produce_image(tensor_equation, tensor_component_equation, desired_tensor)
                window_tensor_type.Element('-TENSOR-').Update('tensor.png')
                window_tensor_type.Element('-TENSOR-COMP-').Update('tensor_component.png')
    
    if desired_tensor == 'Weyl Tensor':
        layout_tensor_type = [
                                [sg.Text(desired_tensor, size=(35, 1), justification='center', font=('Inconsolota', 20), relief=sg.RELIEF_RIDGE)],
                                [sg.Text('Tensor Type:',), sg.InputCombo(tensor_type4, size=(20, 1), default_value='dddd')],
                                [sg.Image('tensor.png', key='-TENSOR-')],
                                [sg.Text('Tensor Component:'), sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0]), sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0]),  sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0]), sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0])],
                                [sg.Image('tensor_component.png', key='-TENSOR-COMP-')],
                                [sg.Submit()]
                            ]
        window_tensor_type = sg.Window('GRTC', layout_tensor_type)
        while True:
            event, values = window_tensor_type.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                desired_tensor_type = values[0]
                components = [values[1], values[2], values[3], values[4]]
                tensor_equation = tensor_producer(diag_comp, coord_sys, desired_tensor, desired_tensor_type)
                tensor_component_equation = tensor_component_producer(diag_comp, coord_sys, desired_tensor, components, desired_tensor_type)
                produce_image(tensor_equation, tensor_component_equation, desired_tensor)
                window_tensor_type.Element('-TENSOR-').Update('tensor.png')
                window_tensor_type.Element('-TENSOR-COMP-').Update('tensor_component.png')
    
    if desired_tensor in scalars:
        layout_tensor_type = [
                                [sg.Text(desired_tensor, size=(35, 1), justification='center', font=('Inconsolota', 20), relief=sg.RELIEF_RIDGE)],
                                [sg.Image('tensor.png', key='-TENSOR-')]
                            ]
        window_tensor_type = sg.Window('GRTC', layout_tensor_type)
        while True:
            event, values = window_tensor_type.read()
            if event == sg.WIN_CLOSED:
                break    

 
# The first page of the GUI
layout_dimension = [
    [sg.Text('General Relativity Tensorial Calculations', size=(35, 1), justification='center', font=('Inconsolota', 20), relief=sg.RELIEF_RIDGE)],
    [sg.Text('Dimension of the Space: ', font=('Ariel', 10)),
     sg.InputCombo([3, 4], size=(8, 1), default_value='4')],
    [sg.Submit(), sg.Exit()]
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
            [sg.Text('General Relativity Tensorial Calculations', size=(35, 1), justification='center', font=('Inconsolota', 20), relief=sg.RELIEF_RIDGE)],
            [sg.Text('Coordinate System')],
            [sg.Image(r'GUI Images\x0.png'), sg.InputCombo(coordinates, size=(6, 1), default_value='t'),
             sg.Image(r'GUI Images\x1.png'), sg.InputCombo(coordinates, size=(6, 1), default_value='r'),
             sg.Image(r'GUI Images\x2.png'), sg.InputCombo(coordinates, size=(6, 1), default_value='theta'),
             sg.Image(r'GUI Images\x3.png'), sg.InputCombo(coordinates, size=(6, 1), default_value='phi')],
            [sg.Text('Enter the Diagonal Components of the Metric Tensor')],
            [sg.Image(r'GUI Images\g00.png'), sg.InputText(default_text='-1')],
            [sg.Image(r'GUI Images\g11.png'), sg.InputText(default_text='1')],
            [sg.Image(r'GUI Images\g22.png'), sg.InputText(default_text='r**2')],
            [sg.Image(r'GUI Images\g33.png'), sg.InputText(default_text='r**2*sin(theta)**2')],
            [sg.Text('Available Tensors')], 
            [sg.InputCombo(tensor_name, size=(20, 1), default_value='Metric Tensor')],
            [sg.Submit(), sg.Exit()]
            ]
        window_4dim = sg.Window('GRTC', layout_4dim)
        while True:
            event, values = window_4dim.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            if event == 'Submit':
                diag_comp = [sympify(values[i]) for i in range(9, 17, 2)] # getting the diagonal components
                desired_tensor = values[16] # getting the desired tensor type
                coord_sys = symbols(values[1] + ' ' + values[3] + ' ' + values[5] + ' ' + values[7]) # getting the coordinate system
                gui_main_process(diag_comp, coord_sys, desired_tensor)
                
    if ndim == 3: # if the dimension is 3
        layout_3dim = [
        [sg.Text('General Relativity Tensorial Calculations', size=(35, 1), justification='center', font=('Inconsolota', 20), relief=sg.RELIEF_RIDGE)],
        [sg.Text('Coordinate System')],
        [sg.Image(r'GUI Images\x0.png'), sg.InputCombo(coordinates, size=(6, 1), default_value='r'),
         sg.Image(r'GUI Images\x1.png'), sg.InputCombo(coordinates, size=(6, 1), default_value='theta'),
         sg.Image(r'GUI Images\x2.png'), sg.InputCombo(coordinates, size=(6, 1), default_value='phi')],
        [sg.Text('Enter the Diagonal Components of the Metric Tensor')],
        [sg.Image(r'GUI Images\g00.png'), sg.InputText(default_text='1')],
        [sg.Image(r'GUI Images\g11.png'), sg.InputText(default_text='r**2')],
        [sg.Image(r'GUI Images\g22.png'), sg.InputText(default_text='r**2*sin(theta)**2')],
        [sg.Text('Available Tensors')], 
        [sg.InputCombo(tensor_name, size=(20, 1), default_value='Metric Tensor')],
        [sg.Submit(), sg.Exit()]
        ]
        window_3dim = sg.Window('GRTC', layout_3dim)
        while True:
            event, values = window_3dim.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            if event == 'Submit':
                diag_comp = [sympify(values[i]) for i in range(7, 13, 2)] # getting the diagonal components
                desired_tensor = values[12] # getting the desired tensor type
                coord_sys = symbols(values[1] + ' ' + values[3] + ' ' + values[5]) # getting the coordinate system
                gui_main_process(diag_comp, coord_sys, desired_tensor)
