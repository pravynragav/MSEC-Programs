def add(s,n):
    s.add(n)
    return s
def delete(s,n):
    s.remove(n)
    return s
l=[int(i) for i in list(input("Enter list: ").split())]
print("Input List:",l)
s=set(l)
print("Set:",s)
n=int(input("Enter element to add: "))
s=add(s,n)
print(s)
n=int(input("Enter element to remove: "))
s=delete(s,n)
print(s)
