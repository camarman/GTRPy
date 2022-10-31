import PySimpleGUI as sg
from equations.grtensorsEP import *
from sympy import preview

from display4D.image_resizer_grtensor import (resize_tensor_component_image,
                                              resize_tensor_image)

#---------- IMPORTANT VARIABLES ----------#


# Turning {'u','d'} tensor type notation into (p, q)
type_dict = {
    '(0,2)': 'dd', '(1,1)': 'ud', '(2,0)': 'uu',
    '(0,3)': 'ddd', '(1,2)': 'udd', '(2,1)': 'uud', '(3,0)': 'uuu',
    '(0,4)': 'dddd', '(1,3)': 'uddd', '(2,2)': 'uudd', '(3,1)': 'uuud', '(4,0)': 'uuuu'
}

# Tensor types
tensor_type2 = ['(0,2)', '(1,1)', '(2,0)']
tensor_type3 = ['(0,3)', '(1,2)', '(2,1)', '(3,0)']
tensor_type4 = ['(0,4)', '(1,3)', '(2,2)', '(3,1)', '(4,0)']

tensor_objects2d = ['Metric Tensor', 'Ricci Tensor',
                   'Traceless Ricci Tensor', 'Einstein Tensor']
scalar_objects = ['Ricci Scalar', 'Kretschmann Scalar']


