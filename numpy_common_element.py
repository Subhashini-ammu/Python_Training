import numpy as np

print("\n<<<<<<<<:Finding the common elements from a and b:>>>>>>>>")

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

common_element = np.intersect1d(a, b)
print("\nThe common element from a & b array is =",common_element)