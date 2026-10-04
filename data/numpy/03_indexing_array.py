import numpy as np
data = np.genfromtxt("../../../datasets/baseball.csv",
                  delimiter = ",",
                  usecols=(3,4,5),
                  skip_header = 1)

print (data.shape)
print(data.dtype)
np_height = data[:,0]
np_weight = data[:,1]
np_age = data[:,2]
print(np_age)
# The value in the first row and first column.
print(f"The value in the first row and first column is: {data[0,0]}")
# The value in the second row and first column.
print(f"The value in the second row and first column is {data[1,0]}")
# The value in the first row and second column.
print(f"The value in the first row and second column is {data[0,1]}")
# The value in the last row and last column.
print(f"The value in the last row and last column is {data[-1,-1]}")
# The value in the third row and third column.
print(f"The value in the third row and third column is {data[2,2]}")

#Use NumPy indexing: