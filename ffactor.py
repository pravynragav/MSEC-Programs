def factor(n):
   i=2
   while(n!=1):
      if(n%i==0):
        print(i)
	n=n//i
      else:
	 i=i+1
a=int(input("Enter a number"))
if(a==1):
   print("1")
else:
   factor(a)
