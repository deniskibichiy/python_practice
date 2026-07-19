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

NumPy allows mathematical operations to be performed element by element on an array.

For example:

```python
np_height + np_height
```

Each element in `np_height` is added to the corresponding element in the same array.

```python
np_height * 2
```

Each element in the array is multiplied by `2`.

NumPy arrays can also be used in calculations with other arrays of the same shape:

```python
np_height + np_weight
```

The calculation is performed element by element.

### Calculating BMI

Height and weight can be used to calculate BMI:

```python
bmi = np_weight / np_height ** 2

print(bmi)
```

The calculation is performed elementwise. Each person's weight is divided by their height squared.

### Comparing NumPy arrays

NumPy allows comparisons to be performed elementwise.

```python
bmi > 23
```

This returns a Boolean array containing `True` or `False` for each element.

Example:

```python
print(bmi > 23)
```

The result indicates which BMI values are greater than `23`.

### Boolean subsetting

Boolean arrays can be used to select specific elements from a NumPy array.

```python
bmi[bmi > 23]
```

This returns only the BMI values that are greater than `23`.

The same approach can be used with other arrays:

```python
np_height[np_height > 1.75]
```

This selects heights greater than `1.75`.
