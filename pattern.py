n=input("enter the first name")
m=input("enter the second name")
l=[]
d=[]
for i in n:
    l.append(i)
for i in m:
    d.append(i)
for i in range(65,91):
    if chr(i) in l and chr(i) in d:
        l.remove(chr(i))
        d.remove(chr(i))
print(l)
print(d)
c=len(l)+len(d)
x=["friends","lovers","affectionate","enemies","marriage","siblings"]
z=1
for i in x:
    if len(x)==1:
        break
    if z==c:
        x.remove(i)
    z=z+1
print("the relationship status is:",x[0])
