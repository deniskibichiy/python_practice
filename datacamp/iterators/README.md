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
