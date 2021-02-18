#!/usr/bin/python3

from easygui import *

# return the investment result as a string
def investment(ten_year_perc, years, investment, amount_added_each_year):
    perc = ten_year_perc / 100
    for year in range(1, years + 1):
        investment += investment * perc
        investment += amount_added_each_year
    investment_str = "{:,.2f}".format(investment)
    return investment_str

msg = "Fill in the fields to form an aproximate return for your investments"
title = "Jason's Investment Calculator"
fieldNames = ["10 Year Percentage\t\t",
              "Years to Invest\t\t",
              "Initial Investment Amount\t",
              "Addition Yearly Investment Amount\t"]
fieldValues = []  # we start with blanks for the values
fieldValues = multenterbox(msg,title, fieldNames, callback=None, run=True)

# test values for correct types
for value in fieldValues:
    try:
        isinstance(float(value), float)
    except:
        msgbox("Entrie must be of whole/decimal value\nNo symbols or alpha characters allowed", title)
        exit(1)

# make sure that none of the fields was left blank
while 1:
    if fieldValues is None: break
    errmsg = ""
    for i in range(len(fieldNames)):
        if fieldValues[i].strip() == "":
            errmsg += "*" + fieldNames[i] + "\n"
    if errmsg == "":
        break # no problems found
    fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)

investment_result = investment(float(fieldValues[0]),
                               int(fieldValues[1]),
                               float(fieldValues[2]),
                               float(fieldValues[3]))

del(msg)
msg = "Return rate\t\t\t%" + fieldValues[0] +\
      "\nYears of growth\t\t\t" + fieldValues[1] +\
      "\nInitial investment\t\t\t${:,.2f}".format(float(fieldValues[2])) +\
      "\nAnnual invesment\t\t\t${:,.2f}".format(float(fieldValues[3])) +\
      "\nEnding balance\t\t\t$" + investment_result
msgbox(msg, title, ok_button='ESC', image=None, root=None)
