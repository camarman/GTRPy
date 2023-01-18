def coordinates4d(coordinate_type='Spherical Coordinates'):
    """
    Producing well-known metrics and coordinate systems for a given coordinate type in 4D

    Args:
        coordinate_type [str]: The name of the coordinate (cartesian, spherical, etc.)

    Returns:
        [tuple]: Metric tensor and the coordinate system
    """
    if coordinate_type == 'Cartesian Coordinates':
        metric_tensor = [
                            ['-1', '0', '0', '0'],
                            ['0', '1', '0', '0'],
                            ['0', '0', '1', '0'],
                            ['0', '0', '0', '1']
                        ]
        coord_sys = ['t', 'x', 'y', 'z']

    elif coordinate_type == 'Cylindrical Coordinates':
        metric_tensor = [
                            ['-1', '0', '0', '0'],
                            ['0', '1', '0', '0'],
                            ['0', '0', 'r**2', '0'],
                            ['0', '0', '0', '1']
                        ]
        coord_sys = ['t', 'r', 'phi', 'z']

    elif coordinate_type == 'Spherical Coordinates':
        metric_tensor = [
                            ['-1', '0', '0', '0'],
                            ['0', '1', '0', '0'],
                            ['0', '0', 'r**2', '0'],
                            ['0', '0', '0', 'r**2*sin(theta)**2']
                        ]
        coord_sys = ['t', 'r', 'theta', 'phi']

    elif coordinate_type == 'Conform-Compactified Coordinates':
        metric_tensor = [
                            ['-1', '0', '0', '0'],
                            ['0', '1', '0', '0'],
                            ['0', '0', 'sin(xi)**2', '0'],
                            ['0', '0', '0', 'sin(xi)**2*sin(theta)**2']
                        ]
        coord_sys = ['psi', 'xi', 'theta', 'phi']

    elif coordinate_type == 'Rindler Coordinates':
        metric_tensor = [
                            ['-1/rho**2', '0', '0', '0'],
                            ['0', '1/rho**4', '0', '0'],
                            ['0', '0', '1', '0'],
                            ['0', '0', '0', '1']
                        ]
        coord_sys = ['tau', 'rho', 'y', 'z']

    elif coordinate_type == 'Schwarzschild Coordinates':
        metric_tensor = [
                            ['-(1-r_s/r)', '0', '0', '0'],
                            ['0', '(1-r_s/r)**(-1)', '0', '0'],
                            ['0', '0', 'r**2', '0'],
                            ['0', '0', '0', 'r**2*sin(theta)**2']
                        ]
        coord_sys = ['t', 'r', 'theta', 'phi']

    elif coordinate_type == 'Eddington-Finkelstein Coordinates':
        metric_tensor = [
                            ['-(1-r_s/r)', '1', '0', '0'],
                            ['1', '0', '0', '0'],
                            ['0', '0', 'r**2', '0'],
                            ['0', '0', '0', 'r**2*sin(theta)**2']
                        ]
        coord_sys = ['v', 'r', 'theta', 'phi']
    return (metric_tensor, coord_sys)
