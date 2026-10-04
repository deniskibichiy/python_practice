# List Comprehensions

List comprehensions provide a concise way to create new lists by combining a `for` loop and an optional conditional into a single expression. They are often more readable than manually building a list with `append()` when the transformation is straightforward.

## General Syntax

```python
[output_expression for iterator_variable in iterable]
```

A list comprehension has three core components:

* **Iterable** – The collection being traversed.
* **Iterator variable** – Represents each element of the iterable during iteration.
* **Output expression** – The value added to the new list.

For example:

```python
nums = [12, 8, 21, 3, 16]

new_nums = [num + 1 for num in nums]

print(new_nums)
```

Output:

```text
[13, 9, 22, 4, 17]
```

---

# Building Lists with a Traditional `for` Loop

Without list comprehensions, creating a transformed list requires multiple lines.

```python
nums = [12, 8, 21, 3, 16]

new_nums = []

for num in nums:
    new_nums.append(num + 1)

print(new_nums)
```

Although perfectly valid, this approach is more verbose than a list comprehension.

---

# Using a List Comprehension

The equivalent operation can be written in a single line.

```python
nums = [12, 8, 21, 3, 16]

new_nums = [num + 1 for num in nums]

print(new_nums)
```

---

# Working with Any Iterable

List comprehensions are not limited to lists. They can iterate over any iterable, including:

* `range()`
* tuples
* strings
* sets
* dictionaries
* generators

Example:

```python
result = [num for num in range(11)]

print(result)
```

Output:

```text
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

# Nested Loops

Nested loops can also be expressed using list comprehensions.

## Traditional Nested Loop

```python
pairs = []

for num1 in range(2):
    for num2 in range(6, 8):
        pairs.append((num1, num2))

print(pairs)
```

Output:

```text
[(0, 6), (0, 7), (1, 6), (1, 7)]
```

---

## Nested List Comprehension

```python
pairs = [(num1, num2)
         for num1 in range(2)
         for num2 in range(6, 8)]

print(pairs)
```

The order of the `for` clauses matches the order of the nested loops.

**Trade-off:** Nested list comprehensions are concise but can become difficult to read as complexity increases. 

---

# Creating a Matrix

Nested list comprehensions are commonly used to build matrices.

```python
matrix = [[col for col in range(5)] for row in range(5)]

for row in matrix:
    print(row)
```

Output:

```text
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
```

---

# Filtering Values with Conditionals

A condition can be placed at the end of the comprehension to determine which elements are included.

General syntax:

```python
[output_expression for iterator_variable in iterable if predicate]
```

Example:

```python
squares = [num ** 2 for num in range(18) if num % 2 == 0]

print(squares)
```

Only even numbers are squared and included in the resulting list.

---

# Using Conditional Expressions

Instead of filtering elements out, a conditional expression can determine what value is added.

General syntax:

```python
[true_value if condition else false_value
 for iterator_variable in iterable]
```

Example:

```python
result = [num ** 2 if num % 2 == 0 else 0
          for num in range(10)]

print(result)
```

Output:

```text
[0, 0, 4, 0, 16, 0, 36, 0, 64, 0]
```

Every element is included, but odd numbers are replaced with `0`.

---

# Practical Examples

## Filtering Strings

```python
fellowship = [
    "frodo",
    "samwise",
    "merry",
    "aragorn",
    "legolas",
    "boromir",
    "gimli"
]

new_fellowship = [
    member
    for member in fellowship
    if len(member) >= 7
]

print(new_fellowship)
```

Output:

```text
['samwise', 'aragorn', 'legolas', 'boromir']
```

---

## Conditional Output

Instead of removing short names, replace them with an empty string.

```python
new_fellowship = [
    member if len(member) >= 7 else ""
    for member in fellowship
]

print(new_fellowship)
```

Output:

```text
['', 'samwise', '', 'aragorn', 'legolas', 'boromir', '']
```

---

# Dictionary Comprehensions

Dictionary comprehensions follow the same idea as list comprehensions but create dictionaries instead of lists.

Differences:

* Produce dictionaries instead of lists.
* Use curly braces `{}`.
* The output expression is written as `key: value`.

General syntax:

```python
{key_expression: value_expression
 for iterator_variable in iterable}
```

Example:

```python
pos_neg = {num: -num for num in range(9)}

print(pos_neg)
```

Output:

```python
{
    0: 0,
    1: -1,
    2: -2,
    3: -3,
    4: -4,
    5: -5,
    6: -6,
    7: -7,
    8: -8
}
```

---

## Creating a Dictionary from a List

```python
fellowship = [
    "frodo",
    "samwise",
    "merry",
    "aragorn",
    "legolas",
    "boromir",
    "gimli"
]

name_lengths = {
    member: len(member)
    for member in fellowship
}

print(name_lengths)
```

Output:

```python
{
    'frodo': 5,
    'samwise': 8,
    'merry': 5,
    'aragorn': 8,
    'legolas': 8,
    'boromir': 8,
    'gimli': 5
}
```

---

# When to Use List Comprehensions

List comprehensions are best suited for:

* Creating transformed lists.
* Filtering data.
* Performing simple element-wise operations.
* Replacing short `for` loops that only build a list.

Avoid using list comprehensions when:

* The logic requires multiple nested conditions.
* Readability suffers.
* Several side effects (such as printing or modifying external variables) are involved.

In such cases, a traditional `for` loop is usually clearer and easier to maintain.
