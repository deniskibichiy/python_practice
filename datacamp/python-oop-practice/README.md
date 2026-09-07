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

# Inheritance and Polymorphism

## Core OOP Concepts

### 1. Encapsulation

Encapsulation is the bundling of data (attributes) and the methods that operate on that data within a class.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount
```

Here, `name` and `salary` represent the object's data, while `give_raise()` operates on that data.

### 2. Inheritance

Inheritance allows a new class to reuse and extend the functionality of an existing class.

A child class inherits attributes and methods from its parent class.

```python
class Manager(Employee):
    pass
```

`Manager` automatically inherits the functionality of `Employee`.

### 3. Polymorphism

Polymorphism allows objects of different classes to be treated through a common interface while providing class-specific behavior.

For example, both `Employee` and `Manager` can have a `give_raise()` method, but `Manager` can provide its own implementation.

---

# Class-Level vs Instance-Level Variables

## Instance Attributes

Instance attributes belong to individual objects.

They are normally created using `self`:

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
```

Each object can have different values:

```python
employee_1 = Employee("Alice", 30000)
employee_2 = Employee("Bob", 40000)
```

```text
employee_1.salary → 30000
employee_2.salary → 40000
```

Changing one object's attribute does not normally change the corresponding attribute of another object.

## Class Attributes

Class attributes belong to the class and are shared through the class unless an instance overrides the attribute with its own value.

They are defined directly inside the class:

```python
class Employee:
    MIN_SALARY = 30000
```

They can be accessed through the class:

```python
Employee.MIN_SALARY
```

or through an instance:

```python
employee.MIN_SALARY
```

For constants, uppercase naming is a common convention:

```python
class Employee:
    MIN_SALARY = 30000
```

Class attributes are useful for values shared across instances, such as configuration values, constants, or default policies.

### Important distinction

Consider:

```python
class Employee:
    MIN_SALARY = 30000

employee_1 = Employee()
employee_2 = Employee()
```

Both instances can access:

```python
Employee.MIN_SALARY
```

However, assigning through an instance:

```python
employee_1.MIN_SALARY = 40000
```

does not normally modify the class attribute. It creates an instance attribute that shadows the class attribute for `employee_1`.

The class attribute remains:

```python
Employee.MIN_SALARY  # 30000
```

This is an important distinction between class-level and instance-level data.

---

# Class Methods

A class method is a method that is bound to the class rather than a particular instance.

It is created using the `@classmethod` decorator:

```python
class MyClass:

    @classmethod
    def my_awesome_method(cls, args):
        ...
```

It is called using the class:

```python
MyClass.my_awesome_method(args)
```

The first parameter is conventionally named `cls`. It refers to the class itself.

```python
class Employee:

    @classmethod
    def example(cls):
        print(cls)
```

`cls` is a convention rather than a Python keyword. Another valid parameter name could technically be used, but `cls` should normally be preferred because it communicates the purpose clearly.

### Class methods vs instance methods

An instance method receives the instance as its first argument:

```python
def method(self):
    ...
```

A class method receives the class as its first argument:

```python
@classmethod
def method(cls):
    ...
```

Therefore:

```text
self → instance/object
cls  → class
```

A class method does not receive `self` automatically, so it cannot directly access instance attributes through `self`.

---

# Alternative Constructors

One important use of class methods is creating alternative constructors.

A Python class normally has one `__init__()` method. Rather than trying to create multiple constructors with different signatures, class methods can provide alternative ways of creating objects.

For example:

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_file(cls, filename):
        with open(filename, "r") as f:
            name = f.readline().strip()
            salary = int(f.readline().strip())

        return cls(name, salary)
```

Now the class provides two ways to create an employee:

```python
employee = Employee("Denis", 50000)
```

or:

```python
employee = Employee.from_file("employee_data.txt")
```

The class method constructs and returns an instance using:

```python
return cls(name, salary)
```

Using `cls` rather than explicitly writing `Employee` also makes the method work correctly with subclasses.

---

# When to Use Class Methods

Common uses include:

1. Alternative constructors

For example:

```python
Employee.from_file(...)
```

2. Operations that conceptually belong to the class rather than a particular instance.

3. Factory-style methods that construct instances from different types of input.

A class method should not be used simply because it does not require instance attributes. If a method needs neither instance data nor class data, a `@staticmethod` may be more appropriate.

---

# Class Method Example: Birth Year

```python
class Person:

    CURRENT_YEAR = 2024

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = cls.CURRENT_YEAR - birth_year
        return cls(name, age)


bob = Person.from_birth_year("Bob", 1990)

print(bob.name)
print(bob.age)
```

The class method provides an alternative way to construct a `Person`.

Instead of requiring:

```python
Person("Bob", 34)
```

the caller can provide:

```python
Person.from_birth_year("Bob", 1990)
```

The class method calculates the age and then creates the object.

---

# Class Method Example: Creating a Date from a String

```python
class BetterDate:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_str(cls, datestr):
        parts = datestr.split("-")

        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])

        return cls(year, month, day)


xmas = BetterDate.from_str("2024-12-25")

print(xmas.year)
print(xmas.month)
print(xmas.day)
```

Here, `from_str()` acts as an alternative constructor that knows how to transform a string into the arguments required by `__init__()`.

---

# Class Inheritance

Inheritance allows a new class to reuse and extend an existing class.

The general structure is:

```python
class Child(Parent):
    ...
```

For example:

```python
class Manager(Employee):
    ...
```

`Manager` inherits from `Employee`.

This means that a `Manager` object can use inherited functionality from `Employee` without reimplementing it.

```python
class Employee:

    MIN_SALARY = 30000

    def __init__(self, name, salary=MIN_SALARY):
        self.name = name

        if salary >= Employee.MIN_SALARY:
            self.salary = salary
        else:
            self.salary = Employee.MIN_SALARY

    def give_raise(self, amount):
        self.salary += amount


