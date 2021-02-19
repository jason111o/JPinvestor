#!/usr/bin/env python3

from easygui import *
import functions

version = "2.0"

# Display and get input from user then store in a dictionary
msg = "Fill in the fields to form an approximate return for your investments"
title = "Jason's Investment Calculator " + version
fieldNames = ["10 Year Percentage\t\t",
              "Years to Invest\t\t",
              "Initial Investment Amount\t",
              "Addition Yearly Investment Amount\t"]
fieldValues = multenterbox(msg, title, fieldNames, callback=None, run=True)

# test values for correct types
while not functions.dict_value_blank_test(fieldValues):
    msgbox("Entries must be of whole or decimal value\nNo other characters are allowed", title)
    fieldValues = multenterbox(msg, title, fieldNames, callback=None, run=True)

# Calculate investment
investment_result = functions.investment(float(fieldValues[0]),
                                         int(fieldValues[1]),
                                         float(fieldValues[2]),
                                         float(fieldValues[3]))

# Display results in a gui window
result_msg = "Return rate\t\t\t%" + fieldValues[0] + \
             "\nYears of growth\t\t\t" + fieldValues[1] + \
             "\nInitial investment\t\t\t${:,.2f}".format(float(fieldValues[2])) + \
             "\nAnnual invesment\t\t\t${:,.2f}".format(float(fieldValues[3])) + \
             "\nEnding balance\t\t\t$" + investment_result
msgbox(result_msg, title, ok_button='ESC', root=None)
