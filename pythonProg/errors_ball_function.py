# Program for computing the height of a ball in vertical motion


def y(t):
    v0 = 5                      # Initial velocity [m/s]
    g = 9.81                    # Acceleration of gravity [m/s^2]
    return v0*t - 0.5*g*t**2       # Vertical position


time = 0.6                     # Time [s]
print(y(time))
time = 0.5                     # Time [s]
print(y(time))

