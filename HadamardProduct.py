import numpy as np
Y = np.array([[2,1],[1,2]])
X = np.array([[1,0],[0,1]])
Z = X*Y  # Hadamard product of two numpy arrays
print(Z)  # Print the result of the Hadamard product
M = np.dot(X, Y)  # Dot product of two numpy arrays
print(M)  # Print the result of the dot product
print(np.sin(Z) ) # Sine of each element in the Hadamard product
print(np.cos(Z) ) # Cosine of each element in the Hadamard product
print(np.tan(Z))  # Tangent of each element in the Hadamard product
print(np.sqrt(Z))  # Square root of each element in the Hadamard product
print(np.exp(Z))  # Exponential of each element in the Hadamard product
print(np.pi)  # Print the value of pi
print(np.e)  # Print the value of e (Euler's number)