def grtensors_gui(metric_tensor, coord_sys, tensor_object):
    """
    The main process of the GUI that produces the image of tensor and tensor component
    for a given metric and coordinate system

    Args:
        metric_tensor [list]: The metric tensor, provided by the user
        coord_sys [list]: The coordinate system given as a list (e.g., [t,x,y,z])
        tensor_object [str]: The name of the grtensor object (metric tensor, riemann tensor, etc.)
    """
    tensor_eqn = tensor_ep(metric_tensor, coord_sys, tensor_object)
    tensor_component_eqn = tensor_component_ep(metric_tensor, coord_sys, tensor_object)
    preview(tensor_eqn, viewer='file', filename=r'display4D/output images/tensor.png', euler=True,
            dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
    preview(tensor_component_eqn, viewer='file', filename=r'display4D/output images/tensor_component.png', euler=True,
            dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
    resize_tensor_image(tensor_object)
    resize_tensor_component_image()
    if tensor_object in tensor_objects2d:
        layout_tensor_type = [
                                [sg.Frame(layout=[
                                    [sg.Text('Tensor Type (p,q):', font=('Tahoma', 11)),
                                     sg.InputCombo(tensor_type2, size=(10, 1), default_value='(0,2)')],
                                    [sg.Image(r'display4D/output images/tensor.png', key='-TENSOR-')]], title = tensor_object, font=('Verdana', 14))],

                                [sg.Frame(layout=[
                                    [sg.Text('Tensor Component:', font=('Tahoma', 11)),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Image(r'display4D/output images/tensor_component.png', key='-TENSOR-COMP-')]], title=tensor_object + ' Component', font=('Verdana', 14))],

                                [sg.Submit(button_color='blue')]
                            ]
        window_tensor_type = sg.Window('GRTC', layout_tensor_type)
        while True:
            event, values = window_tensor_type.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                new_tensor_type = type_dict[values[0]]   # new type of the tensor
                components = [values[1], values[2]]   # the components of the new tensor
                tensor_eqn = tensor_ep(metric_tensor, coord_sys, tensor_object, new_tensor_type)
                tensor_component_eqn = tensor_component_ep(metric_tensor, coord_sys, tensor_object, new_tensor_type, components)
                preview(tensor_eqn, viewer='file', filename=r'display4D/output images/tensor.png', euler=True,
                        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                preview(tensor_component_eqn, viewer='file', filename=r'display4D/output images/tensor_component.png', euler=True,
                        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                resize_tensor_image(tensor_object, new_tensor_type)
                resize_tensor_component_image()
                # updating the images with the new ones
                window_tensor_type.Element('-TENSOR-').Update(r'display4D/output images/tensor.png')
                window_tensor_type.Element('-TENSOR-COMP-').Update(r'display4D/output images/tensor_component.png')

    elif tensor_object == 'Inverse Metric Tensor':
        layout_tensor_type = [
                                [sg.Frame(layout=[
                                    [sg.Image(r'display4D/output images/tensor.png')]], title='Inverse Metric Tensor', font=('Verdana', 14))],

                                [sg.Frame(layout=[
                                    [sg.Text('Tensor Component:', font=('Tahoma', 11)),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Image(r'display4D/output images/tensor_component.png', key='-TENSOR-COMP-')]], title='Inverse Metric Tensor Component', font=('Verdana', 14))],

                                [sg.Submit(button_color='blue')]
                             ]
        window_tensor_type = sg.Window('GRTC', layout_tensor_type)
        while True:
            event, values = window_tensor_type.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                components = [values[1], values[2]]
                tensor_component_eqn = tensor_component_ep(metric_tensor, coord_sys, tensor_object, component = components)
                preview(tensor_component_eqn, viewer='file', filename=r'display4D/output images/tensor_component.png', euler=True,
                        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                resize_tensor_component_image()
                window_tensor_type.Element('-TENSOR-COMP-').Update(r'display4D/output images/tensor_component.png')

    elif tensor_object == 'Christoffel Symbol':
        layout_tensor_type = [
                                [sg.Frame(layout=[
                                    [sg.Text('Type (p,q):', font=('Tahoma', 11)),
                                     sg.InputCombo(tensor_type3, size=(10, 1), default_value='(1,2)', font=('Tahoma', 11))],
                                    [sg.Image(r'display4D/output images/tensor.png', key='-TENSOR-')]], title='Christoffel Symbol', font=('Verdana', 14))],

                                [sg.Frame(layout = [
                                    [sg.Text('Component:', font=('Tahoma', 11)),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Image(r'display4D/output images/tensor_component.png', key='-TENSOR-COMP-')]], title='Christoffel Symbol Component', font=('Verdana', 14))],

                                [sg.Submit(button_color='blue')]
                            ]
        window_tensor_type = sg.Window('GRTC', layout_tensor_type)
        while True:
            event, values = window_tensor_type.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                new_tensor_type = type_dict[values[0]]
                components = [values[1], values[2], values[3]]
                tensor_eqn = tensor_ep(metric_tensor, coord_sys, tensor_object, new_tensor_type)
                tensor_component_eqn = tensor_component_ep(metric_tensor, coord_sys, tensor_object, new_tensor_type, components)
                preview(tensor_eqn, viewer='file', filename=r'display4D/output images/tensor.png', euler=True,
                        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                preview(tensor_component_eqn, viewer='file', filename=r'display4D/output images/tensor_component.png', euler=True,
                        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                resize_tensor_image(tensor_object, new_tensor_type)
                resize_tensor_component_image()
                window_tensor_type.Element('-TENSOR-').Update(r'display4D/output images/tensor.png')
                window_tensor_type.Element('-TENSOR-COMP-').Update(r'display4D/output images/tensor_component.png')

    elif tensor_object == 'Riemann Tensor':
        layout_tensor_type = [
                                [sg.Frame(layout=[
                                    [sg.Text('Tensor Type (p,q):', font=('Tahoma', 11)),
                                     sg.InputCombo(tensor_type4, size=(10, 1), default_value='(1,3)', font=('Tahoma', 11))],
                                    [sg.Image(r'display4D/output images/tensor.png', key='-TENSOR-')]], title = 'Riemann Tensor', font=('Verdana', 14))],

                                [sg.Frame(layout = [
                                    [sg.Text('Tensor Component:', font=('Tahoma', 11)),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Image(r'display4D/output images/tensor_component.png', key='-TENSOR-COMP-')]], title='Riemann Tensor Component', font=('Verdana', 14))],

                                [sg.Submit(button_color='blue')]
                            ]
        window_tensor_type = sg.Window('GRTC', layout_tensor_type)
        while True:
            event, values = window_tensor_type.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                new_tensor_type = type_dict[values[0]]
                components = [values[1], values[2], values[3], values[4]]
                tensor_eqn = tensor_ep(metric_tensor, coord_sys, tensor_object, new_tensor_type)
                tensor_component_eqn = tensor_component_ep(metric_tensor, coord_sys, tensor_object, new_tensor_type, components)
                preview(tensor_eqn, viewer='file', filename=r'display4D/output images/tensor.png', euler=True,
                        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                preview(tensor_component_eqn, viewer='file', filename=r'display4D/output images/tensor_component.png', euler=True,
                        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                resize_tensor_image(tensor_object, new_tensor_type)
                resize_tensor_component_image()
                window_tensor_type.Element('-TENSOR-').Update(r'display4D/output images/tensor.png')
                window_tensor_type.Element('-TENSOR-COMP-').Update(r'display4D/output images/tensor_component.png')

    elif tensor_object == 'Weyl Tensor':
        layout_tensor_type = [
                                [sg.Frame(layout=[
                                    [sg.Text('Tensor Type (p,q):', font=('Tahoma', 11)),
                                     sg.InputCombo(tensor_type4, size=(10, 1), default_value='(0,4)', font=('Tahoma', 11))],
                                    [sg.Image(r'display4D/output images/tensor.png', key='-TENSOR-')]], title='Weyl Tensor', font=('Verdana', 14))],

                                [sg.Frame(layout=[
                                    [sg.Text('Tensor Component:', font=('Tahoma', 11)),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11)),
                                     sg.InputCombo(coord_sys, size = (6,1), default_value=coord_sys[0], font=('Tahoma', 11))],
                                    [sg.Image(r'display4D/output images/tensor_component.png', key='-TENSOR-COMP-')]], title='Weyl Tensor Component', font=('Verdana', 14))],

                                [sg.Submit(button_color='blue')]
                            ]
        window_tensor_type = sg.Window('GRTC', layout_tensor_type)
        while True:
            event, values = window_tensor_type.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Submit':
                new_tensor_type = type_dict[values[0]]
                components = [values[1], values[2], values[3], values[4]]
                tensor_eqn = tensor_ep(metric_tensor, coord_sys, tensor_object, new_tensor_type)
                tensor_component_eqn = tensor_component_ep(metric_tensor, coord_sys, tensor_object, new_tensor_type, components)
                preview(tensor_eqn, viewer='file', filename=r'display4D/output images/tensor.png', euler=True,
                        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                preview(tensor_component_eqn, viewer='file', filename=r'display4D/output images/tensor_component.png', euler=True,
                        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                resize_tensor_image(tensor_object, new_tensor_type)
                resize_tensor_component_image()
                window_tensor_type.Element('-TENSOR-').Update(r'display4D/output images/tensor.png')
                window_tensor_type.Element('-TENSOR-COMP-').Update(r'display4D/output images/tensor_component.png')

    elif tensor_object in scalar_objects:
        layout_tensor_type = [
                                [sg.Frame(layout=[[sg.Image(r'display4D/output images/tensor.png', key='-TENSOR-')]], title=tensor_object, font=('Verdana', 14))]
                            ]
        window_tensor_type = sg.Window('GRTC', layout_tensor_type)
        while True:
            event, values = window_tensor_type.read()
            if event == sg.WIN_CLOSED:
                break
