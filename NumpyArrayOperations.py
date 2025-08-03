import numpy as np
import matplotlib.pyplot as plt
u = np.array([10,20,30])
v= np.array([5,10,15])
z = np.add(u, v)  # Add two numpy arrays
print(z)  # Print the result of the addition
c = np.subtract(u, v)  # Subtract two numpy arrays
print(c)  # Print the result of the subtraction
d = np.multiply(u, v)  # Multiply two numpy arrays
print(d)  # Print the result of the multiplication
e = np.divide(u, v)  # Divide two numpy arrays
print(e)  # Print the result of the division
f = np.dot(u, v)  # Dot product of two numpy arrays
print(f)  # Print the result of the dot product 
g = np.cross(u, v)  # Cross product of two numpy arrays
print(g)  # Print the result of the cross product
print(np.pi)  # Print the value of pi
print(np.e)  # Print the value of e (Euler's number)    
h = np.sqrt(u)  # Square root of each element in the numpy array
print(h)  # Print the square root results
i = np.exp(u)  # Exponential of each element in the numpy array
print(i)  # Print the exponential results

x = np.array([0, np.pi/2 , np.pi])
y = np.sin(x)  # Sine of each element in the numpy array
print(y)  # Print the sine results
z = np.cos(x)  # Cosine of each element in the numpy array
print(z)  # Print the cosine results
w = np.tan(x)  # Tangent of each element in the numpy array
print(w)  # Print the tangent results

# Line Space
print(np.linspace(0,2*np.pi, num=5))  # Generate 5 evenly spaced numbers between 0 and 2*pi
print(np.linspace(-2,2, num=5) ) # Generate 5 evenly spaced numbers between -2 and 2
print(np.linspace(-2,2, num=9))  # Generate 9 evenly spaced numbers between -2 and 2

y= np.sin(x)
plt.plot(x, y)  # Plot sine function
plt.title('Sine Function')  # Set the title of the plot
plt.xlabel('x')  # Set the x-axis label
plt.ylabel('sin(x)')  # Set the y-axis label
plt.grid(True)  # Enable grid on the plot
plt.show()  # Display the plot
