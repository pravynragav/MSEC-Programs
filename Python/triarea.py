import sys
print("Enter 1 for breadth and length")
print("Enter 2 for sides")
x=int(input())
if x==1:
   b=int(input("enter breadth"))
   h=int(input("enter height"))
   if(b<0 or h<0):
     print("inalid input")
     sys.exit()
   a1=0.5*b*h
   print(f"Area = {a1}")
elif x==2:
  a=int(input("Enter side a"))
  b=int(input("Enter side b"))
  c=int(input("Enter side c"))
  if(a<0 or b<0 or c<0):
    print("invalid input")
    sys.exit()
  s=(a+b+c)/2
  a2=s*(s-a)*(s-b)*(s-c)
  area=a2**0.5
  print(f"Area of triangle = {area}")
else:
  print("Choose valid option")
