################### GUI - GENERAL RELATIVITY - TENSORS ###################


import PySimpleGUI as sg
from sympy import preview

from Equations.GR_tensors_eqn_prod import *
from Display.image_resizer import re_size_tensor_image, re_size_tensor_component_image


# Turning tensor types into strings in terms of 'u' and 'd'
type_dict = {
            '(0,2)':'dd', '(1,1)':'ud', '(2,0)':'uu',
            '(0,3)':'ddd', '(1,2)':'udd', '(2,1)':'uud','(3,0)':'uuu',
            '(0,4)':'dddd', '(1,3)':'uddd', '(2,2)':'uudd', '(3,1)':'uuud', '(4,0)':'uuuu'
            }


# Tensor types
tensor_type2 = ['(0,2)', '(1,1)', '(2,0)']
tensor_type3 = ['(0,3)', '(1,2)', '(2,1)', '(3,0)']
tensor_type4 = ['(0,4)', '(1,3)', '(2,2)', '(3,1)', '(4,0)']


tensor2d = ['Metric Tensor', 'Ricci Tensor', 'Traceless Ricci Tensor', 'Einstein Tensor']
scalars = ['Ricci Scalar', 'Kretschmann Scalar']


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
    preview(tensor_equation, viewer='file', filename=r'Display\Output Images\tensor.png', euler=False,
            dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
    preview(tensor_component_equation, viewer='file', filename=r'Display\Output Images\tensor_component.png', euler=False,
            dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
    re_size_tensor_image(desired_tensor)
    re_size_tensor_component_image()
    if desired_tensor in tensor2d:  
        layout_tensor_type = [
                                [sg.Frame(layout=[
                                    [sg.Text('Tensor Type (p,q):', font=('Tahoma', 11)), 
                                     sg.InputCombo(tensor_type2, size=(10, 1), default_value='(0,2)')], 
                                    [sg.Image(r'Display\Output Images\tensor.png', key='-TENSOR-')]], title = desired_tensor, font=('Verdana', 14))],
                                [sg.Frame(layout=[
                                    [sg.Text('Tensor Component:', font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))], 
                                    [sg.Image(r'Display\Output Images\tensor_component.png', key='-TENSOR-COMP-')]], title=desired_tensor + ' Component', font=('Verdana', 14))],
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
                preview(tensor_equation, viewer='file', filename=r'Display\Output Images\tensor.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                preview(tensor_component_equation, viewer='file', filename=r'Display\Output Images\tensor_component.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_tensor_image(desired_tensor, desired_tensor_type)
                re_size_tensor_component_image()
                # updating the images with the new ones
                window_tensor_type.Element('-TENSOR-').Update(r'Display\Output Images\tensor.png')
                window_tensor_type.Element('-TENSOR-COMP-').Update(r'Display\Output Images\tensor_component.png')
    
    elif desired_tensor == 'Inverse Metric Tensor':
        layout_tensor_type = [
                                [sg.Frame(layout=[
                                    [sg.Image(r'Display\Output Images\tensor.png')]], title='Inverse Metric Tensor', font=('Verdana', 14))],
                                [sg.Frame(layout=[
                                    [sg.Text('Tensor Component:', font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Image(r'Display\Output Images\tensor_component.png', key='-TENSOR-COMP-')]], title='Inverse Metric Tensor Component', font=('Verdana', 14))],
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
                preview(tensor_component_equation, viewer='file', filename=r'Display\Output Images\tensor_component.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_tensor_component_image()
                window_tensor_type.Element('-TENSOR-COMP-').Update(r'Display\Output Images\tensor_component.png')
    
    elif desired_tensor == 'Christoffel Symbol':
        layout_tensor_type = [
                                [sg.Frame(layout=[
                                    [sg.Text('Type (p,q):', font=('Tahoma', 11)), 
                                     sg.InputCombo(tensor_type3, size=(10, 1), default_value='(1,2)', font=('Tahoma', 11))],
                                    [sg.Image(r'Display\Output Images\tensor.png', key='-TENSOR-')]], title='Christoffel Symbol', font=('Verdana', 14))],
                                [sg.Frame(layout = [
                                    [sg.Text('Component:', font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)),  
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Image(r'Display\Output Images\tensor_component.png', key='-TENSOR-COMP-')]], title='Christoffel Symbol Component', font=('Verdana', 14))],
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
                preview(tensor_equation, viewer='file', filename=r'Display\Output Images\tensor.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                preview(tensor_component_equation, viewer='file', filename=r'Display\Output Images\tensor_component.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_tensor_image(desired_tensor, desired_tensor_type)
                re_size_tensor_component_image()
                window_tensor_type.Element('-TENSOR-').Update(r'Display\Output Images\tensor.png')
                window_tensor_type.Element('-TENSOR-COMP-').Update(r'Display\Output Images\tensor_component.png') 
    
    elif desired_tensor == 'Riemann Tensor':
        layout_tensor_type = [
                                [sg.Frame(layout=[
                                    [sg.Text('Tensor Type (p,q):', font=('Tahoma', 11)), 
                                     sg.InputCombo(tensor_type4, size=(10, 1), default_value='(1,3)', font=('Tahoma', 11))],
                                    [sg.Image(r'Display\Output Images\tensor.png', key='-TENSOR-')]], title = 'Riemann Tensor', font=('Verdana', 14))],
                                [sg.Frame(layout = [
                                    [sg.Text('Tensor Component:', font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)),  
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Image(r'Display\Output Images\tensor_component.png', key='-TENSOR-COMP-')]], title='Riemann Tensor Component', font=('Verdana', 14))],
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
                preview(tensor_equation, viewer='file', filename=r'Display\Output Images\tensor.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                preview(tensor_component_equation, viewer='file', filename=r'Display\Output Images\tensor_component.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_tensor_image(desired_tensor, desired_tensor_type)
                re_size_tensor_component_image()
                window_tensor_type.Element('-TENSOR-').Update(r'Display\Output Images\tensor.png')
                window_tensor_type.Element('-TENSOR-COMP-').Update(r'Display\Output Images\tensor_component.png')
    
    elif desired_tensor == 'Weyl Tensor':
        layout_tensor_type = [
                                [sg.Frame(layout=[
                                    [sg.Text('Tensor Type (p,q):', font=('Tahoma', 11)), 
                                     sg.InputCombo(tensor_type4, size=(10, 1), default_value='(0,4)', font=('Tahoma', 11))],
                                    [sg.Image(r'Display\Output Images\tensor.png', key='-TENSOR-')]], title='Weyl Tensor', font=('Verdana', 14))],
                                [sg.Frame(layout=[
                                    [sg.Text('Tensor Component:', font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)),  
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)), 
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Image(r'Display\Output Images\tensor_component.png', key='-TENSOR-COMP-')]], title='Weyl Tensor Component', font=('Verdana', 14))],
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
                preview(tensor_equation, viewer='file', filename=r'Display\Output Images\tensor.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                preview(tensor_component_equation, viewer='file', filename=r'Display\Output Images\tensor_component.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                re_size_tensor_image(desired_tensor, desired_tensor_type)
                re_size_tensor_component_image()
                window_tensor_type.Element('-TENSOR-').Update(r'Display\Output Images\tensor.png')
                window_tensor_type.Element('-TENSOR-COMP-').Update(r'Display\Output Images\tensor_component.png')
    
    elif desired_tensor in scalars:
        layout_tensor_type = [
                                [sg.Frame(layout=[[sg.Image(r'Display\Output Images\tensor.png', key='-TENSOR-')]], title=desired_tensor, font=('Verdana', 14))]
                            ]
        window_tensor_type = sg.Window('GRTC', layout_tensor_type)
        while True:
            event, values = window_tensor_type.read()
            if event == sg.WIN_CLOSED:
                break    
            
############################################################################