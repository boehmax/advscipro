"""
A collection of simple math operations
"""
def simple_add(a, b):
    """
    Perform simple addition of two numbers.

    Parameters
    ----------
    a : int or float
        The first number.
    b : int or float
        The second number.

    Returns
    -------
    result : int or float
        The result of adding `a` and `b`.
    """
    return a + b

def simple_sub(a, b):
    """
    Perform simple subtraction of two numbers.

    Parameters
    ----------
    a : int or float
        The minuend.
    b : int or float
        The subtrahend.

    Returns
    -------
    result : int or float
        The result of subtracting `b` from `a`.
    """
    return a - b

def simple_mult(a, b):
    """
    Perform simple multiplication of two numbers.

    Parameters
    ----------
    a : int or float
        The first factor.
    b : int or float
        The second factor.

    Returns
    -------
    result : int or float
        The result of multiplying `a` and `b`.
    """
    return a * b

def simple_div(a, b):
    """
    Perform simple division of two numbers.

    Parameters
    ----------
    a : int or float
        The dividend.
    b : int or float
        The divisor (must be non-zero).

    Returns
    -------
    result : float
        The result of dividing `a` by `b`.
    """
    return a / b

def poly_first(x, a0, a1):
    """
    Evaluate a first-degree polynomial at a given point.

    Parameters
    ----------
    x : int or float
        The point at which to evaluate the polynomial.
    a0 : int or float
        The coefficient for the constant term.
    a1 : int or float
        The coefficient for the linear term.

    Returns
    -------
    result : int or float
        The value of the polynomial `a0 + a1*x`.
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """
    Evaluate a second-degree polynomial at a given point.

    Parameters
    ----------
    x : int or float
        The point at which to evaluate the polynomial.
    a0 : int or float
        The coefficient for the constant term.
    a1 : int or float
        The coefficient for the linear term.
    a2 : int or float
        The coefficient for the quadratic term.

    Returns
    -------
    result : int or float
        The value of the polynomial `a0 + a1*x + a2*x**2`.
    """
    return poly_first(x, a0, a1) + a2*(x**2)


# Feel free to expand this list with more interesting mathematical operations...
# .....
