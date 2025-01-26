import numpy as np

a = np.array([[1,2,3],
              [4, "Hello", 6],
              [7,8,9]
              ])


print(type(a[0][1])) # Output: <class 'str'>,  because of the string "Hello" in the array.