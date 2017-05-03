def convergence_rates(f,F,a,b,num_experiments=14):
    from trapezoidal import trapezoidal
    from math import log
    from numpy import zeros
    expected = F(b) - F(a)
    n = zeros(num_experiments,dtype=int)
    E = zeros(num_experiments)
    r = zeros(num_experiments - 1)
    for i in range(num_experiments):
        n[i] = 2**(i+1)
        computed = trapezoidal(f,a,b,n)
        E[i] = abs(expected - computed)
        if i>0:
            r_im1 = log(E[i]/E[i-1])/log(float(n[i])/n[i-1])
            r[i-1] = float("%.2f" %r_im1)    #truncate to two d.p.
    return r
