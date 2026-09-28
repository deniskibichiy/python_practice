# Pandas DataFrame Workflows: `eval()`, `query()`, and `groupby()`

Three DataFrame operations appear repeatedly in practical Pandas workflows:

| Method         | Main purpose              | Mental model  |
| -------------- | ------------------------- | ------------- |
| `df.eval()`    | Perform calculations      | **Calculate** |
| `df.query()`   | Filter rows               | **Find**      |
| `df.groupby()` | Organize rows into groups | **Group**     |

The important skill is not memorizing the methods individually. It is learning to combine them into a sequence:

```text
DataFrame
   ↓
Calculate with eval()
   ↓
Filter with query()
   ↓
Group with groupby()
   ↓
Aggregate
```

---

## 1. `DataFrame.eval()` — Calculate

`eval()` evaluates an expression using DataFrame columns.

It is particularly useful when creating a column from a formula.

### Basic syntax

```python
df.eval("new_column = formula", inplace=True)
```

For example, suppose we have right triangles:

```python
import pandas as pd

triangles = pd.DataFrame({
    "base": [15, 10, 8, 12],
    "height": [8, 6, 5, 9]
})

triangles
```

We can calculate the area using:

```text
area = 1/2 × base × height
```

With `eval()`:

```python
triangles.eval(
    "area = 0.5 * base * height",
    inplace=True
)
```

The resulting DataFrame contains:

```text
   base  height  area
0    15       8  60.0
1    10       6  30.0
2     8       5  20.0
3    12       9  54.0
```

### Why use `eval()`?

Without `eval()`:

```python
triangles["area"] = 0.5 * triangles["base"] * triangles["height"]
```

With `eval()`:

```python
triangles.eval(
    "area = 0.5 * base * height",
    inplace=True
)
```

For simple calculations, both approaches are valid. `eval()` becomes particularly convenient when expressions involve several DataFrame columns.

### Creating multiple calculated columns

You can perform more than one calculation:

```python
triangles.eval("""
    area = 0.5 * base * height
    perimeter = base + height + (base**2 + height**2)**0.5
""", inplace=True)
```

### Important distinction

`eval()` is primarily about **calculations**, not filtering.

Think:

```text
eval() → "What should I calculate?"
```

---

# 2. `DataFrame.query()` — Find Rows

`query()` filters a DataFrame according to a condition.

### Basic syntax

```python
df.query("condition")
```

Suppose we have:

```python
students = pd.DataFrame({
    "name": ["Alice", "Brian", "Carol", "David"],
    "age": [20, 22, 19, 24],
    "score": [75, 62, 81, 48]
})
```

To find students who scored at least 70:

```python
students.query("score >= 70")
```

Result:

```text
    name  age  score
0  Alice   20     75
2  Carol   19     81
```

### Multiple conditions

Use `and`:

```python
students.query("score >= 70 and age < 21")
```

Or `or`:

```python
students.query("score >= 70 or age < 20")
```

You can also use parentheses for clarity:

```python
students.query("(score >= 70) and (age < 21)")
```

### Filtering strings

```python
students.query("name == 'Alice'")
```

### Filtering using a variable

Suppose:

```python
minimum_score = 70
```

You can reference the Python variable using `@`:

```python
students.query("score >= @minimum_score")
```

### Important distinction

`query()` is primarily about **finding rows**.

Think:

```text
query() → "Which rows do I want?"
```

---

# 3. `DataFrame.groupby()` — Build Groups

`groupby()` separates rows into groups based on a common value.

Consider a fruit dataset:

```python
fruit = pd.DataFrame({
    "fruit": [
        "strawberry",
        "banana",
        "banana",
        "strawberry",
        "orange",
        "banana"
    ],
    "weight": [10, 118, 124, 11, 131, 120]
})
```

The data contains different fruit types.

We can group by fruit:

```python
fruit.groupby("fruit")
```

A `groupby()` operation normally becomes useful when combined with an aggregation.

For example:

```python
fruit.groupby("fruit")["weight"].mean()
```

This calculates the average weight for each fruit type.

---

## Common aggregation functions

After grouping, you can calculate:

### Mean

```python
fruit.groupby("fruit")["weight"].mean()
```

### Sum

```python
fruit.groupby("fruit")["weight"].sum()
```

### Minimum

```python
fruit.groupby("fruit")["weight"].min()
```

### Maximum

```python
fruit.groupby("fruit")["weight"].max()
```

### Count

```python
fruit.groupby("fruit")["weight"].count()
```

---

## Multiple aggregations

You can calculate several statistics at once:

```python
fruit.groupby("fruit")["weight"].agg(
    ["count", "mean", "min", "max", "sum"]
)
```

This produces a summary table for every fruit type.

---

