def midpoint_double(f,a,b,c,d,nx,ny):
    hx = (b-a)/float(nx)
    hy = (d-c)/float(ny)
    I=0
    for i in range (nx):
        for j in range (ny):
            xi = a + hx/2 + i*hx
            yj = c + hy/2 + j*hy
            I += hx*hy*f(xi,yj)
    return I
