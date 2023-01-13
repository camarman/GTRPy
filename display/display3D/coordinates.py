def coordinates3d(coordinate_type='Spherical Coordinates'):
    """
    Producing well-known metrics and coordinate systems for a given coordinate type in 3D

    Args:
        coordinate_type [str]: The name of the coordinate (cartesian, spherical, etc.)

    Returns:
        [tuple]: Metric tensor and the coordinate system
    """
    if coordinate_type == 'Cartesian Coordinates':
        metric_tensor = [
                            ['1', '0', '0'],
                            ['0', '1', '0'],
                            ['0', '0', '1']
                        ]
        coord_sys = ['x', 'y', 'z']

    elif coordinate_type == 'Cylindrical Coordinates':
        metric_tensor = [
                            ['1', '0', '0'],
                            ['0', 'r**2', '0'],
                            ['0', '0', '1']
                        ]
        coord_sys = ['r', 'phi', 'z']

    elif coordinate_type == 'Spherical Coordinates':
        metric_tensor = [
                            ['1', '0', '0'],
                            ['0', 'r**2', '0'],
                            ['0', '0', 'r**2*sin(theta)**2']
                        ]
        coord_sys = ['r', 'theta', 'phi']
    return (metric_tensor, coord_sys)
