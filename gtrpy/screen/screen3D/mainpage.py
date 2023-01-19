import importlib
import PySimpleGUI as sg

from sympy import symbols, sympify

from gtrpy.screen.grtensorsGUI import grtensors_gui
from gtrpy.screen.screen3D.coordinates import coordinates3d
from gtrpy.screen.screen3D.scalarfieldGUI import *
from gtrpy.screen.screen3D.vectorfieldGUI import *
from gtrpy.screen.screen3D.tensorfieldGUI import *

# ========== INPUT VARIABLES ==========

# GRTensor objects
GRTensor_objects = [
                    'Metric Tensor', 'Inverse Metric Tensor', 'Christoffel Symbol',
                    'Riemann Tensor', 'Ricci Tensor', 'Ricci Scalar', 'Weyl Tensor',
                    'Traceless Ricci Tensor', 'Einstein Tensor', 'Kretschmann Scalar'
                   ]

# Vector and Tensor Field object
vector_fields = ['Type (1,0) Vector Field', 'Type (0,1) Vector Field']
tensor_fields = ['Type (2,0) Tensor Field', 'Type (1,1) Tensor Field', 'Type (0,2) Tensor Field']

# Defining most commonly used coordinate system symbols
coordinate_symbols = ['t', 'x', 'y', 'z', 'r', 'v', 'r', 'theta', 'phi', 'rho', 'sigma', 'psi', 'eta', 'tau', 'xi', 'T', 'X']

# Available/Predefined Coordinate Systems
available_coord_sys = [ 'Cartesian Coordinates', 'Cylindrical Coordinates', 'Spherical Coordinates']

# Image Path
resPATH = importlib.machinery.PathFinder().find_module("gtrpy").get_filename()[:-11] + 'res'

# ========== GTRPy - MAIN PAGE ==========

