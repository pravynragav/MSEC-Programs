def calc(s1,s2,s3,s4,s5):
   total = s1+s2+s3+s4+s5
   aveg = total/5
   return total,aveg
a=int(input("enter your first mark"))
b=int(input("enter your second mark"))
c=int(input("enter your 3rd mark"))
d=int(input("enter your 4th mark"))
e=int(input("enter your fifth mark"))
tot,avg = calc(a,b,c,d,e)
print(f"Total is {tot} and average is {avg}")
