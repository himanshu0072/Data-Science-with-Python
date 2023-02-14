#This programm will calculate the age by taking the age from user
from datetime import datetime

Year_of_birth=int(input("Enter Year :"))
current_date=datetime.now().year

age=current_date - Year_of_birth 

print("Your age is :",age)
