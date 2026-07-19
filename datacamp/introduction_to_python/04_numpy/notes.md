# ndarray
- n-dimensional array
## creating n-dimensional array

```python

import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.71])

print(type(np_height))
print(type(np_weight))

np_2d = np.array([np_height, np_weight])
```
- An array can only contain one single type
`npArray.shape`: check the shape of the numpy array which contains both the number of rows and the number of columns in the numpy array

### subsetting a numpy array
#### Accessing specific elements in a numpy array:

`npArray[row][column]`:

`np_2d[0][2]`: the first row and the third element

Alternative:

 `np_2d[0,2]`: selects the first row, third element and returns the intersection of the rows and column
#### Selecting both column and row in a 2d array
`npArray[:, 1:3]`: selects both rows, second argument after comma selects the first and selects the first two elements through the power of slicing but the specified index is not included.
#### Selecting the entire column
`npArray[1, :] selects the first column entirely

### Performing elementwise calculations
