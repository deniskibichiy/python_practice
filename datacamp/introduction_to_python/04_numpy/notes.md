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

# NumPy Practice — Day 2

## Objective

Today’s goal is to become comfortable working with real-world tabular data using NumPy.

By the end of these exercises, you should be able to:

* Load a CSV dataset into a NumPy array.
* Inspect the dimensions and structure of an array.
* Select individual elements.
* Select rows and columns.
* Use slicing to subset arrays.
* Perform calculations on columns.
* Use Boolean indexing to filter data.
* Combine multiple NumPy operations to answer questions about a dataset.

## Dataset

The dataset for today's exercises is:

```text
../../../datasets/baseball.csv
```

Start by loading the dataset:

```python
import numpy as np

data = np.loadtxt(
    "../../../datasets/baseball.csv",
    delimiter=",",
    skiprows=1
)

print(data)
```

Before starting the exercises, inspect the dataset:

```python
print(data.shape)
print(data.ndim)
print(data.size)
```

---

# Exercise 1 — Inspect the Dataset

Create a Python file:

```text
01_inspect_dataset.py
```

Load the `baseball.csv` dataset and answer the following questions using NumPy:

1. How many rows are in the dataset?
2. How many columns are in the dataset?
3. How many dimensions does the NumPy array have?
4. How many total values are stored in the array?

Use:

```python
data.shape
data.ndim
data.size
```

### Expected Skills

You should understand the difference between:

```text
shape
ndim
size
```

### Challenge

Print the information in a readable format:

```text
Dataset dimensions:
Number of rows:
Number of columns:
Number of dimensions:
Total number of values:
```

---

# Exercise 2 — Access Individual Elements

Create:

```text
02_indexing_array.py
```

Using the `data` NumPy array, practice accessing individual values.

Print:

1. The value in the first row and first column.
2. The value in the second row and first column.
3. The value in the first row and second column.
4. The value in the last row and last column.
5. The value in the third row and third column.

Use NumPy indexing:

```python
data[row, column]
```

Remember that Python uses zero-based indexing.

For example:

```python
data[0, 0]
```

refers to the first row and first column.

### Challenge

Access the same last element using negative indexing:

```python
data[-1, -1]
```

Confirm that both approaches produce the same result.

---

# Exercise 3 — Select Rows and Columns

Create:

```text
03_select_rows_columns.py
```

Practice selecting complete rows and columns.

Print:

1. The first row.
2. The second row.
3. The last row.
4. The first column.
5. The second column.
6. The last column.

Use slicing and indexing.

Examples:

```python
data[0, :]
```

and:

```python
data[:, 0]
```

### Questions

After completing the exercise, answer:

1. What does `:` mean when used in `data[0, :]`?
2. What does `:` mean when used in `data[:, 0]`?
3. What is the difference between selecting a row and selecting a column?

### Challenge

Print the first five rows:

```python
data[:5, :]
```

Then print the first five rows and first two columns:

```python
data[:5, :2]
```

---

# Exercise 4 — Slice the Dataset

Create:

```text
04_slicing_array.py
```

Use NumPy slicing to create different subsets of the dataset.

Print:

1. The first five rows.
2. The last five rows.
3. Rows 5 through 10.
4. The first two columns of every row.
5. The last two columns of every row.
6. The first five rows and first three columns.

Use slicing syntax:

```python
data[start:stop]
```

and:

```python
data[row_start:row_stop, column_start:column_stop]
```

### Challenge

Create a new NumPy array containing only the first 10 rows and the first 2 columns.

Store it in:

```python
subset
```

Then print:

```python
print(subset)
print(subset.shape)
```

Explain why the shape of `subset` is different from the shape of `data`.

---

# Exercise 5 — Calculate Statistics for the Dataset

Create:

```text
05_numpy_statistics.py
```

Use NumPy functions to calculate statistics for each column.

For every column, calculate:

* Minimum
* Maximum
* Mean
* Median
* Standard deviation

Use functions such as:

```python
np.min()
np.max()
np.mean()
np.median()
np.std()
```

For example:

```python
print(np.mean(data[:, 0]))
```

### Questions

For each column, determine:

1. Which column has the highest average?
2. Which column has the lowest average?
3. Which column has the largest range?
4. Which column has the smallest range?

