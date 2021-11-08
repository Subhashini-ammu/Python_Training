import numpy as np

print("\n<<<<<<<<:Finding max and min from a matrix:>>>>>>>>")

matrix = np.array([1,2,1,3,1,4,0.4,9,11])
max_element = np.max(matrix)
min_element = np.min(matrix)
print("\nMatrix is : ",matrix)
print("\nMaximum element in the matrix is =",max_element)
print("\nMinimum element in the matrix is =",min_element)