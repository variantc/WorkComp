def test_trapezoidal_linear():
    from trapezoidal import trapezoidal
    """Check that linear functions are integrated exactly."""
    f = lambda x: 6*x - 4
    F = lambda x: 3*x**2 - 4*x      # Anti-derivative
    a = 1.2;    b = 4.4
    expected = F(b) - F(a)
    tol = 1e-14
    for n in 2, 20,21:
        computed = trapezoidal(f,a,b,n)
        error = abs(expected - computed)
        print("error is: %g" %(error))
        success = error < tol
        print(success)
        msg = "n=%d, err=%g" %(n,error)
        assert success, msg
