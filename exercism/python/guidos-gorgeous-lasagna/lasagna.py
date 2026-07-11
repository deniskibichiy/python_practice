"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME_PER_LAYER = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_cake_layers):
    """Calculate the preparation time
    
    parameters: 
        number: This is the number of layers that the lasagna is expected to have. The assumption here is that each layer will take like 2 minutes to complete.
    returns:
        returns the total time required to cook the lasagna
    """
    return number_of_cake_layers * PREPARATION_TIME_PER_LAYER


def elapsed_time_in_minutes (number_of_layers, elapsed_time):
    """ Calculate the total elapsed time
        parameters:
            number: this is the number of layers that the lasagna has and used the preparation_time_in_minutes function to computer the expected preparation time
            elapsed time: this is the total time that the cake has actually been in the oven.
        returns: 
            The total time that has been spent cooking the lasagna so far.
    """
    number_of_minutes = preparation_time_in_minutes(number_of_layers)
    return number_of_minutes + elapsed_time
