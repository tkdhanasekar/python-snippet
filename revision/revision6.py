#!/usr/bin/python3

birthyear = int(input("Enter your year of birth: "))
age = 2023-birthyear
print(age)
if age > 18 and age < 70:
    print("you are eligible to vote and marriage")
elif age > 70:
    print("your age is too high take rest")
elif age < 18:
    print("you are minor not eligible to vote and booked under POSCO act")

