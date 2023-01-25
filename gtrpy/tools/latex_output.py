def latex_output_grtensor(tensor_object, tensor_eqn):
    """
    Defining the function that opens a file and saves the LaTeX output of
    operations on tensors of GTR.

    Args:
        tensor_object [str]: The name of the grtensor object (metric tensor, Riemann tensor, etc.)
        latex_eqn     [str]: Tensor equation in the LaTeX form
    """
    if tensor_object == 'Metric Tensor':
        file = open('logs/metric_tensor.txt', 'w')
    if tensor_object == 'Inverse Metric Tensor':
        file = open('logs/inverse_metric_tensor.txt', 'w')
    if tensor_object == 'Christoffel Symbol':
        file = open('logs/christoffel_symbol.txt', 'w')
    if tensor_object == 'Riemann Tensor':
        file = open('logs/riemann_tensor.txt', 'w')
    if tensor_object == 'Weyl Tensor':
        file = open('logs/weyl_tensor.txt', 'w')
    if tensor_object == 'Ricci Tensor':
        file = open('logs/ricci_tensor.txt', 'w')
    if tensor_object == 'Traceless Ricci Tensor':
        file = open('logs/traceless_ricci_tensor.txt', 'w')
    if tensor_object == 'Einstein Tensor':
        file = open('logs/einstein_tensor.txt', 'w')
    if tensor_object == 'Ricci Scalar':
        file = open('logs/ricci_scalar.txt', 'w')
    if tensor_object == 'Kretschmann Scalar':
        file = open('logs/kretschmann_scalar.txt', 'w')
    file.write(tensor_eqn)
    file.close()


def latex_output_scalar_field(scalar_field_eqn):
    """
    Defining the function that opens a file and saves the LaTeX output of
    operations on scalar fields.
    """
    file = open('logs/scalar_field.txt', 'w')
    file.write(scalar_field_eqn)
    file.close()


def latex_output_vector_field(vector_field_eqn):
    """
    Defining the function that opens a file and saves the LaTeX output of
    operations on vector fields.
    """
    file = open('logs/vector_field.txt', 'w')
    file.write(vector_field_eqn)
    file.close()


def latex_output_tensor_field(tensor_field_eqn):
    """
    Defining the function that opens a file and saves the LaTeX output of
    operations on tensor fields.
    """
    file = open('logs/tensor_field.txt', 'w')
    file.write(tensor_field_eqn)
    file.close()
