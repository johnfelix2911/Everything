def board():
    print("        1     2     3     4     5     6     7     8")
    print("A    | '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'|".format(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7]))
    print("B    | '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'|".format(b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7]))
    print("C    | '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'|".format(c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7]))
    print("D    | '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'|".format(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7]))
    print("E    | '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'|".format(e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7]))
    print("F    | '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'|".format(f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7]))
    print("E    | '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'|".format(g[0],g[1],g[2],g[3],g[4],g[5],g[6],g[7]))
    print("H    | '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'|".format(h[0],h[1],h[2],h[3],h[4],h[5],h[6],h[7]))

def playw():
    m=input("enter your move in the format 'position1 to position2' (white)")
    l=m.split()
    p1=l[0]
    p2=l[2]
    if p1[0]=="A":
        p=a[int(p1[1])]
        while True:
            if p[0]=="b":
                print("not your piece")
            else:
                if p[1]=="P":
                    if 
                break

def playb():
    #statements

a=["bR","bH","bB","bQ","bK","bB","bH","bR"]
b=["bP","bP","bP","bP","bP","bP","bP","bP"]
c=["  ","  ","  ","  ","  ","  ","  ","  "]
d=["  ","  ","  ","  ","  ","  ","  ","  "]
e=["  ","  ","  ","  ","  ","  ","  ","  "]
f=["  ","  ","  ","  ","  ","  ","  ","  "]
g=["wP","wP","wP","wP","wP","wP","wP","wP"]
h=["wR","wH","wB","wQ","wK","wB","wH","wR"]
board()
while True:
    playw()
    playb()
