def square(number):
    """
    1 - 1 = 2^0 
    2 - 2 = 2^1
    3 - 4 = 2 ^2
    4 - 8 = 2 ^ 3
    5 - 16 = 2 ^ 4
    6 - 32 = 2 ^ 5
    7 - 64 = 2 ^ 6
    8 - 128 = 2 ^ 7
    9 - 256 = 2 ^ 8
    try:
        success_failure_ratio = num_successes/num_failures
        return success_failure_ratio
    except ZeroDivisionError:
        return "No failures, so the success/failure ration is undefined."
print(square(8,0)) 
"""
    try:
        if number > 0 and number < 65:
            return 2 ** (number - 1)
    except:
        raise ValueError ("square must be between 1 and 64")
    print(square(3))




def total(number):
    """
    1 = 1
    2 = square(2) + square(1)
    3 = square (3) + square(2) + square(1)
    4 = square(4) + square (3) + square (2) + square(1)
    
    """
