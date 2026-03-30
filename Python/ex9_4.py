input_str = input("Enter two strings separated by a space: ")
str1, str2 = input_str.split()
new_str1 = str2[0:2] + str1[2:]
new_str2 = str1[0:2] + str2[2:]
ans = new_str1 + " " + new_str2
print(ans)
