def find(s,n):
   if n in s:
      print(n,"exists")
   else:
      print(n,"doesn't exists")
s={int(i) for i in set(input("Enter value: ").split())}
print("length: ",len(s))
print("set: ",s)
n=int(input("enter element to check: "))
find(s,n)
