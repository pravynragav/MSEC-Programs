s = input("Enter a string: ")
alphabets = 0
numbers = 0
spaces = 0
for char in s:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        numbers += 1
    elif char.isspace():
        spaces += 1
print("Alphabets:", alphabets)
print("Numbers:", numbers)
print("Spaces:", spaces)
