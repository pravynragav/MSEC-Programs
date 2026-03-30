import cmath
a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
c=int(input("Enter c value: "))
d=(b**2) - (4*a*c)
if d>0:
    r1 = (-b+(d**0.5))/(2*a)
    r2 = (-b-(d**0.5))/(2*a)
    print(f"Roots are real and distinct: x1={r1}, x2={r2}")
elif d==0:
    r1=-b/(2*a)
    print(f"Roots are real and equal: x1={r1}")
else:
    r1=(-b+cmath.sqrt(d))/(2*a)
    r2=(-b-cmath.sqrt(d))/(2*a)
    print(f"Roots are complex: x1={r1}, x2={r2}")
