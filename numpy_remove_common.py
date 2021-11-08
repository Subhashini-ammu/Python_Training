import numpy as np

print("\n<<<<<<<<:Removing common element from b if present in a:>>>>>>>>")

a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 7, 8, 9])
result = np.setdiff1d(b, a)
print("\nArray a =",a)
print("\nArray b =",b)
print("\nArray [b-a] =",result)