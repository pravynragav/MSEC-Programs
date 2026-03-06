def AddKey(Result, keyv, val):
    Result[keyv] = val
    SortD = sorted(Result.values(), reverse=True)
    R = {}
    for v in SortD:
        for k in Result:
            if Result[k] == v and k not in R:
                R[k] = v
    print("Descending after add:", R)
val_input = int(input("Enter val: "))
key_input = int(input("Enter key: "))
D = {1: 2, 2: 5, 3: 3, 4: 1}
SortD_vals = sorted(D.values())
Result = {}
for v in SortD_vals:
    for k in D:
        if D[k] == v and k not in Result:
            Result[k] = v
print("Ascending: ", Result)
AddKey(Result, key_input, val_input)
