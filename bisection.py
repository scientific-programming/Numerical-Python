import numpy as np
import matplotlib.pyplot as plt


def myfunc(x):
    """

    Returns a cubic equation

    Parameters:
    -----------
    x, float or int:
        A number

    Returns
    -------
    float:
        Returns $x^2 + (x - 2)^3 - 5

    """
    return x**2 + (x - 2)**3 - 5

def mybisection(f, interval, eps):
    """
    Performs the bisection algorithm on a function f.

    Parameters:
    -----------
    f: function
        The function to be bisected. Should return a single number.

    interval: tuple, list, nd.array
        An interval which takes two numbers [a, b]

    eps: float
        A tolerance for the error; the algorithm stops
        when abs(f(x)) < eps

    """
    try:
        a, b = interval
    except:
        raise ValueError("Interval must be a list, tuple or "
                          "NumPy array holding two values.")

    while abs(a - b) > eps:
        x = (a + b) / 2.0
        fafb = f(a) * f(x)
        if fafb < 0:
            b = x
        else:
            a = x

    return (a + b)/2.0


def run_bisection():
    a, b = 0, 3
    x = np.linspace(a, b, 100)
    y = myfunc(x)

    tols = [1e-1, 1e-2, 1e-3]
    xvals = []
    for tol in tols:
        x_sol = mybisection(myfunc, [a, b], tol)
        print(x_sol)
        xvals.append(x_sol)

    plt.plot(x, y)
    plt.axvline(x=xvals[0])
    plt.axvline(x=xvals[1])
    plt.axvline(x=xvals[2])
    plt.axhline(y=0, 'r')
    plt.savefig('myfunc.pdf')
   

run_bisection()

