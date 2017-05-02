from trapezoidal import trapezoidal

def test_trapezoidal_one_exact_result():
    """Compare on hand-computed result"""
    from math import exp
    v = lambda t: 3*(t**2)*exp(t**3)
    n = 2
    computed = trapezoidal(v,0,1,n)
    expected = 2.463742041244344
    error = abs(expected - computed)
    print(error)
    tol = 1e-14
    success = error < tol
    print(success)
    msg = "error=%g > tolerange=%g" %(error,tol)
    assert success, msg
