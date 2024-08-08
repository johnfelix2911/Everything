import random
print("player 1 must play first")
print("try to guess the four didgit word the computer has generated")
x=random.randint(1000,9999)
k=0
while True:
    g=int(input("enter your guess"))
    y=str(x)
    l=[]
    for i in y:
        l.append(i)
    z=str(g)
    d=[]
    for i in z:
        d.append(i)
    b=0
    c=0
    v=p=u=t=""
    if l[0]==d[0]:
        b=b+1
        v=l[0]
    if l[1]==d[1]:
        b=b+1
        p=l[1]
    if l[2]==d[2]:
        b=b+1
        u=l[2]
    if l[3]==d[3]:
        b=b+1
        t=l[3]
    if v!="":
        l.remove(v)
        d.remove(v)
    if p!="":
        l.remove(p)
        d.remove(p)
    if u!="":
        l.remove(u)
        d.remove(u)
    if t!="":
        l.remove(t)
        d.remove(t)
    print("number of bulls=",b)
    for i in d:
        if i in l:
            c=c+1
    k=k+1
    print("number of cows =",c)
    print("attempt number =",k)
    if b==4:
        break
print("total number of guesses=",k)
