num_list = []
num = True
while num:
  var = input("Enter the number: ")
  if var == "":
    num = False
    break
  num_list.append(int(var))
print(num_list)
print(sum(num_list))

