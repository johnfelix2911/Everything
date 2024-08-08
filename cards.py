import random
s=[("spade","ace"),("spade","king"),("spade","queen"),("spade","jack")]
a=[("spade",str(i)) for i in range (2,11)]
s.extend(a)
h=[("heart","ace"),("heart","king"),("heart","queen"),("heart","jack")]
a=[("heart",str(i)) for i in range (2,11)]
h.extend(a)
d=[("diamond","ace"),("diamond","king"),("diamond","queen"),("diamond","jack")]
a=[("diamond",str(i)) for i in range (2,11)]
d.extend(a)
c=[("clubs","ace"),("clubs","king"),("clubs","queen"),("clubs","jack")]
a=[("clubs",str(i)) for i in range (2,11)]
c.extend(a)
s.extend(h)
s.extend(d)
s.extend(c)
w=s.copy()
l=[]
p=[]
for i in range(26):
    k=random.choice(w)
    l.append(k)
    w.remove(k)
d=[]
while True:
    d.append(l[-1])
    l.remove(l[-1])
    #a=input("player 1 enter 1 to play")
    print("player 1 has",len(l),"cards")
    #print(d)
    if len(d)>1:
        if d[-1][1]==d[-2][1]:
            l.extend(d)
            random.shuffle(l)
            d=[]
            print("player 1 scored")
            print("player 1 has",len(l),"cards")
    #b=input("player 2 enter 2 to play")
    d.append(w[-1])
    w.remove(w[-1])
    #print(d)
    print("player 2 has",len(w),"cards")
    if len(d)>1 and d[-1][1]==d[-2][1]:
        w.extend(d)
        random.shuffle(w)
        d=[]
        print("player 2 scored")
        print("player 2 has",len(l),"cards")
    if l==[]:
        print("player 1 has lost")
        break
    if w==[]:
        print("player 2 has lost")
        break
