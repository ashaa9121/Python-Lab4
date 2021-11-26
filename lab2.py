# Write a Python program to subtract five days from current date.

from datetime import date,timedelta

date_diff = date.today() - timedelta(5)
print("Current date : ",date.today())
print()
print("5 days before current date :", date_diff)