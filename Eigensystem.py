from sympy import *

A = Matrix([[0, 2], [1, -3]])

print(A.eigenvals())  #returns eigenvalues and their algebraic multiplicity
print(A.eigenvects())  #returns eigenvalues, eigenvects