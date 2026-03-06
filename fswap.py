def swap(a,b):
   a=a+b
   b=a-b
   a=a-b
   print("after swap")
   print(f" a = {a}")
   print(f" b = {b}")
a=int(input("Enter a value"))
b=int(input("Enter b value"))
swap(a,b)
