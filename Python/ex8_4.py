Set1={int(i) for i in set(input("Enter set 1: ").split())}
Set2={int(i) for i in set(input("Enter set 2: ").split())}
if(Set1.issubset(Set2)==True):
    print("S1 is subset of S2")
elif(Set2.issubset(Set1)==True):
    print("S2 is subset of S1")
else:
    print("There is no subsets on each set")
