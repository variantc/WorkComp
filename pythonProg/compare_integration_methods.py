from trapezoidal import trapezoidal
from midpoint import midpoint
from math import exp

g = lambda y: 6*y-4
a = 1.2
b = 4.4
print ('     n       midpoint        trapezoidal')
for i in range(1,21):
    n = 2**i
    m = midpoint(g,a,b,n)
    t = trapezoidal(g,a,b,n)
    print('%7d %.16f %.16f' %(n,m,t))
