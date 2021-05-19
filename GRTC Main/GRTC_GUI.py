#### General Relativity Tensorial Calculations - Graphical User Interface (GUI) ###

import PySimpleGUI as sg
from PIL import Image
from sympy import *
from GUI_eqn_producer import tensor_producer, tensor_component_producer


# Color option of the GUI
sg.ChangeLookAndFeel('BlueMono')


# Defining some of the most common symbols in physics
G, M, m, c, a, k, r_s = symbols('G, M, m, c, a, k, r_s')
alpha, beta, gamma, delta, eta, epsilon, kappa = symbols(
    'alpha, beta, gamma, delta, eta, epsilon, kappa')
mu, nu, sigma, tau, chi, psi, omega = symbols(
    'mu, nu, sigma, tau, chi, psi, omega')


# Defining the used tensors in the GRTC
tensor = [
    'Metric Tensor', 'Inverse Metric Tensor', 'Christoffel Symbol',
    'Riemann Tensor', 'Ricci Tensor', 'Ricci Scalar',
    'Weyl Tensor', 'Traceless Ricci Tensor', 'Einstein Tensor',
    'Kretschmann Scalar'
        ]


# Defining the tensor types
tensor_type2 = ['dd', 'ud', 'uu']
tensor_type3 = ['ddd', 'udd', 'uud', 'uuu']
tensor_type4 = ['dddd', 'uddd', 'uudd', 'uuud', 'uuuu']


# Defining the tensors that will be used with the tensor types
tensor2d = ['Metric Tensor', 'Ricci Tensor',
            'Traceless Ricci Tensor', 'Einstein Tensor']
scalars = ['Ricci Scalar', 'Kretschmann Scalar']


# Defining the most common coordinate system symbols
coordinates = ['t', 'x', 'y', 'z', 'r', 'theta', 'phi', 'rho']

def re_size(xtensor, xtensor_type = ''):
    """
    Re-sizing the image of a tensor

    Args:
        xtensor [ndim-array]: The given tensor 
    """
    im = Image.open('tensor.png')
    if xtensor == 'Metric Tensor' and xtensor_type == 'ud': # for some reason this tensor looks bigger
         size = (300, 300)
    elif xtensor in tensor2d or xtensor == 'Inverse Metric Tensor':
        size = (500, 500)
    elif xtensor == 'Christoffel Symbol':
        size = (1200, 600)
    elif xtensor == 'Riemann Tensor' or xtensor == 'Weyl Tensor':
        size = (600, 600)
    elif xtensor in scalars:
        size = (500, 500)
    im.thumbnail(size, Image.ANTIALIAS)
    out_dim = im.size
    out_name = 'tensor.png'
    im.save(out_name, "PNG")
    im.close()


def re_size_component():
    """
    Re-sizing the image of the tensor component
    """
    im = Image.open('tensor_component.png')
    size = (200, 200)
    im.thumbnail(size, Image.ANTIALIAS)
    out_dim = im.size
    out_name = 'tensor_component.png'
    im.save(out_name, "PNG")
    im.close()


def gui_main_process(diag_comp, coord_sys, desired_tensor):
    """
    The main process of the GUI that processes the images for given metric, and coordinate system

    Args:
        coord_sys [symbol]: The chosen coordinate system (cartesian, spherical, etc.)
        diag_comp [list]: Diagonal components of the metric tensor
        desired_tensor [string]: The tensor that is chose by the user
    """
    tensor_equation = tensor_producer(diag_comp, coord_sys, desired_tensor)
    tensor_component_equation = tensor_component_producer(diag_comp, coord_sys, desired_tensor)
    preview(tensor_equation, viewer='file', filename='tensor.png', euler=False,
            dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 600', '-bg', 'Transparent'])
    preview(tensor_component_equation, viewer='file', filename='tensor_component.png', euler=False,
            dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 600', '-bg', 'Transparent'])
    re_size(desired_tensor)
    re_size_component()
    
    if desired_tensor in tensor2d:  # tensors with 2-dimension and has various types
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
                desired_tensor_type = values[0] # the desired new type of the tensor
                components = [values[1], values[2]] # the components of the tensor
                tensor_equation = tensor_producer(diag_comp, coord_sys, desired_tensor, desired_tensor_type)
                tensor_component_equation = tensor_component_producer(diag_comp, coord_sys, desired_tensor, components, desired_tensor_type)
                preview(tensor_equation, viewer='file', filename='tensor.png', euler=False,
                        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 600', '-bg', 'Transparent'])
                preview(tensor_component_equation, viewer='file', filename='tensor_component.png', euler=False,
                        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 600', '-bg', 'Transparent'])
                re_size(desired_tensor, desired_tensor_type)
                re_size_component()
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
                preview(tensor_equation, viewer='file', filename='tensor.png', euler=False,
                        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 600', '-bg', 'Transparent'])
                preview(tensor_component_equation, viewer='file', filename='tensor_component.png', euler=False,
                        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 600', '-bg', 'Transparent'])
                re_size(desired_tensor)
                re_size_component()
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
                preview(tensor_equation, viewer='file', filename='tensor.png', euler=False,
                        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 600', '-bg', 'Transparent'])
                preview(tensor_component_equation, viewer='file', filename='tensor_component.png', euler=False,
                        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 600', '-bg', 'Transparent'])
                re_size(desired_tensor)
                re_size_component()
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
                preview(tensor_equation, viewer='file', filename='tensor.png', euler=False,
                        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 600', '-bg', 'Transparent'])
                preview(tensor_component_equation, viewer='file', filename='tensor_component.png', euler=False,
                        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 600', '-bg', 'Transparent'])
                re_size(desired_tensor)
                re_size_component()
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
            [sg.InputCombo(tensor, size=(20, 1), default_value='Metric Tensor')],
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
        [sg.InputCombo(tensor, size=(20, 1), default_value='Metric Tensor')],
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
    


            
            
        
