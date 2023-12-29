mystr = input("Enter the string: ")
str1=mystr.split(":")[0]
str2=mystr.split(":")[1]
print(str1.lstrip()+(":")+str2.lstrip())

