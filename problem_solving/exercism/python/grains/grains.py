def square(number):
    try:
        if (number > 0 and number < 65):
            return 2 ** (number - 1)
    except:
        raise ValueError ("square must be between 1 and 64")

def total():
    pass
