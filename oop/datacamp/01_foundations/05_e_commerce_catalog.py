"""
Level 3: Basic Inheritance

Scenario: E-Commerce Product Catalog

Create a base Product class and a child DigitalProduct class.

Product Attributes: name (str), price (float).

Product Method: get_display_price() — returns formatted price string like "$19.99".

DigitalProduct Attributes: Inherits name and price, plus adds download_link (str) and file_size_mb (float).

DigitalProduct Method: generate_download_payload() — returns a dict containing name, download_link, and file_size_mb.
"""