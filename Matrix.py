from numpy import zeros, mat, transpose
x = zeros(2)
print(x)

y = mat(x)
print(y)

z = zeros((2, 2))
print(z)

z[0, 0] = 1
z[1, 1] = 1
print(z)
