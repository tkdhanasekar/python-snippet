#!/usr/bin/python3

#n = int(input("Enter the base length of the triangle: "))
#for txt in range(1,n+1):
#    txt="@"
#    x=txt.center(5)
#    print(x)
 
def triangle(n):
   for i in range(1, n+1):
      print(' ' * n, end='')
      print('@ '*(i))
      n -= 1
n = int(input("Enter the base length of the triangle: "))
triangle(n)