Remember:

```text
range = maximum - minimum
```

### Challenge

Calculate the statistics without using a Python `for` loop first.

Then, if you can, use a loop to print the statistics for every column.

---

# Exercise 6 — Boolean Indexing

Create:

```text
06_boolean_indexing.py
```

Use Boolean indexing to filter the dataset.

Start with one column:

```python
column = data[:, 0]
```

Create a Boolean condition that identifies values greater than the mean:

```python
condition = column > np.mean(column)
```

Use the condition to filter the data:

```python
filtered_data = data[condition]
```

Print:

```python
print(filtered_data)
```

### Tasks

Perform the following:

1. Find the mean of the first column.
2. Select all rows where the first column is greater than its mean.
3. Count how many rows satisfy the condition.
4. Select all rows where the first column is less than its mean.

### Challenge

Create a condition involving two columns.

For example:

```python
condition = (data[:, 0] > np.mean(data[:, 0])) & \
            (data[:, 1] > np.mean(data[:, 1]))
```

Use the condition to find rows where both conditions are true.

---

# Exercise 7 — NumPy Mini-Analysis

Create:

```text
07_numpy_mini_analysis.py
```

This is the final challenge for today.

Using only NumPy operations, perform a small analysis of the `baseball.csv` dataset.

Your program should:

1. Load the dataset.
2. Print its shape.
3. Calculate the mean of every column.
4. Calculate the minimum of every column.
5. Calculate the maximum of every column.
6. Identify the row with the highest value in the first column.
7. Identify the row with the lowest value in the first column.
8. Filter the dataset to include only rows where the first column is above its mean.
9. Print the number of rows remaining after filtering.

Use:

```python
np.argmax()
np.argmin()
np.mean()
np.min()
np.max()
```

### Challenge

Use `np.argmax()` and `np.argmin()` to find the row positions of the maximum and minimum values in the first column.

Then use those positions to retrieve the complete rows.

---

# Rules for Today's Practice

For these exercises:

* Use NumPy.
* Do not use pandas.
* Do not use DataFrames.
* Do not use external datasets.
* Do not search for solutions online.
* Use the local `baseball.csv` dataset.
* Write each exercise in its own Python file.
* Run each file from the terminal.
* Use `print()` to inspect your results.

You may use the official Python and NumPy documentation that you have saved locally.

---

# Recommended Directory Structure

By the end of today, your directory should look approximately like this:

```text
04_numpy/
├── 01_inspect_dataset.py
├── 02_indexing_array.py
├── 03_select_rows_columns.py
├── 04_slicing_array.py
├── 05_numpy_statistics.py
├── 06_boolean_indexing.py
└── 07_numpy_mini_analysis.py
```

The dataset remains in:

```text
python_practice/
└── datasets/
    └── baseball.csv
```

---

# Completion Checklist

## Exercise 1

* [ ] Loaded the dataset
* [ ] Checked `shape`
* [ ] Checked `ndim`
* [ ] Checked `size`

## Exercise 2

* [ ] Accessed individual elements
* [ ] Used positive indexing
* [ ] Used negative indexing

## Exercise 3

* [ ] Selected rows
* [ ] Selected columns
* [ ] Practiced `:`

## Exercise 4

* [ ] Practiced slicing
* [ ] Created a smaller subset
* [ ] Checked the subset's shape

## Exercise 5

* [ ] Calculated minimum
* [ ] Calculated maximum
* [ ] Calculated mean
* [ ] Calculated median
* [ ] Calculated standard deviation

## Exercise 6

* [ ] Created Boolean conditions
* [ ] Filtered rows
* [ ] Counted filtered results
* [ ] Used multiple conditions

## Exercise 7

* [ ] Completed the mini-analysis
* [ ] Used `argmax`
* [ ] Used `argmin`
* [ ] Combined indexing, slicing, statistics, and Boolean filtering

---

# Final Goal

By the end of today's session, you should be able to look at a NumPy array and confidently answer:

```text
How big is this array?
What does each dimension represent?
How do I access a specific value?
How do I select a row?
How do I select a column?
How do I select a subset?
How do I calculate statistics?
How do I filter the data?
How do I combine these operations to analyze the data?
```

Do not move to pandas until these operations feel natural in NumPy.

