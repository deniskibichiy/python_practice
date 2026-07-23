# Built-in Functions
```python
max(list) # 
min(list) #
sum(list)
round(value,no of decimals )
len(list) # number of elements -strings (no of characters including spaces)
sorted(variable) # strings, sort a variable in ascending order
```
## Exercise
### Problem Description

You are developing a backend system for a food delivery platform. During peak traffic, the platform records the monetary value of customer orders placed within a recent one-hour period.

The order amounts are stored in a Python list. Your task is to calculate three important business metrics using Python's built-in functions:

1. The smallest order amount.
2. The largest order amount.
3. The total revenue generated from all orders.

These metrics could help the platform monitor customer spending patterns and revenue during peak periods.

Given Data
```python
recent_orders = [15.99, 28.50, 42.75, 18.99, 55.00, 31.25, 22.99, 67.50]
```
### Requirements

Write a Python program that:

1. Finds the smallest value in recent_orders and stores it in smallest_order.
2. Finds the largest value in recent_orders and stores it in largest_order.
3. Calculates the sum of all order amounts and stores it in total_revenue.
4. Prints all three metrics with clear labels.