def gtrpy_3d(coordinate_type='Spherical Coordinates'):
    """
    The main page of the GTRPy, for the case of 3D

    Args:
        coordinate_type (str, optional): The name of the coordinate. Defaults to 'Spherical Coordinates'
    """
    new_coordinate = coordinates3d(coordinate_type)
    new_metric_tensor = new_coordinate[0]  # the new metric choosen by the user
    new_coord_sys = new_coordinate[1]      # the new coordinate system that accompanies the metric tensor

    GRTensors_col1 = [
                        [sg.Button('Metric Tensor', button_color='purple', size=(20, 1)),
                            sg.Image(resPATH + r'/images3D/metrictensor.png')],
                        [sg.Button('Inverse Metric Tensor', button_color='purple', size=(20, 1)),
                            sg.Image(resPATH + r'/images3D/inversemetrictensor.png')],
                        [sg.Button('Christoffel Symbol', button_color='purple', size=(20, 1)),
                            sg.Image(resPATH + r'/images3D/chrissymbol.png')],
                        [sg.Button('Riemann Tensor', button_color='purple', size=(20, 1)),
                            sg.Image(resPATH + r'/images3D/riemanntensor.png')],
                        [sg.Button('Ricci Tensor', button_color='purple', size=(20, 1)),
                            sg.Image(resPATH + r'/images3D/riccitensor.png')]
                    ]

    GRTensors_col2 = [
                        [sg.Button('Ricci Scalar', button_color='purple', size=(20, 1)),
                            sg.Image(resPATH + r'/images3D/ricciscalar.png')],
                        [sg.Button('Weyl Tensor', button_color='purple', size=(20, 1)),
                            sg.Image(resPATH + r'/images3D/weyltensor.png')],
                        [sg.Button('Traceless Ricci Tensor', button_color='purple', size=(20, 1)),
                            sg.Image(resPATH + r'/images3D/tracelessriccitensor.png')],
                        [sg.Button('Einstein Tensor', button_color='purple', size=(20, 1)),
                            sg.Image(resPATH + r'/images3D/einsteintensor.png')],
                        [sg.Button('Kretschmann Scalar', button_color='purple', size=(20, 1)),
                            sg.Image(resPATH + r'/images3D/kretschmannscalar.png')]
                    ]

    Fields_col1 = [
                    [sg.Button('Scalar Field', button_color='purple', size=(20, 1)),
                        sg.Image(resPATH + r'/images3D/scalarfield.png')],
                    [sg.Button('Type (1,0) Vector Field', button_color='purple', size=(20, 1)),
                        sg.Image(resPATH + r'/images3D/vectorfield_10.png')],
                    [sg.Button('Type (0,1) Vector Field', button_color='purple', size=(20, 1)),
                        sg.Image(resPATH + r'/images3D/vectorfield_01.png')]
                    ]

    Fields_col2 = [
                    [sg.Button('Type (2,0) Tensor Field', button_color='purple', size=(20, 1)),
                        sg.Image(resPATH + r'/images3D/tensorfield_20.png')],
                    [sg.Button('Type (1,1) Tensor Field', button_color='purple', size=(20, 1)),
                        sg.Image(resPATH + r'/images3D/tensorfield_11.png')],
                    [sg.Button('Type (0,2) Tensor Field', button_color='purple', size=(20, 1)),
                        sg.Image(resPATH + r'/images3D/tensorfield_02.png')]
                ]

    GRTensors_tab = [
                        [sg.Column(GRTensors_col1),
                            sg.Column(GRTensors_col2)]
                    ]

    Fields_tab = [
                    [sg.Column(Fields_col1),
                        sg.Column(Fields_col2)]
                ]

    layout_4dim = [
                    [sg.Frame(layout=[
                        [sg.InputCombo(available_coord_sys, default_value=coordinate_type, font=('Tahoma', 11)),
                        sg.Button('Change Coordinate System', button_color='blue')]],
                    title='Predefined Coordinates', font=('Georgia', 14), expand_x=True, element_justification='center', title_location='n')],

                    [sg.Frame(layout=[
                        [sg.Image(resPATH + r'/images3D/x0.png'),
                        sg.InputCombo(coordinate_symbols, size=(6, 1), default_value=new_coord_sys[0], font=('Tahoma', 11)),
                        sg.Image(resPATH + r'/images3D/x1.png'),
                        sg.InputCombo(coordinate_symbols, size=(6, 1), default_value=new_coord_sys[1], font=('Tahoma', 11)),
                        sg.Image(resPATH + r'/images3D/x2.png'),
                        sg.InputCombo(coordinate_symbols, size=(6, 1), default_value=new_coord_sys[2], font=('Tahoma', 11))]],
                    title='Coordinate System', font=('Georgia', 14), expand_x=True, element_justification='center', title_location='n')],

                    [sg.Frame(layout = [
                        [sg.Image(resPATH + r'/images3D/g0b.png'),
                            sg.InputText(default_text=new_metric_tensor[0][0], size=(15, 1),  font=('Tahoma', 11)),
                            sg.InputText(default_text=new_metric_tensor[0][1], size=(15, 1),  font=('Tahoma', 11)),
                            sg.InputText(default_text=new_metric_tensor[0][2], size=(15, 1), font=('Tahoma', 11))],
                        [sg.Image(resPATH + r'/images3D/g1b.png'),
                            sg.InputText(default_text=new_metric_tensor[1][0], size=(15, 1),  font=('Tahoma', 11)),
                            sg.InputText(default_text=new_metric_tensor[1][1], size=(15, 1),  font=('Tahoma', 11)),
                            sg.InputText(default_text=new_metric_tensor[1][2], size=(15, 1), font=('Tahoma', 11))],
                        [sg.Image(resPATH + r'/images3D/g2b.png'),
                            sg.InputText(default_text=new_metric_tensor[2][0], size=(15, 1),  font=('Tahoma', 11)),
                            sg.InputText(default_text=new_metric_tensor[2][1], size=(15, 1),  font=('Tahoma', 11)),
                            sg.InputText(default_text=new_metric_tensor[2][2], size=(15, 1), font=('Tahoma', 11))],],
                    title='Metric Tensor', font=('Georgia', 14), expand_x=True, element_justification='center', title_location='n')],

                    [sg.Frame(layout=[
                        [sg.TabGroup([
                            [sg.Tab('GR Tensors', GRTensors_tab, font=('Georgia', 12)),
                                sg.Tab('Fields', Fields_tab, font=('Georgia', 12))]])]],
                    title = 'Operations', font=('Georgia', 14), expand_x=True, element_justification='center', title_location='n')],
                    [sg.Exit(button_color='red')]
                ]
    window_3dim = sg.Window('GTRPy', layout_4dim)
    while True:
        event, values = window_3dim.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        elif event == 'Change Coordinate System':
            window_3dim.close()
            gtrpy_3d(coordinate_type=values[0])   # new coordinates chosen by the user

        else:
            # Obtaining the metric tensor
            metric_tensor = [[sympify(values[i+j]) for i in range(3)] for j in range(8, 20, 4)]
            # Obtaining the coordinate system
            coord_sys = symbols(values[2] + ' ' + values[4] + ' ' + values[6])
            if event in GRTensor_objects:
                grtensors_gui(metric_tensor, coord_sys, tensor_object=event)

            elif event == 'Scalar Field':
                scalarfield_gui3d(coord_sys)

            elif event in vector_fields:
                vectorfield_gui3d(event, metric_tensor, coord_sys)

            elif event in tensor_fields:
                tensorfield_gui3d(event, metric_tensor, coord_sys)
