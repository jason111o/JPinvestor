#!/usr/bin/env python3

# Check a dictionary for blank values
def dict_value_blank_test(some_dict: dict) -> bool:
    if not some_dict:
        exit("User escaped program")
    else:
        for value in some_dict:
            try:
                isinstance(float(value), float)
            except:
                return False
    return True


# Return the investment result as a string in U.S. currency format
def investment(ten_year_percentage, years, invested, amount_added_each_year):
    percentage = ten_year_percentage / 100
    for year in range(1, years + 1):
        invested += invested * percentage
        invested += amount_added_each_year
    investment_str = "{:,.2f}".format(invested)
    return investment_str
