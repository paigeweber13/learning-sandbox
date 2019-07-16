def mandelbrot_function(z: float, c: complex):
    return z**2 + c

def test_if_mandelbrot_number(c: complex, num_iterations: int, bound: int):
    """
    the higher num_iterations, the higher the confidence level. This is the
    number of z to test before stopping

    bound is the amount that the function can diverge from the original result
    while still being considered 
    """
    is_mandelbrot = True
    z = 0
    for i in range(0, num_iterations):
        # or use previous_z?
        # next_z =
        # if next_z 
        pass
    return is_mandelbrot
