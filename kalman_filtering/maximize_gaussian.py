from math import *

def f(mu, sigma2, x):
    return 2/sqrt(2.*pi*sigma2) * exp(-.5 * (x-mu)**2 / sigma2)

print f(10., 4., 10.)
