import numpy as np
data = np.genfromtxt("../../../datasets/baseball.csv",
delimiter = ",",
skip_header = 1)

print(data.ndim)
print(data.shape)
print(data.size)
np_baseball = np.array(data)
print(np_baseball)
np_height = data[:,3]
print(np_height)
np_weight = data[:,4]
np_age = data[:,5]
print(np_age)

