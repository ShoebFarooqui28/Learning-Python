import numpy as np

print(np.nan) # Output: nan, which is the representation of missing data in numpy
print(np.inf) # Output: inf, which is the representation of infinity in numpy

print(np.isnan(np.nan)) # Output: True, which means the value is missing
print(np.isinf(np.inf)) # Output: True, which means the value is infinite