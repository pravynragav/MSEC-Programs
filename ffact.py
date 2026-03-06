def fact(n):
   if(n==1 or n==0):
      return n
   else:
      return n*fact(n-1)
num=int(input("Enter a number"))
if num <0:
   print("factorial number is negative")
else:
   print("factorial of ",num,"is",fact(num))

