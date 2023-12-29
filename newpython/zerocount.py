myword = input("Enter the word: ")
a = myword.split("-")
print(a[0]+str(a[1].count('0'))+a[2])


