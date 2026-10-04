recent_orders = [15.99, 28.50, 42.75, 18.99, 55.00, 31.25, 22.99, 67.50]


def average(values):
    """Find the mean of the provided values, rounding the result to 2 digits"""
    average_value = sum(values)/ len(values)
    rounded_average = round(average_value, 2)
    return rounded_average
print(average(recent_orders))
original_price = 899.99

# Define the function with default arguments
def calculate_discount(price, discount_percent=15, round_result=True):
    discounted_price = price - (price * (discount_percent / 100))
    
    if round_result == True:
        # Round the result to two decimal places
        return round(discounted_price,2)
    else:
        return discounted_price

# Call the function with keyword arguments
final_price = calculate_discount(price=original_price, discount_percent=25, round_result=False)
print(final_price)

def clean_text(text, lower=True):
    # Add a multi-line docstring
    """
    Clean text by swapping spaces to underscores and converting to lowercase.
    
    Args:
    	text (str): A string to be cleaned.
    	lower (bool): Whether to convert the text to lowercase.
    
    Returns:
    	text (str): Cleaned string.
    """
    clean_text = text.replace(' ', '_')
    if lower == False:
        return clean_text
    else:
        return clean_text.lower()
      
print(help(clean_text))


# Define a function called concat
def concat(*string):
  """Concatenates multiple string arguments with spaces between them."""

  result = ""

  # Iterate over the Python args tuple
  for arg in string:
    result += " " + arg
  return result

# Call the function
print(concat("Python", "is", "great!"))

# Define a function called concat
def concat(**kwargs):
  """Concatenates keyword arguments into a single string with spaces."""
  
  result = ""
  
  # Iterate over the Python kwargs
  for kwarg in kwargs.values():
    result += " " + kwarg
  return result

# Call the function
print(concat(start="Python", middle="is", end="great!"))

file_size = 2500
extra_space = 0.15

# Define a lambda function
calculate_total = lambda x: x * (1 + extra_space)

# Call the lambda function
print(calculate_total(file_size))
# Call a lambda function in one line
print((lambda x: x * (1 + extra_space))(file_size))

colleagues = ["Sarah Martinez", "Michael Chen", "Emily Brown"]

# Apply the lambda function to each colleague's name
cleaned = map(lambda x: x.replace(" ", "_").lower(), colleagues)

# Convert map object to list
cleaned_list = list(cleaned)
print(cleaned_list)