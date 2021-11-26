
#Write a Python program to get days between two dates. 
#Exampe: days between 28/02/2000 and  28/02/2001

from datetime import date

date1 = date(2000,2,28)
date2 = date(2001,2,28)

diff = date2-date1
print("Two dates :", date1," ",date2)
print("Number of days between these days :" ,diff.days)