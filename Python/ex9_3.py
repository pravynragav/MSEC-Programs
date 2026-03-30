s = input("Enter a string: ")
ans = {}
for char in s:
    if char in ans:
        ans[char] += 1
    else:
        ans[char] = 1
print(ans)
