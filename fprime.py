def prime(num):
   flag=int(0)
   for i in range(2,num//2):
      if(num%i==0):
	 flag=1
	 break
   if(flag==0):
      return 1
   else:
      return 0
num = int(input("Enter a number to check"))
c=(prime(num))
if c==1:
   print("It is prime number")
else:
   print("Not a prime number")
