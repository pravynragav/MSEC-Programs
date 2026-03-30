print("Enter three numbers")
a=int(input("Enter a value "))
b=int(input("Enter b value "))
c=int(input("Enter c value "))
if (a>b) and (a>c):
   print(f"{a} is the largest number")
elif (b>c) and (b>a):
   print(f"{b} is the largest number")
else:
   print(f"{c} is the largest number")
