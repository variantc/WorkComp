def test_trapezoidal_conv_rate():
    """check empirical convergence rates against the expected -2"""
    from math import exp
    v = lambda t: 3*(t**2)*exp(t**3)
    V = lambda t: exp(t**3)
    a = 1.1;    b = 1.9
    r = convergence_rates(v,V,a,b,14)
    print (r)
    tol = 0.01
    msg = str(r[-4:])   # show last 4 estimated rates
    assert(abs(r[-1])-2) < tol, msg
