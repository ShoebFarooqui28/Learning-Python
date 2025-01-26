import numpy as np

a = np.array([1,2,3])
a = np.append(a, [4,5,6]) # append to the end of the array

print(a)

print("\n")

a = np.insert(a, 3, [7,8,9]) # insert at the 3rd position, but it will be inserted in the form of element, not a list
print(a)

print("\n")

b = np.array([[1,2,3],
              [4,5,6]]) # 2D array

b = np.delete(b, 1, axis=1) # delete the 2nd column, axis=1 means along the columns
print(b)

b = np.delete(b, 1,) # delete the 2nd row, axis=0 means along the rows
b = np.insert(b, 1, 0) # insert a 0 at the 2nd row
b = np.reshape(b, (2,2)) # reshape the array to 2x2 matrix
print(b)

print("\n")

print(b.flatten()) # flatten the array to 1D array

print("\n")

print(b.transpose()) # transpose the array, swap rows and columns

print("\n")

c = np.array([[1,2,3], [4,5,6]])
d = np.array([[7,8,9], [10,11,12]]) 

merged = np.concatenate((c,d), axis=1) # merge two arrays
print(merged)

print("\n")

e = np.array([[1,2,3,4,5],
              [6,7,8,9,10]])

print(np.split(e, 2, axis=0)) # split the array into two parts along the rows

