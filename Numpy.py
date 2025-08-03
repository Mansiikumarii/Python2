import numpy as np
a=[1,2,3,4,5]
x = np.array(a)
print(x)  # Print the numpy array
print(x.shape)  # Print the shape of the numpy array
print(x.dtype)  # Print the data type of the numpy array
print(x[0])  # Access the first element of the numpy array
print(x[1:3])  # Access a slice of the numpy array
print(x.sum())  # Print the sum of the elements in the numpy array
print(x.mean())  # Print the mean of the elements in the numpy array
print(x.max())  # Print the maximum value in the numpy array
print(x.min())  # Print the minimum value in the numpy array
print(x.reshape(5, 1))  # Reshape the numpy array to a 5x1 array
print(x.reshape(1, 5))  # Reshape the numpy array to a
# 1x5 array
print(x.T)  # Transpose the numpy array
print(np.arange(10))  # Create an array with values from 0 to 9
print(np.__version__)
print(type(x))  # Print the type of the numpy array
select = [0,2,3,4]
print(select)
print(x.size)
print(x.ndim)  # Print the number of dimensions of the numpy array
print(x.itemsize)  # Print the size of each item in the numpy array
print(x.nbytes)  # Print the total number of bytes consumed by the numpy array
print(x.flags)  # Print the memory layout of the numpy array
print(x.tolist())  # Convert the numpy array to a list
standatd_deviation = np.std(x)  # Calculate the standard deviation of the numpy array
print(standatd_deviation)  # Print the standard deviation