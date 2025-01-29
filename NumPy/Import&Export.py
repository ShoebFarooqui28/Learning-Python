import numpy as np

a = np.array([[1,2,3,4,5],[32,3,23,23,4]])
#np.save("myArray1.npy", a) # save the array to a file
#np.savetxt("myArray.csv", a, delimiter=",") # save the array to a csv file

b = np.loadtxt("D:\\Learning-Python\\NumPy\\Saved Files\\myArray.csv", delimiter=",") # load the array from a csv file
print(b)



