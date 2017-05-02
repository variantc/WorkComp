from numpy import linspace
import matplotlib.pyplot as plt

v0 = 5
g = 9.81
t = linspace(0,1,1000)

y = v0*t - 0.5*g*t**2

largestHeight = y[0]
for i in range(1,1000):
    if y[i] > largestHeight:
        largestHeight = y[i]

print("The largest height was %f m" %(largestHeight))

plt.plot(t,y)
plt.xlabel('t (s)')
plt.ylabel('y (m)')
plt.show()
