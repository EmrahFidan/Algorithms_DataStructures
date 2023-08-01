import numpy as np

print("\n----------------------------------------------------\n")

array = np.array([[1, 2, 3, 4, 5]]) # vector 1D array
print(array)
print("Dimension: ", array.shape)


#?  Array2,3,4 boyutlu bile olabilir. 
#! 2D Array = Row - Column

print("\n---------------------------------------------------------\n")

array2D = np.array([[1, 2, 3, 4, 5],[6,7,8,9,10]]) # vector 2D array
print(array2D)
print("Location row 2 - column 4 => ", array2D[1,3])
print("Dimension: ", array2D.shape)

print("\n----------------------------------------------------------\n")

