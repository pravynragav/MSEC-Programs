def Keyadd(res, keyv, val):
    Result[keyv] = val
    SortD = sorted(Result.values(), reverse=True)
    R = {}
    for v in SortD:
        for k in Result:
            if res[k] == v and k not in R:
                R[k] = v
    print("Descending after add:", R)
key_input = input("Enter key: ")
val_input = int(input("Enter val: "))
D = {"apple": 2, "banana": 5, "orange": 3, "jackfruit": 1}
SortD_vals = sorted(D.values())
Result = {}
for v in SortD_vals:
    for k in D:
        if D[k] == v and k not in Result:
            Result[k] = v
print("Ascending: ", Result)
Keyadd(Result, key_input, val_input)