# 4. The Three Methods Together

The real value comes from combining the operations.

Suppose we have sales data:

```python
sales = pd.DataFrame({
    "product": ["Laptop", "Laptop", "Phone", "Phone", "Tablet", "Tablet"],
    "quantity": [2, 5, 3, 10, 4, 8],
    "price": [800, 800, 500, 500, 300, 300]
})
```

We want to answer:

> Which products generated more than 3,000 in revenue?

First, calculate revenue.

```python
sales.eval(
    "revenue = quantity * price",
    inplace=True
)
```

Now filter the rows:

```python
sales.query("revenue > 3000")
```

But suppose we want total revenue **per product**.

Group the rows:

```python
sales.groupby("product")["revenue"].sum()
```

We can combine the ideas:

```python
sales.eval(
    "revenue = quantity * price",
    inplace=True
)

sales.groupby("product")["revenue"].sum()
```

Or filter before grouping:

```python
sales.query("quantity >= 5").groupby("product")["revenue"].sum()
```

The sequence matters because each operation changes what the next operation works with.

---

# 5. The Core Mental Model

When working with a DataFrame, ask three questions:

### 1. Do I need to calculate something?

Use:

```python
df.eval()
```

Example:

```python
df.eval("revenue = quantity * price", inplace=True)
```

### 2. Do I need to select specific rows?

Use:

```python
df.query()
```

Example:

```python
df.query("revenue > 1000")
```

### 3. Do I need statistics for categories?

Use:

```python
df.groupby()
```

Example:

```python
df.groupby("category")["revenue"].mean()
```

The workflow becomes:

```text
CALCULATE
    ↓
eval()

FILTER
    ↓
query()

GROUP
    ↓
groupby()

AGGREGATE
    ↓
mean(), sum(), min(), max(), count(), agg()
```

---

# 6. Practical Example: Sales Analysis

Consider:

```python
import pandas as pd

sales = pd.DataFrame({
    "product": [
        "Laptop", "Laptop", "Laptop",
        "Phone", "Phone", "Phone",
        "Tablet", "Tablet", "Tablet"
    ],
    "category": [
        "Computer", "Computer", "Computer",
        "Mobile", "Mobile", "Mobile",
        "Computer", "Computer", "Computer"
    ],
    "quantity": [2, 5, 3, 10, 4, 8, 6, 2, 9],
    "unit_price": [800, 800, 800, 500, 500, 500, 300, 300, 300]
})
```

### Step 1 — Calculate revenue

```python
sales.eval(
    "revenue = quantity * unit_price",
    inplace=True
)
```

### Step 2 — Find high-value transactions

```python
sales.query("revenue >= 3000")
```

### Step 3 — Group by product

```python
sales.groupby("product")["revenue"].sum()
```

### Step 4 — Calculate several statistics

```python
sales.groupby("product")["revenue"].agg(
    ["count", "sum", "mean", "min", "max"]
)
```

### Step 5 — Combine filtering and grouping

```python
sales.query("quantity >= 5").groupby("product")["revenue"].sum()
```

This is closer to the kind of workflow used in real data analysis.

---

# 7. Common Mistakes

## Mistake 1: Forgetting that `query()` returns a DataFrame

This:

```python
sales.query("quantity > 5")
```

does not modify `sales`.

If you want to keep the result:

```python
large_orders = sales.query("quantity > 5")
```

---

## Mistake 2: Forgetting the aggregation after `groupby()`

This:

```python
sales.groupby("product")
```

creates the groups, but does not answer a useful statistical question by itself.

Usually you want:

```python
sales.groupby("product")["revenue"].sum()
```

or:

```python
sales.groupby("product")["revenue"].mean()
```

---

## Mistake 3: Using the wrong column in `eval()`

This will fail if `cost` does not exist:

```python
sales.eval("profit = revenue - cost", inplace=True)
```

Check your columns:

```python
print(sales.columns)
```

---

## Mistake 4: Confusing filtering with grouping

These operations solve different problems:

```python
df.query("score > 70")
```

means:

> Give me rows satisfying this condition.

Whereas:

```python
df.groupby("course")["score"].mean()
```

means:

> Split the rows by course and calculate the average score for each course.

---

# 8. Quick Reference

```python
# Calculate a column
df.eval("total = quantity * price", inplace=True)

# Filter rows
df.query("total > 1000")

# Filter using a Python variable
df.query("total > @threshold")

# Group rows
df.groupby("category")

# Aggregate one column
df.groupby("category")["total"].sum()

# Multiple aggregations
df.groupby("category")["total"].agg(
    ["count", "sum", "mean", "min", "max"]
)

# Filter → group → aggregate
df.query("quantity >= 5") \
  .groupby("category")["total"] \
  .sum()
```

---