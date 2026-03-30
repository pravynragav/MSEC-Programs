def max(a,b,c):
   if(a>b) and (a>c):
      big=a
   elif(b>a) and (b>c):
      big=b
   else:
      big=c
   return big
a=int(input("Enter a value"))
b=int(input("Enter b value"))
c=int(input("Enter c value"))
l=max(a,b,c)
print(f"{l} is the largest number")

