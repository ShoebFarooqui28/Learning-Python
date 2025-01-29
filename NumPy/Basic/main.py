import numpy as np

list1 = np.array([1, 2, 3, 4, 5])
list2 = np.array([6, 7, 8, 9, 10])

list3 = np.array([list1, list2])

print(list3.dtype) # Output: int64
print(list3.shape) # Output: (2, 5)
print(list3.ndim) # Output: 2
print(list3.size) # Output: 10