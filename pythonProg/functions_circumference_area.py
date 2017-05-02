from numpy import *

r = float(input("Input radius: "))

def Circum(rad):
    return 2*pi*rad

def Area(rad):
    return pi*rad**2

print("The circumference of circle with radius %0.2f m is %0.3f m" %(r,Circum(r)))
print("The area of circle with radius %0.2f m is %0.3f m^2" %(r,Area(r)))
