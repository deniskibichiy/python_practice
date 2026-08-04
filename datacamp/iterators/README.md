# Iterators
Iterators control loops, allowing for traversal of arbitrary data containers one item at a time while iterables provide the data to be iterated over. 

Iteration in python is abstracted away from the actual implementation of collection or container data types. This allows iteration over unordered collections, such as sets, ensuring every element is visited exactly once. 

We can iterate with a `for` loop over a specific range
```python
for i in range(4):
    print (i)
```
```bash
0
1
2
3
```
There are a number of iterables in python, including strings, dictionaries, file connections

An inerable is an object with an associated `iter()` method. Applying `iter()` to an iterable creates an iterator.

Iterator: an object that has an associated `next()` method that produces consecutive values

## Creating an iterator on an iterable
An iterator is an object that allows you to iterate over collections of data, such as lists, tuples, dictionaries, and sets. 

Python iterators implement the iterator design pattern which allows traversal of containers and accessing container elements exactly once. The iterator pattern decouples the iteration algorithms from container data structures. 

Iterators:
1. Return the data from a stream or a container one item at a time
2. Keeps track of the current and visited items. 
Use the function iter() and pass the iterable into it 

Iterators

```python
word = 'Data'
it = iter(word)
# Then use next() on the iterator to produce the next value until there are no more values to iterate over

next(word)
next(word)
```
## Iterating at once with (*)
The "star" operator unpacts all values of an iterator in one swoop. 

## Iterators as function arguments
* There are functions that take iterators and iterables as arguments. For example, `list()` and `sum()` functions return a list and the sum of elements, respectively.
### Exercise: Use functions that take an iterable as arguments.
```python
# Create a range object values that would produce the values from 10 to 20 using range()
values = range(10,21)

# Print the range object
print(values)

# Use the list() function to create a list of values from the range object values.
values_list = list(values)

# Print values_list
print(values_list)

# Use the sum() function to get the sum of the values from 10 to 20 from the range object values.
values_sum = sum(values)

# Print values_sum
print(values_sum)
```
## Using `enumerate()`
The function is used to iterate over an iterable while keeping track of both the index and the value. It returns pairs in the form (index, element)
```python
a = ["Python", "Java", "C++"]
for i, v in enumerate(a):
    print(i, v)

```
Output
```bash
0 Python
1 Java
2 C++
```
Syntax:
```python
enumerate(iterable, start=0)
```
Parameters:

* **Iterable:** sequence or collection to iterate over
* **start(optional):** starting value of the index. Default is 0

Returns an enumerate object that generates (index, element) pairs. 

## Using `zip()` function
Combines two or more iterables (such as lists, tuples, or strings) by pairing their corresponding elements together. Returns a zip object, which is an iterator that produces tuples containing one element from each iterable. 

Commonly used when processing related data stored in separate lists. 

Syntax:
```python
zip(iterable1, iterable2, iterable3, ...)
```
```python
mutants = ["charles xavier", "bobby drake", "kurt wagner"]
aliases = ["prof x", "iceman", "nightcrawler"]
powers = ["telepathy", "ice manipulation", "teleportation"]
```
### Creating a List of Tuples
Since `zip()` returns an iterator, it can be converted into a list for easier viewing

```python
mutant_data = list(zip(mutants, aliases, powers))

print(mutant_data)
```
Output
```bash
[
    ('charles xavier', 'prof x', 'telepathy'),
    ('bobby drake', 'iceman', 'ice manipulation'),
    ('kurt wagner', 'nightcrawler', 'teleportation')
]
```
### Creating a Zip Object
```python
mutant_zip = zip(mutants, aliases, powers)

print(mutant_zip)
```
### Unpacking the Zip Object
A zip object can be iterated over using a `for` loop.

```python
mutant_zip = zip(mutants, aliases, powers)

for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)
```
`zip()` pairs elements based on their positions. 

The resulting object is an iterator, meaning it can only be traversed once

To inspect all values multiple times, convert the zip object into a list. 
```python
z = zip([1, 2, 3], ['a', 'b', 'c'])

print(list(z))
print(list(z))
```
Output:
```bash
[(1, 'a'), (2, 'b'), (3, 'c')]
[] # produces an empty list because the iterator has alreadby been consumed
```
# Unpacking Iterables Using `*`

The unpacking operator (`*`) expands the contents of an iterable into individual elements. This is particularly useful when working with iterators such as those returned by `zip()`.

