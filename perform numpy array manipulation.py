import numpy as np
array = np.array([1, 2, 3, 4, 5])
print(array.reshape((2, 3)))
print(array[1:3])
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print(np.stack([array1, array2]))
print(np.concatenate([array1, array2]))
print(np.array_split(array, 2))