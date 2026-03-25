num = int(input("Enter a number to check armstrong or not "))
n=num
pow=len(str(num))
tot=0
while n>0:
   digit=n%10
   tot=tot+(digit**pow)
   n=n//10
if tot==num:
      print("The number is armstrong numer")
else:
      print("The number is not an armstrong numer")
