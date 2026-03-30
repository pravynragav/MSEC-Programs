Set1={int(i) for i in set(input("Enter set 1: ").split())}
Set2={int(i) for i in set(input("Enter set 2: ").split())}
print("Interaction:",Set1.intersection(Set2))
print("Union:",Set1.union(Set2))
print("Difference:",Set1.difference(Set2))
