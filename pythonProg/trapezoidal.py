def application(intFunc):
    from math import exp
    v = lambda t: 3*(t**2)*exp(t**3)
    n = int(input("n: "))
    numerical = intFunc(v, 0, 1, n)

    # Compare the exact result
    V = lambda t: exp(t**3)
    exact = V(1) - V(0)
    error = exact - numerical
    print("n=%d: %.16f, error: %g" %(n, numerical, error))

def trapezoidal(f,a,b,n):
    h = float(b-a)/n
    result = 0.5 * f(a) + 0.5 * f(b)
    for i in range (1,n):
        result += f(a+i*h)
    result *= h
    return result

def testContinue():
    inp = input("Proceed? ('q' to quit): ")
    if inp == "q" :
        return False
    else:
        return True

# run = True
# 
# while (testContinue()):
#     application()
#     # run = testContinue()
