import numpy as np

print("\n<<<<<<<<:Replacing all odd numbers from the array with -1:>>>>>>>>\n")

array = np.arange(1, 100, dtype=int)
for i in range(len(array)):
    if (i % 2 == 1):
        array[i] = -1

print("\t\t\tOdd numbers from 1 to 100 replaced with '-1' \n", array)