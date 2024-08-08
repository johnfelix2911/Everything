a=[" "," "," "," "," "]
b=[" "," "," "," "," "]
c=[" "," "," "," "," "]
d=[" "," "," "," "," "]
e=[" "," "," "," "," "]

def print_board():
    r1="| {}| {}| {}| {}| {}|".format(a[0],a[1],a[2],a[3],a[4])
    r2="| {}| {}| {}| {}| {}|".format(b[0],b[1],b[2],b[3],b[4])
    r3="| {}| {}| {}| {}| {}|".format(c[0],c[1],c[2],c[3],c[4])
    r4="| {}| {}| {}| {}| {}|".format(d[0],d[1],d[2],d[3],d[4])
    r5="| {}| {}| {}| {}| {}|".format(e[0],e[1],e[2],e[3],e[4])
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)

def play(p,r):
    while True:
        col=int(input("Enter the column"))
        row=int(input("Enter the row"))
        if row==1:
            if a[col-1]==" " and col<=5:
                a[col-1]=p
                break
            else:
                print("Sorry but that spot is already filled")
        elif row==2:
            if b[col-1]==" " and col<=5:
                b[col-1]=p
                break
            else:
                print("Sorry but that spot is already filled")
        elif row==3:
            if c[col-1]==" " and col<=5:
                c[col-1]=p
                break
            else:
                print("Sorry but that spot is already filled")
        elif row==4:
            if d[col-1]==" " and col<=5:
                d[col-1]=p
                break
            else:
                print("Sorry but that spot is already filled")
        elif row==5:
            if e[col-1]==" " and col<=5:
                e[col-1]=p
                break
            else:
                print("Sorry but that spot is already filled")
        else:
            print("row is out of limits")
    if row==1:
        if col==1:
            if a[1]==r and a[2]==p:
                a[1]=p
            if a[1]==r and a[2]==r and a[3]==p:
                a[1]=p
                a[2]=p
            if a[1]==r and a[2]==r and a[3]==r and a[4]==p:
                a[1]=p
                a[2]=p
                a[3]=p
            if b[0]==r and c[0]==p:
                b[0]=p
            if b[0]==r and c[0]==r and d[0]==p:
                b[0]=p
                c[0]=p
            if b[0]==r and c[0]==r and d[0]==r and e[0]==p:
                b[0]=p
                c[0]=p
                d[0]=p
            if b[1]==r and c[2]==p:
                b[1]=p
            if b[1]==r and c[2]==r and d[3]==p:
                b[1]=p
                c[2]=p
            if b[1]==r and c[2]==r and d[3]==r and e[4]==p:
                b[1]=p
                c[2]=p
                d[3]=p
        if col==2:
            if a[2]==r and a[3]==p:
                a[2]=p
            if a[2]==r and a[3]==r and a[4]==p:
                a[2]=p
                a[3]=p
            if b[1]==r and c[1]==p:
                b[1]=p
            if b[1]==r and c[1]==r and d[1]==p:
                b[1]=p
                c[1]=p
            if b[1]==r and c[1]==r and d[1]==r and e[1]==p:
                b[1]=p
                c[1]=p
                d[1]=p
            if b[2]==r and c[3]==p:
                b[2]=p
            if b[2]==r and c[3]==r and d[4]==p:
                b[2]=p
                c[3]=p
        if col==3:
            if a[1]==r and a[0]==p:
                a[1]=p
            if a[3]==r and a[4]==p:
                a[3]=p
            if b[1]==r and c[0]==p:
                b[1]=p
            if b[3]==r and c[4]==p:
                b[3]=p
            if b[2]==r and c[2]==p:
                b[2]=p
            if b[2]==r and c[2]==r and d[2]==p:
                b[2]=p
                c[2]=p
            if b[2]==r and c[2]==r and d[2]==r and e[2]==p:
                b[2]=p
                c[2]=p
                d[2]=p
        if col==4:
            if a[2]==r and a[1]==p:
                a[2]=p
            if a[2]==r and a[1]==r and a[0]==p:
                a[2]=p
                a[1]=p
            if b[3]==r and c[3]==p:
                b[3]=p
            if b[3]==r and c[3]==r and d[3]==p:
                b[3]=p
                c[3]=p
            if b[3]==r and c[3]==r and d[3]==r and e[3]==p:
                b[3]=p
                c[3]=p
                d[3]=p
            if b[2]==r and c[1]==p:
                b[2]=p
            if b[2]==r and c[1]==r and d[0]==p:
                b[2]=p
                c[1]=p
        if col==5:
            if a[3]==r and a[2]==p:
                a[3]=p
            if a[3]==r and a[2]==r and a[1]==p:
                a[3]=p
                a[2]=p
            if a[3]==r and a[2]==r and a[1]==r and a[0]==p:
                a[3]=p
                a[2]=p
                a[1]=p
            if b[4]==r and c[4]==p:
                b[4]=p
            if b[4]==r and c[4]==r and d[4]==p:
                b[4]=p
                c[4]=p
            if b[4]==r and c[4]==r and d[4]==r and e[4]==p:
                b[4]=p
                c[4]=p
                d[4]=p
            if b[3]==r and c[2]==p:
                b[3]=p
            if b[3]==r and c[2]==r and d[1]==p:
                b[3]=p
                c[2]=p
            if b[3]==r and c[2]==r and d[1]==r and e[0]==p:
                b[3]=p
                c[2]=p
                d[1]=p
    if row==2:
        if col==1:
            if b[1]==r and b[2]==p:
                b[1]=p
            if b[1]==r and b[2]==r and b[3]==p:
                b[1]=p
                b[2]=p
            if b[1]==r and b[2]==r and b[3]==r and b[4]==p:
                b[1]=p
                b[2]=p
                b[3]=p
            if c[0]==r and d[0]==p:
                c[0]=p
            if c[0]==r and d[0]==r and e[0]==p:
                c[0]=p
                d[0]=p
            if c[1]==r and d[2]==p:
                c[1]=p
            if c[1]==r and d[2]==r and e[3]==p:
                c[1]=p
                d[2]=p
        if col==2:
            if b[2]==r and b[3]==p:
                b[2]=p
            if b[2]==r and b[3]==r and b[4]==p:
                b[2]=p
                b[3]=p
            if c[1]==r and d[1]==p:
                c[1]=p
            if c[1]==r and d[1]==r and e[1]==p:
                c[1]=p
                d[1]=p
            if c[2]==r and d[3]==p:
                c[2]=p
            if c[2]==r and d[3]==r and e[4]==p:
                c[2]=p
                d[3]=p
        if col==3:
            if b[1]==r and b[0]==p:
                b[1]=p
            if b[3]==r and b[4]==p:
                b[3]=p
            if c[2]==r and d[2]==p:
                c[2]=p
            if c[2]==r and d[2]==r and e[2]==p:
                c[2]=p
                d[2]=p
        if col==4:
            if b[2]==r and b[1]==p:
                b[2]=p
            if b[2]==r and b[1]==r and b[0]==p:
                b[2]=p
                b[1]=p
            if c[3]==r and d[3]==p:
                c[3]=p
            if c[3]==r and d[3]==r and e[3]==p:
                c[3]=p
                d[3]=p
            if c[2]==r and d[1]==p:
                c[2]=p
            if c[2]==r and d[1]==r and e[0]==p:
                c[2]=p
                d[3]=p
        if col==5:
            if b[3]==r and b[2]==p:
                b[3]=p
            if b[3]==r and b[2]==r and b[1]==p:
                b[3]=p
                b[2]=p
            if b[3]==r and b[2]==r and b[1]==r and b[0]==p:
                b[3]=p
                b[2]=p
                b[1]=p
            if c[3]==r and d[2]==p:
                c[3]=p
            if c[3]==r and d[2]==r and e[1]==p:
                c[3]=p
                d[2]=p
            if c[4]==r and d[4]==p:
                c[4]=p
            if c[4]==r and d[4]==r and e[4]==p:
                c[4]=p
                d[4]=p
    if row==3:
        if col==1:
            if c[1]==r and c[2]==p:
                c[1]=p
            if c[1]==r and c[2]==r and c[3]==p:
                c[1]=p
                c[2]=p
            if c[1]==r and c[2]==r and c[3]==r and c[4]==p:
                c[1]=p
                c[2]=p
                c[3]=p
            if b[0]==r and a[0]==p:
                b[0]=p
            if d[0]==r and e[0]==p:
                d[0]=p
            if b[1]==r and a[2]==p:
                b[1]=p
            if d[1]==r and e[2]==p:
                d[1]=p
        if col==2:
            if c[2]==r and c[3]==p:
                c[2]=p
            if c[2]==r and c[3]==r and c[4]==p:
                c[2]=p
                c[3]=p
            if b[1]==r and a[1]==p:
                b[1]=p
            if d[1]==r and e[1]==p:
                d[1]=p
        if col==3:
            if b[2]==r and a[2]==p:
                b[2]=p
            if c[3]==r and c[4]==p:
                c[3]=p
            if c[1]==r and c[0]==p:
                c[1]=p
            if d[2]==r and e[2]==p:
                d[2]=p
            if b[1]==r and a[0]==p:
                b[1]=p
            if b[3]==r and a[4]==p:
                b[3]=p
            if d[1]==r and e[0]==p:
                d[1]=p
            if d[3]==r and e[4]==p:
                d[3]=p
        if col==4:
            if c[2]==r and c[1]==p:
                c[2]=p
            if c[2]==r and c[1]==r and c[0]==p:
                c[2]=p
                c[1]=p
            if b[3]==r and a[3]==p:
                b[3]=p
            if d[3]==r and e[3]==p:
                d[3]=p
        if col==5:
            if b[4]==r and a[4]==p:
                b[4]=p
            if d[4]==r and e[4]==p:
                d[4]=p
            if c[3]==r and c[2]==p:
                c[3]=p
            if c[3]==r and c[2]==r and c[1]==p:
                c[3]=p
                c[2]=p
            if c[3]==r and c[2]==r and c[1]==r and c[0]==p:
                c[3]=p
                c[2]=p
                c[1]=p
            if b[3]==r and a[2]==p:
                b[3]=p
            if d[3]==r and e[2]==p:
                d[3]=p
    if row==4:
        if col==1:
            if d[1]==r and d[2]==p:
                d[1]=p
            if d[1]==r and d[2]==r and d[3]==p:
                d[1]=p
                d[2]=p
            if d[1]==r and d[2]==r and d[3]==r and d[4]==p:
                d[1]=p
                d[2]=p
                d[3]=p
            if c[0]==r and b[0]==p:
                c[0]=p
            if c[0]==r and b[0]==r and a[0]==p:
                c[0]=p
                b[0]=p
            if c[1]==r and b[2]==p:
                c[1]=p
            if c[1]==r and b[2]==r and a[3]==p:
                c[1]=p
                b[2]=p
        if col==2:
            if d[2]==r and d[3]==p:
                d[2]=p
            if d[2]==r and d[3]==r and d[4]==p:
                d[2]=p
                d[3]=p
            if c[1]==r and b[1]==p:
                c[1]=p
            if c[1]==r and b[1]==r and a[1]==p:
                c[1]=p
                b[1]=p
            if c[2]==r and b[3]==p:
                c[2]=p
            if c[2]==r and b[3]==r and a[4]==p:
                c[2]=p
                b[3]=p
        if col==3:
            if d[1]==r and d[0]==p:
                d[1]=p
            if d[3]==r and d[4]==p:
                d[3]=p
            if c[2]==r and b[2]==p:
                c[2]=p
            if c[2]==r and b[2]==r and a[2]==p:
                c[2]=p
                b[2]=p
        if col==4:
            if d[2]==r and d[1]==p:
                d[2]=p
            if d[2]==r and d[1]==r and d[0]==p:
                d[2]=p
                d[1]=p
            if c[3]==r and b[3]==p:
                c[3]=p
            if c[3]==r and b[3]==r and a[3]==p:
                c[3]=p
                b[3]=p
            if c[2]==r and b[1]==p:
                c[2]=p
            if c[2]==r and b[1]==r and a[0]==p:
                c[2]=p
                b[3]=p
        if col==5:
            if d[3]==r and d[2]==p:
                d[3]=p
            if d[3]==r and d[2]==r and d[1]==p:
                d[3]=p
                d[2]=p
            if d[3]==r and d[2]==r and d[1]==r and d[0]==p:
                d[3]=p
                d[2]=p
                d[1]=p
            if c[3]==r and b[2]==p:
                c[3]=p
            if c[3]==r and b[2]==r and a[1]==p:
                c[3]=p
                b[2]=p
            if c[4]==r and b[4]==p:
                c[4]=p
            if c[4]==r and b[4]==r and a[4]==p:
                c[4]=p
                b[4]=p
    if row==5:
        if col==1:
            if e[1]==r and e[2]==p:
                e[1]=p
            if e[1]==r and e[2]==r and e[3]==p:
                e[1]=p
                e[2]=p
            if e[1]==r and e[2]==r and e[3]==r and e[4]==p:
                e[1]=p
                e[2]=p
                e[3]=p
            if d[0]==r and c[0]==p:
                d[0]=p
            if d[0]==r and c[0]==r and b[0]==p:
                d[0]=p
                c[0]=p
            if d[0]==r and c[0]==r and b[0]==r and a[0]==p:
                d[0]=p
                c[0]=p
                b[0]=p
            if d[1]==r and c[2]==p:
                d[1]=p
            if d[1]==r and c[2]==r and b[3]==p:
                d[1]=p
                c[2]=p
            if d[1]==r and c[2]==r and b[3]==r and a[4]==p:
                b[1]=p
                c[2]=p
                d[3]=p
        if col==2:
            if e[2]==r and e[3]==p:
                e[2]=p
            if e[2]==r and e[3]==r and e[4]==p:
                e[2]=p
                e[3]=p
            if d[1]==r and c[1]==p:
                d[1]=p
            if d[1]==r and c[1]==r and b[1]==p:
                d[1]=p
                c[1]=p
            if d[1]==r and c[1]==r and b[1]==r and a[1]==p:
                d[1]=p
                c[1]=p
                b[1]=p
            if d[2]==r and c[3]==p:
                d[2]=p
            if d[2]==r and c[3]==r and b[4]==p:
                d[2]=p
                c[3]=p
        if col==3:
            if e[1]==r and e[0]==p:
                e[1]=p
            if e[3]==r and e[4]==p:
                e[3]=p
            if d[1]==r and c[0]==p:
                d[1]=p
            if d[3]==r and c[4]==p:
                d[3]=p
            if d[2]==r and c[2]==p:
                d[2]=p
            if d[2]==r and c[2]==r and b[2]==p:
                d[2]=p
                c[2]=p
            if d[2]==r and c[2]==r and b[2]==r and a[2]==p:
                b[2]=p
                c[2]=p
                d[2]=p
        if col==4:
            if e[2]==r and e[1]==p:
                e[2]=p
            if e[2]==r and e[1]==r and e[0]==p:
                e[2]=p
                e[1]=p
            if d[3]==r and c[3]==p:
                d[3]=p
            if d[3]==r and c[3]==r and b[3]==p:
                d[3]=p
                c[3]=p
            if d[3]==r and c[3]==r and b[3]==r and a[3]==p:
                d[3]=p
                c[3]=p
                b[3]=p
            if d[2]==r and c[1]==p:
                d[2]=p
            if d[2]==r and c[1]==r and b[0]==p:
                d[2]=p
                c[1]=p
        if col==5:
            if e[3]==r and e[2]==p:
                e[3]=p
            if e[3]==r and e[2]==r and e[1]==p:
                e[3]=p
                e[2]=p
            if e[3]==r and e[2]==r and e[1]==r and e[0]==p:
                e[3]=p
                e[2]=p
                e[1]=p
            if d[4]==r and c[4]==p:
                d[4]=p
            if d[4]==r and c[4]==r and b[4]==p:
                d[4]=p
                c[4]=p
            if d[4]==r and c[4]==r and b[4]==r and a[4]==p:
                b[4]=p
                c[4]=p
                d[4]=p
            if d[3]==r and c[2]==p:
                d[3]=p
            if d[3]==r and c[2]==r and b[1]==p:
                d[3]=p
                c[2]=p
            if d[3]==r and c[2]==r and b[1]==r and a[0]==p:
                d[3]=p
                c[2]=p
                b[1]=p

print_board()
z=0
for i in range(25):
    if z%2==0:
        print("player x must play now")
        play("x","o")
        print_board()
        z=z+1
    else:
        print("player o mjust play now")
        play("o","x")
        print_board()
        z=z+1
n=0
m=0
for i in a:
    if i.strip()=="x":
        n=n+1
    else:
        m=m+1
for i in b:
    if i.strip()=="x":
        n=n+1
    else:
        m=m+1
for i in c:
    if i.strip()=="x":
        n=n+1
    else:
        m=m+1
for i in d:
    if i.strip()=="x":
        n=n+1
    else:
        m=m+1
for i in e:
    if i.strip()=="x":
        n=n+1
    else:
        m=m+1
if n>m:
    print("player x wins")
else:
    print("player o wins")
