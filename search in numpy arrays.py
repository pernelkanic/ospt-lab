import numpy as np
a1=np.array([0,1,3,4,5, 6,7,8,9])
print(np.where (a1==3))
print(np.where (a1%2==0))
print(np.where (a1%2==1))
print(np.searchsorted(a1,7,side= 'right'))
print(np.searchsorted (a1, [1,2,3]))