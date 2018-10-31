import numpy as np
from bisection import mybisection
import matplotlib.pyplot as plt

def myfunc2(x):
    return np.sin(x**2) - x + 5


# Exercise 1.3

# 1. Alter myfunc with f(x). Invoke mybisection with the interval [3.8, 6]
x1 = mybisection(myfunc2, [3.8, 6], 0.001)
print(f"Solution 1 = {x1}")

# 2. Repeat the exercise by slightly changing the initial interval as [3.8, 5.5] and
# tolerance \eps = 0.001.
x2 = mybisection(myfunc2, [3.8, 5.5], 0.001)
print(f"Solution 2 = {x2}")

# 3.Why are the two roots different? Plot the function in a range that comprises both the
# intervals i.e., 0 to 10, to explore what is happening.

x = np.linspace(0, 10, 100)
y = myfunc2(x)
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("$ \sin{x^2} - x + 5$")
plt.savefig("../plots/myfunc2.pdf")
plt.clf()

# 4. Find the roots of the equation f(x) = (x - 2)^2

def myfunc3(x):
    return (x - 2)**2

# Uncomment the following lines to run the code. 
# There is clearly no root here - the graph touches
# but does not cross the x-axis. Bisection therefore stops immediately.

x4 = mybisection(myfunc3, [0, 3], 0.001)

print(f"Solution 4 (Doesn't work!) = {x4}")

# 5. Find the roots of f(x) = tan(x) in the range [1, 2]
def myfunc4(x):
    return np.tan(x)

# Tan is a discontinuous function in this range of values.
# Hence it cannot find a root in this interval that makes
# sense...
x = np.linspace(1, 2, 1000)
y = myfunc4(x)

plt.plot(x, y)
plt.savefig("../myfunc4.pdf")
plt.clf()

x5 = mybisection(myfunc4, [1, 2], 0.001)
print(f"Solution 5 (not accurate = {x4}")
