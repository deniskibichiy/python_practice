"""
Build an Inventory class for an RPG game where items have weight constraints.

Attributes:

max_weight: Maximum weight capacity passed in during instantiation.

items: A dictionary storing item names as keys and their weights as values (e.g., {"sword": 5.0, "potion": 0.5}).

Methods:

add_item(name, weight): Adds the item if current_weight + weight <= max_weight and returns True. If it exceeds capacity, do not add it and return False.

remove_item(name): Removes the item by name and returns its weight. If the item isn't in inventory, return None.

get_total_weight(): Returns the sum of all item weights currently stored.
"""
class Inventory:
    items = {"sword": 5.0, "potion": 0.5}
    def __init__(self, max_weight, items):
        self.max_weight = max_weight
        self.items = items
    def add_item(self,name, weight):
        pass
    def remove_item(name):
        pass
    def get_total_weight():
        pass





"""
Level 3: Basic Inheritance

Scenario: E-Commerce Product Catalog

Create a base Product class and a child DigitalProduct class.

Product Attributes: name (str), price (float).

Product Method: get_display_price() — returns formatted price string like "$19.99".

DigitalProduct Attributes: Inherits name and price, plus adds download_link (str) and file_size_mb (float).

DigitalProduct Method: generate_download_payload() — returns a dict containing name, download_link, and file_size_mb.
"""

"""
Level 4: Extending Constructors with super()

Scenario: Employee Payroll System

Create a base Employee class and a SalariedEmployee child class.

Employee Constructor: Takes employee_id (str) and base_salary (float). Stores both as attributes and initializes an empty deductions list.

SalariedEmployee Constructor: Must use super().__init__() to accept employee_id and base_salary, while taking an additional parameter annual_bonus (float).

SalariedEmployee Method: calculate_monthly_pay() — returns (base_salary + annual_bonus) / 12.
"""

"""
Level 5: Method Overriding

Scenario: Notification Dispatcher

Create a base Notification class and two subclasses: EmailNotification and SMSNotification.

Notification Method: send(message) — raises NotImplementedError("Subclasses must implement send()").

EmailNotification Attributes: recipient_email (str). Overrides send(message) to return "Sending email to [recipient_email]: [message]".

SMSNotification Attributes: phone_number (str). 

Overrides send(message) to return "Sending SMS to [phone_number]: [message]".
"""


"""
Level 6: Overriding + Calling Parent via super()

Scenario: Bank Account TypesCreate a base BankAccount class and a SavingsAccount child class.

BankAccount Attributes: account_number (str), balance (float).

BankAccount Method: withdraw(amount) — subtracts amount if funds are sufficient and returns True. Returns False if insufficient funds.

SavingsAccount Attributes: Extends BankAccount using super().__init__(), adding withdrawal_fee (float, e.g., 2.50).

SavingsAccount Method: Overrides withdraw(amount). It should calculate total_deduction = amount + withdrawal_fee and delegate the actual withdrawal logic to super().withdraw(total_deduction).
"""


"""
Level 7: Polymorphism

Scenario: Media Playlist PlayerDemonstrate duck typing and polymorphism without forcing rigid inheritance.

Create three distinct classes: 

Song (attributes: title, artist), Podcast (attributes: title, host, episode_num), and Audiobook (attributes: title, narrator).Give all three classes a play() method that returns a custom playback string (e.g., "Playing song: Title by Artist").

Write a standalone function play_entire_queue(media_queue) that accepts a list containing a mix of Song, Podcast, and Audiobook instances, calls play() on each, and collects the results into a list.
"""

"""
Level 8: Mixed OOP Decision Problem

Scenario: Smart Home IoT Network

Determine the appropriate mechanism (Class vs Instance Attribute, Inheritance, super(), Class Method) for each requirement:

Create a base SmartDevice class with device_id and is_powered_on (bool, default False). 

Include a class variable connected_devices_count.

Create an alternative constructor from_config_dict(config) that initializes a SmartDevice from {"id": "DEV123", "power": True}.

Create a child SmartThermostat class that inherits from SmartDevice, uses super() in __init__, and adds target_temperature (float) and mode ("heat" or "cool").

Override get_status() in SmartThermostat to call super().get_status() and append target temperature and mode information to the result.

"""

"""
Level 9: Debugging & Refactoring

Scenario: Spot the BugIdentify and fix the 3 conceptual OOP bugs in this snippet:"""

class InventoryItem:
    item_count = 0
    items_list = []  # Bug 1 location?

    def __init__(self, name, price):
        self.name = name
        self.price = price
        InventoryItem.item_count += 1
        self.items_list.append(self)

    def apply_discount(self,discount_percent):  # Bug 2 location? - The method did not have a self argument.
        self.price -= self.price * (discount_percent / 100)

    def create_sale_item(name):  # Bug 3 location?
        return InventoryItem(name, price=5.0)

"""
Level 10: Cumulative Mini-Project

Scenario: Library Management & Checkout System

Build a terminal application in a single file combining all concepts covered:

Book (Class vs Instance):Class attribute total_books_in_catalog.

Instance attributes: isbn, title, author, is_checked_out (bool).

LibraryMember (Encapsulation & Inheritance):Base class 

Member: member_id, name, borrowed_books (list).

Subclass VIPMember: uses super(), gets a higher max_borrow_limit (5 books vs 2 for regular members).

Library (Alternative Constructors & Polymorphism):Class method from_json_file(filepath) / from_dict_list(data) to bulk initialize catalog.

Method checkout(member, isbn) — validates borrowing limits and updates book state.

Method generate_report() — iterates over all catalog items and members polymorphically to display system status.

"""
