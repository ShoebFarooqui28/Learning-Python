import numpy as np

print("\n")

a1 = np.array([1,2,3,4])
print(a1*5) # Output: [5 10 15 20], because numpy arrays are vectorized and can perform operations on the entire array at once.
print(a1 * 2) # Output: [2 4 6 8]

print("\n")

b1 = np.array([1,2,3,4])
c1 = np.array([[1], [2]])
print(b1 + c1)

print("\n")

d1 = np.array([1,2,3,4])
print(np.sqrt(d1))  # This will output the square root of each element in the array.
print(np.sin(d1)) # This will output the sine of each element in the array.
print(np.cos(d1)) # This will output the cosine of each element in the array.
print(np.exp(d1)) # This will output the exponential of each element in the array.



 