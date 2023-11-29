import numpy as np
def ndims(x):
return len(x.shape)
a = np.array([1, 2, 3])
print(ndims(a)) 
b = np.array([[1, 2, 3], [4, 5, 6]])
print(ndims(b))