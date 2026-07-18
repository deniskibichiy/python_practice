def leap_year(year):
    """
    parameters
        year(int) year to be checked
    returns
        bool: if year is leap 
    """
    if year % 4 == 0 and not year % 100 == 0:
        return True
    if year % 100 == 0:
        return year % 400 == 0
    return False
    