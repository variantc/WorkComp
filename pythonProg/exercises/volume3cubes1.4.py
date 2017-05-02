from numpy import linspace
import matplotlib.pyplot as plt

L = linspace(1,3,1001)
V = L**3

plt.plot(L,V)
plt.xlabel("L (m)")
plt.ylabel("V (m^3)")
plt.show()
