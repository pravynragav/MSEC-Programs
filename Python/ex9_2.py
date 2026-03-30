s = input("Enter a string: ")
u = 0
l = 0
for char in s:
    if char.isupper():
        u += 1
    elif char.islower():
        l += 1
print("Uppercase letters:", u)
print("Lowercase letters:", l)
