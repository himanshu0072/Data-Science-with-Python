#This programm will calculate the age by taking the vakue from user
from datetime import datetime

Day_of_birth=int(input("Enter date between 1-31 :"))
Day_date=datetime.now().day

Month_of_birth=int(input("Enter Month between 1-12 :"))
Month_date=datetime.now().month

Year_of_birth=int(input("Enter Year :"))
current_date=datetime.now().year

year=(current_date - Year_of_birth)

month=(Month_date-Month_of_birth)
month=abs(month)

day=Day_date-Day_of_birth
day=abs(day)


print("Your age is :",year,"Years ",month,"Months ",day,"days ")
