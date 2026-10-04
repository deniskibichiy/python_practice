import numpy as np
data = np.genfromtxt("datasets/baseball.csv",
                     delimiter = ",",
                     skip_header = 1)
print(data.shape)

# Extracting height and weight data and storing them in numpy array
np_height = data[:,3] # select the entire second column and all the rows
np_weight = data[:,4] # select the fourth column, all rows

print(np_height.itemsize)
print(np_height.size)
print(np_height.shape)
# type of the elements in the array.
print(np_height.dtype.name)
print(np_weight.shape)

#45th element of the height array
print(np_height[45])

np_2d = np.array([np_height, np_weight])


# Create a 2D numpy array from baseball: np_baseball


# Print out the shape of np_baseball


