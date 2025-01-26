import numpy as np

number = np.random.randint(99, size=(1,3,4)) # 3D array with random integers between 0 and 99, size 1x3x4
print(number)

coinflips = np.random.binomial(1, p =0.5, size=(3,3)) # 2D array with random binomial distribution, size 3x3
print(coinflips)