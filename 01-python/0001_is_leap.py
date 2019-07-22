def is_leap(year):
    """check if the year is leap or not"""
    if year % 4 == 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False


