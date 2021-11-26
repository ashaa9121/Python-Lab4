# Write a Python program to convert unix timestamp string to readable date.

import datetime 

print(datetime.datetime.fromtimestamp(int("1637908961")).strftime('%Y-%m-%d %H:%M:%S'))
#print(datetime.datetime.now().timestamp())
