import datetime

birth_year = input("Enter your birth year:")
print(type(datetime.date.today().year),type(birth_year))
print("Your Age is : ", datetime.date.today().year-int(birth_year)) 

