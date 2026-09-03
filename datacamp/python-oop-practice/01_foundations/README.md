# Basic Introduction to Object-Oriented Programming (OOP)

Object-Oriented Programming (OOP) is a programming paradigm that organizes code around **objects**.

An **object** combines:

* **State**: the data associated with an object.
* **Behavior**: the actions or functionality an object can perform.

OOP bundles an object's state and behavior together, making it easier to model real-world entities and organize complex programs.

For example, a `Customer` object may have:

* **State:** `name`, `email`, and `balance`
* **Behavior:** `deposit()`, `withdraw()`, and `identify()`

In Python, strings, lists, dictionaries, integers, and user-defined instances are all objects.

## Classes

A **class** is a blueprint used to create objects. It defines the attributes and methods that its objects can have.

An **object** is an **instance of a class**.

Objects created from the same class share the same structure and available behavior, although their individual data can differ.

For example, all Python lists support operations such as adding, removing, and accessing elements, even though each list may contain different data.

```python
numbers = [1, 2, 3]
names = ["Denis", "Laura"]

numbers.append(4)
names.append("James")
```

Both objects are lists and therefore support the `append()` method.

## Attributes

**Attributes** represent the state or data of an object.

For example:

```python
customer.name
customer.balance
```

Here, `name` and `balance` are attributes representing information about the `customer` object.

You can inspect an object's available attributes and methods using:

```python
dir(object)
```

For example:

```python
dir(customer)
```

This returns a list of attributes and methods associated with the object.

## Methods

**Methods** represent the behavior of an object.

A method is a function defined inside a class and is used to perform actions involving an object.

For example:

```python
customer.deposit()
customer.withdraw()
```

These methods define actions that a `Customer` object can perform.

## Creating a Class

A class is defined using the `class` keyword.

```python
class Customer:

    def set_name(self, new_name):
        self.name = new_name

    def identify(self):
        print("I am customer " + self.name)
```

An object can then be created from the class:

```python
cust = Customer()

cust.set_name("Denis")
cust.identify()
```

Output:

```text
I am customer Denis
```

In this example:

* `Customer` is the class.
* `cust` is an object, or instance, of the `Customer` class.
* `name` is an attribute.
* `set_name()` and `identify()` are methods.

> **Note:** `cust.identify("Laura")` would produce an error because the `identify()` method does not accept an argument other than `self`.

### `self`

`self` is the first parameter of an **instance method**.

It refers to the specific object on which the method is being called. Python automatically passes the object as the first argument when an instance method is called.

For example:

```python
cust.set_name("Denis")
```

Python effectively calls:

```python
Customer.set_name(cust, "Denis")
```

Therefore, inside the method:

```python
self.name = new_name
```

`self` refers to `cust`, allowing the method to access or modify that specific object's attributes.

Although `self` is technically a naming convention rather than a Python keyword, it should always be used for readability and consistency.

## The `__init__()` Constructor

When a class contains several attributes, the `__init__()` method provides a convenient way to initialize them when an object is created.

The `__init__()` method is automatically called whenever a new object is created.

```python
class Customer:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

        print("The __init__ method was called")
```

Creating an object:

```python
cust = Customer("Denis Kibichiy")
```

The object now has the attributes:

```python
cust.name
# Denis Kibichiy

cust.balance
# 0
```

You can also explicitly provide a value for `balance`:

```python
cust = Customer("Denis Kibichiy", balance=500)
```

### Why Initialize Attributes in `__init__()`?

Although attributes can be created inside other methods, initializing them in `__init__()` is generally preferable when they represent the expected state of every object.

For example:

```python
class Customer:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
```

This makes it immediately clear which attributes a `Customer` object is expected to have.

It also ensures that the attributes are created when the object itself is created.

Defining attributes throughout multiple methods can make a class harder to understand and maintain, particularly as the class grows larger.

## Best Practices

1. **Initialize expected instance attributes in `__init__()`**

   This makes the structure and expected state of an object clear.

2. **Follow Python naming conventions**

   Use `PascalCase` for class names:

   ```python
   class Customer:
       pass
   ```

   Use `lower_snake_case` for functions, methods, variables, and attributes:

   ```python
   def set_name(self, new_name):
       self.customer_name = new_name
   ```

3. **Use `self` consistently for instance methods**

   `self` is the standard convention for referring to the current instance.

4. **Use meaningful names**

   Choose names that clearly describe the purpose of classes, methods, and attributes.

5. **Use docstrings**

   Docstrings help explain the purpose of classes and methods, making code easier for other developers to understand and maintain.

   ```python
   class Customer:
       """Represents a customer with a name and account balance."""

       def __init__(self, name, balance=0):
           """Initialize a customer with a name and optional balance."""
           self.name = name
           self.balance = balance
   ```

## Summary

| Concept      | Description                                                      |
| ------------ | ---------------------------------------------------------------- |
| Object       | An entity that combines data and behavior                        |
| State        | The data associated with an object                               |
| Behavior     | The actions an object can perform                                |
| Class        | A blueprint used to create objects                               |
| Instance     | An object created from a class                                   |
| Attribute    | Data representing an object's state                              |
| Method       | A function representing an object's behavior                     |
| `self`       | A reference to the current object instance                       |
| `__init__()` | A special method used to initialize an object when it is created |
