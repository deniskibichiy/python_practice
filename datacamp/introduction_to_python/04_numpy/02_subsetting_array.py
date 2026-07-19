import numpy as np
data = np.load("../../../datasets/baseball.csv")
print(data.shape)
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.71])

print(type(np_height))
print(type(np_weight))

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
