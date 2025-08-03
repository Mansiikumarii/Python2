import numpy as np
A = np.array([[11,12],[21,22],[31,32]])
B= np.array([[1,2],[3,4],[5,6]])
print(A[1])  # Print the second row of the array
print(A[1, 0])  # Print the element at the second row and first column
Z= np.dot(A, B.T)  # Dot product of two numpy arrays
print(Z)  # Print the result of the dot product