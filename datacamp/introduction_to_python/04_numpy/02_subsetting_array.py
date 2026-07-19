import numpy as np
data = np.genfromtxt("datasets/baseball.csv",
                     delimiter = ",",
                     skip_header = 1)
print(data.shape)
np_height = data[:,3]
np_weight = data[:,4]

print(np_height)
print(np_weight)
print(np_height.shape)
print(np_weight.shape)

np_2d = np.array([np_height, np_weight])

print(np_2d.shape)
print("Baseball starts here")

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array([baseball])
# Print out the type of np_baseball
print(np_baseball)
print(np_baseball.shape)

# Print out the shape of np_baseball