### Example

```python
z = zip([1, 2, 3], ['a', 'b', 'c'])
```

Since `zip()` returns an iterator, it does not immediately produce all values. To unpack the iterator into separate tuples:

```python
z1, z2, z3 = z

print(z1)  # (1, 'a')
print(z2)  # (2, 'b')
print(z3)  # (3, 'c')
```

Alternatively, use the unpacking operator to convert the iterator into a tuple containing all of its elements:

```python
z = zip([1, 2, 3], ['a', 'b', 'c'])

pairs = (*z,)

print(pairs)
# ((1, 'a'), (2, 'b'), (3, 'c'))
```

> **Note:** Iterators are exhausted after they have been traversed once. Attempting to iterate over `z` again after unpacking will produce no values.

---

# 03-08-2026: Using Iterators to Process Large Datasets

## Why use iterators?

Large datasets may not fit entirely into a computer's memory. Loading an entire CSV file can consume a significant amount of RAM and may even cause the program to crash.

Instead of loading the whole dataset at once, an iterator allows the data to be processed **one chunk at a time**.

The general workflow is:

1. Load a small chunk of data into memory.
2. Process the chunk.
3. Store or aggregate the results.
4. Discard the processed chunk.
5. Load the next chunk.

Since only a small portion of the dataset is held in memory at any given time, this approach is memory-efficient and scales well to very large files.

---

## Reading a CSV File in Chunks

Pandas' `read_csv()` function accepts a `chunksize` argument. When provided, it returns an iterator that yields DataFrames instead of loading the entire file.

```python
import pandas as pd

# Store intermediate results
result = []

# read_csv() now returns an iterator
for chunk in pd.read_csv("data.csv", chunksize=1000):

    # Each chunk is a DataFrame containing 1000 rows
    result.append(chunk["x"].sum())

# Compute the final total
total = sum(result)

print(total)
```

### How it works

* `chunksize=1000` loads 1000 rows at a time.
* Each `chunk` is a pandas DataFrame.
* The sum of column `x` is calculated for each chunk.
* Each partial result is stored in a list.
* After all chunks have been processed, the partial sums are combined to produce the final result.

---

## Example: Counting Language Occurrences in a Large Twitter Dataset

The following example counts the frequency of each language in a Twitter dataset while reading only **10 rows at a time**.

```python
import pandas as pd

# Initialize an empty dictionary
counts_dict = {}

# Process the CSV in chunks
for chunk in pd.read_csv("tweets.csv", chunksize=10):

    # Iterate over the selected column
    for entry in chunk["lang"]:

        if entry in counts_dict:
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

print(counts_dict)
```

### Algorithm

For every chunk:

1. Read 10 rows.
2. Iterate through the `lang` column.
3. If the language already exists in the dictionary, increment its count.
4. Otherwise, create a new key with a count of 1.
5. Continue until every chunk has been processed.

---

## Reusable Solution Using a Function

The previous approach can be generalized into a reusable function that works with any CSV file, chunk size, and column.

```python
import pandas as pd

def count_entries(csv_file, c_size, colname):
    """
    Count occurrences of unique values in a column of a CSV file.

    Parameters
    ----------
    csv_file : str
        Path to the CSV file.
    c_size : int
        Number of rows to load per chunk.
    colname : str
        Column whose values should be counted.

    Returns
    -------
    dict
        Dictionary mapping each unique value to its frequency.
    """

    counts_dict = {}

    for chunk in pd.read_csv(csv_file, chunksize=c_size):

        for entry in chunk[colname]:

            if entry in counts_dict:
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    return counts_dict


# Count language occurrences
result_counts = count_entries(
    "tweets.csv",
    c_size=10,
    colname="lang"
)

print(result_counts)
```

---

## Advantages of Chunk Processing

* Processes datasets larger than available RAM.
* Reduces memory consumption.
* Suitable for streaming and ETL pipelines.
* Makes it possible to process millions of records on ordinary hardware.
* Integrates naturally with pandas through the `chunksize` parameter.

---

## Key Takeaways

* `pd.read_csv()` normally loads the entire dataset into memory.
* Supplying the `chunksize` argument makes `read_csv()` return an iterator.
* Each iteration yields a DataFrame containing only the specified number of rows.
* Chunk processing is ideal for large datasets that cannot fit into memory.
* Dictionaries are commonly used to accumulate statistics across chunks.
* Wrapping the logic inside a function improves reusability and readability.
