def is_leap(year):
    """check if the year is leap or not"""
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

# test case
print(is_leap(1800))  # Should be False
print(is_leap(2000))  # Should be True