class Manager(Employee):
    pass


mng = Manager("Denis Kibichiy", 86500)

print(mng.name)
mng.give_raise(2000)
print(mng.salary)
```

Even though `Manager` contains no methods of its own, it inherits:

* `MIN_SALARY`
* `__init__()`
* `give_raise()`

from `Employee`.

An important relationship exists here:

```text
Manager IS-A Employee
```

Therefore:

```python
isinstance(mng, Manager)   # True
isinstance(mng, Employee)  # True
```

---

# Customizing Functionality Through Inheritance

Inheritance is not only about reusing existing functionality. A child class can also customize or extend the behavior it inherits.

For example:

```python
class SavingsAccount(BankAccount):

    def __init__(self, balance, interest_rate):
        BankAccount.__init__(self, balance)
        self.interest_rate = interest_rate
```

The `SavingsAccount` constructor first uses the parent constructor to initialize the `BankAccount` portion of the object:

```python
BankAccount.__init__(self, balance)
```

Then it initializes its own additional attribute:

```python
self.interest_rate = interest_rate
```

A `SavingsAccount` is still a `BankAccount`, but it has additional functionality.

Modern Python generally prefers `super()`:

```python
class SavingsAccount(BankAccount):

    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate
```

---

# Adding Functionality

A child class can define additional methods that do not exist in the parent class.

```python
class SavingsAccount(BankAccount):

    def compute_interest(self, n_periods=1):
        return self.balance * (
            (1 + self.interest_rate) ** n_periods - 1
        )
```

The method can use:

* attributes inherited from `BankAccount`
* attributes defined by `SavingsAccount`

---

# Adding Another Child Class

Multiple classes can inherit from the same parent.

```python
class CheckingAccount(BankAccount):

    def __init__(self, balance, limit):
        super().__init__(balance)
        self.limit = limit

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount, fee=0):
        if amount <= self.limit:
            super().withdraw(amount + fee)
```

The inheritance structure is therefore:

```text
             BankAccount
              /       \
             /         \
SavingsAccount       CheckingAccount
```

Both child classes inherit the common functionality of `BankAccount`, while each can add or customize its own behavior.

---

# Extending a Parent Constructor

A child class can define its own constructor while reusing the parent's constructor.

```python
class Employee:

    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary


class Manager(Employee):

    def __init__(self, name, salary=50000, project=None):
        super().__init__(name, salary)
        self.project = project
```

Here:

```python
super().__init__(name, salary)
```

calls the parent's `__init__()` method.

It initializes:

```python
self.name
self.salary
```

The `Manager` constructor then adds its own attribute:

```python
self.project = project
```

Conceptually:

```text
Manager.__init__()
       │
       ├── Employee.__init__()
       │       ├── self.name
       │       └── self.salary
       │
       └── Manager-specific initialization
               └── self.project
```

---

# Method Overriding

A child class can provide its own implementation of an inherited method.

This is called **method overriding**.

```python
class Employee:

    def give_raise(self, amount):
        self.salary += amount


class Manager(Employee):

    def give_raise(self, amount, bonus=1.05):
        new_amount = amount * bonus
        self.salary += new_amount
```

There is no special `override` keyword in Python.

The child simply defines a method with the same name:

```text
Employee → give_raise()
Manager  → give_raise()
```

When `give_raise()` is called on a `Manager` object, Python uses the `Manager` implementation.

---

# Calling the Parent Implementation with `super()`

Sometimes the child wants to override a method while still reusing the parent's implementation.

`super()` allows the child to call the parent implementation.

```python
class Manager(Employee):

    def give_raise(self, amount, bonus=1.05):
        super().give_raise(amount)
        self.salary += amount * (bonus - 1)
```

The sequence is:

```text
Manager.give_raise()
        ↓
super().give_raise(amount)
        ↓
Employee.give_raise(amount)
```

`super()` is therefore not what causes overriding. Instead:

```text
Same method name in child
        ↓
Method overriding

super().method(...)
        ↓
Call inherited/parent implementation
```

---

# Complete Example

```python
class Employee:

    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount


class Manager(Employee):

    def __init__(self, name, salary=50000, project=None):
        super().__init__(name, salary)
        self.project = project

    def display(self):
        print("Manager", self.name)

    def give_raise(self, amount, bonus=1.05):
        new_amount = amount * bonus
        super().give_raise(new_amount)


mngr = Manager("Ashta Dunbar", 78500)

mngr.give_raise(2000, bonus=1.03)

print(mngr.salary)
```

Output:

```text
80560.0
```

The important concepts demonstrated here are:

```text
Inheritance
    ↓
Manager inherits Employee

Constructor extension
    ↓
super().__init__()

Method overriding
    ↓
Manager.give_raise()

Parent method reuse
    ↓
super().give_raise()
```

## Key Takeaways

| Concept                 | Meaning                                                                                    |
| ----------------------- | ------------------------------------------------------------------------------------------ |
| Encapsulation           | Bundling data and behavior inside a class                                                  |
| Inheritance             | Reusing and extending another class                                                        |
| Class attribute         | Attribute associated with the class                                                        |
| Instance attribute      | Attribute associated with an individual object                                             |
| Class method            | Method bound to the class, receiving `cls`                                                 |
| `@classmethod`          | Decorator used to define a class method                                                    |
| Alternative constructor | Class method providing another way to create an object                                     |
| Method overriding       | Child class provides its own implementation of an inherited method                         |
| `super()`               | Accesses inherited behavior, commonly the parent implementation                            |
| Polymorphism            | Different classes provide compatible interfaces with potentially different implementations |
