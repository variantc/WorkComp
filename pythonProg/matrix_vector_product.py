from numpy import zeros, mat, transpose

x = zeros(2)
x = mat(x)
x = transpose(x)
x[0] = 3;  x[1] = 2

A = zeros((2,2))
A = mat(A)
A[0,0] = 1; A[0,1] = 0
A[1,0] = 0; A[1,1] = 1

y = A * x
print("x = \n", x)
print("A = \n", A)
print("y = \n", y)
