def board():
    print("| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'|".format(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8]))
    print("| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'|".format(b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7],b[8]))
    print("| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'|".format(c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8]))
    print("| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'|".format(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8]))
    print("| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'|".format(e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7],e[8]))
    print("| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'|".format(f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8]))
    print("| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'|".format(g[0],g[1],g[2],g[3],g[4],g[5],g[6],g[7],g[8]))
    print("| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'|".format(h[0],h[1],h[2],h[3],h[4],h[5],h[6],h[7],h[8]))
    print("| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'| '{}'|".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))

a=['','','','','','','','','']
b=['','','','','','','','','']
c=['','','','','','','','','']
d=['','','','','','','','','']
e=['','','','','','','','','']
f=['','','','','','','','','']
g=['','','','','','','','','']
h=['','','','','','','','','']
i=['','','','','','','','','']

a=['5','3',' ',' ','7',' ',' ',' ',' ']
b=['6',' ',' ','1','9','5',' ',' ',' ']
c=[' ','9','8',' ',' ',' ',' ','6',' ']
d=['8',' ',' ',' ','6',' ',' ',' ','3']
e=['4',' ',' ','8',' ','3',' ',' ','1']
f=['7',' ',' ',' ','2',' ',' ',' ','6']
g=[' ','6',' ',' ',' ',' ','2','8',' ']
h=[' ',' ',' ','4','1','9',' ',' ','5']
i=[' ',' ',' ',' ','8',' ',' ','7','9']

#setboard()
board()
l=['1','2','3','4','5','6','7','8','9']
while True:
    p=0
    for x in range(9):
        for y in range(9):
            if x!=y:
                if a[x]==a[y]:
                    for v in l:
                        if v not in a:
                            a[x]=v
                    p=p+1
    for x in range(9):
        for y in range(9):
            if x!=y:
                if b[x]==b[y]:
                    for v in l:
                        if v not in b:
                            b[x]=v
                    p=p+1
    for x in range(9):
        for y in range(9):
            if x!=y:
                if c[x]==c[y]:
                    for v in l:
                        if v not in c:
                            c[x]=v
                    p=p+1
    for x in range(9):
        for y in range(9):
            if x!=y:
                if d[x]==d[y]:
                    for v in l:
                        if v not in d:
                            d[x]=v
                    p=p+1
    for x in range(9):
        for y in range(9):
            if x!=y:
                if e[x]==e[y]:
                    for v in l:
                        if v not in e:
                            e[x]=v
                    p=p+1
    for x in range(9):
        for y in range(9):
            if x!=y:
                if f[x]==f[y]:
                    for v in l:
                        if v not in f:
                            f[x]=v
                    p=p+1
    for x in range(9):
        for y in range(9):
            if x!=y:
                if g[x]==g[y]:
                    for v in l:
                        if v not in g:
                            g[x]=v
                    p=p+1
    for x in range(9):
        for y in range(9):
            if x!=y:
                if h[x]==h[y]:
                    for v in l:
                        if v not in h:
                            h[x]=v
                    p=p+1
    for x in range(9):
        for y in range(9):
            if x!=y:
                if i[x]==i[y]:
                    for v in l:
                        if v not in i:
                            i[x]=v
                    p=p+1
    if a[0]==b[0] or a[0]==c[0] or a[0]==d[0] or a[0]==e[0] or a[0]==f[0] or a[0]==g[0] or a[0]==h[0] or a[0]==i[0]:
        m=[a[0],b[0],c[0],d[0],e[0],f[0],g[0],h[0],i[0]]
        if a[0]==b[0]:
            for q in l:
                if q not in m:
                    a[0]=q
        if a[0]==c[0]:
            for q in l:
                if q not in m:
                    a[0]=q
        if a[0]==d[0]:
            for q in l:
                if q not in m:
                    a[0]=q
        if a[0]==e[0]:
            for q in l:
                if q not in m:
                    a[0]=q
        if a[0]==f[0]:
            for q in l:
                if q not in m:
                    a[0]=q
        if a[0]==g[0]:
            for q in l:
                if q not in m:
                    a[0]=q
        if a[0]==h[0]:
            for q in l:
                if q not in m:
                    a[0]=q
        if a[0]==i[0]:
            for q in l:
                if q not in m:
                    a[0]=q
        p=p+1
    if a[1]==b[1] or a[1]==c[1] or a[1]==d[1] or a[1]==e[1] or a[1]==f[1] or a[1]==g[1] or a[1]==h[1] or a[1]==i[1]:
        m=[a[1],b[1],c[1],d[1],e[1],f[1],g[1],h[1],i[1]]
        if a[1]==b[1]:
            for q in l:
                if q not in m:
                    a[1]=q
        if a[1]==c[1]:
            for q in l:
                if q not in m:
                    a[1]=q
        if a[1]==d[1]:
            for q in l:
                if q not in m:
                    a[1]=q
        if a[1]==e[1]:
            for q in l:
                if q not in m:
                    a[1]=q
        if a[1]==f[1]:
            for q in l:
                if q not in m:
                    a[1]=q
        if a[1]==g[1]:
            for q in l:
                if q not in m:
                    a[1]=q
        if a[1]==h[1]:
            for q in l:
                if q not in m:
                    a[1]=q
        if a[1]==i[1]:
            for q in l:
                if q not in m:
                    a[1]=q
        p=p+1
    if a[2]==b[2] or a[2]==c[2] or a[2]==d[2] or a[2]==e[2] or a[2]==f[2] or a[2]==g[2] or a[2]==h[2] or a[2]==i[2]:
        m=[a[2],b[2],c[2],d[2],e[2],f[2],g[2],h[2],i[2]]
        if a[2]==b[2]:
            for q in l:
                if q not in m:
                    a[2]=q
        if a[2]==c[2]:
            for q in l:
                if q not in m:
                    a[2]=q
        if a[2]==d[2]:
            for q in l:
                if q not in m:
                    a[2]=q
        if a[2]==e[2]:
            for q in l:
                if q not in m:
                    a[2]=q
        if a[2]==f[2]:
            for q in l:
                if q not in m:
                    a[2]=q
        if a[2]==g[2]:
            for q in l:
                if q not in m:
                    a[2]=q
        if a[2]==h[2]:
            for q in l:
                if q not in m:
                    a[2]=q
        if a[2]==i[2]:
            for q in l:
                if q not in m:
                    a[2]=q
        p=p+1
    if a[3]==b[3] or a[3]==c[3] or a[3]==d[3] or a[3]==e[3] or a[3]==f[3] or a[3]==g[3] or a[3]==h[3] or a[3]==i[3]:
        m=[a[3],b[3],c[3],d[3],e[3],f[3],g[3],h[3],i[3]]
        if a[3]==b[3]:
            for q in l:
                if q not in m:
                    a[3]=q
        if a[3]==c[3]:
            for q in l:
                if q not in m:
                    a[3]=q
        if a[3]==d[3]:
            for q in l:
                if q not in m:
                    a[3]=q
        if a[3]==e[3]:
            for q in l:
                if q not in m:
                    a[3]=q
        if a[3]==f[3]:
            for q in l:
                if q not in m:
                    a[3]=q
        if a[3]==g[3]:
            for q in l:
                if q not in m:
                    a[3]=q
        if a[3]==h[3]:
            for q in l:
                if q not in m:
                    a[3]=q
        if a[3]==i[3]:
            for q in l:
                if q not in m:
                    a[3]=q
        p=p+1
    if a[4]==b[4] or a[4]==c[4] or a[4]==d[4] or a[4]==e[4] or a[4]==f[4] or a[4]==g[4] or a[4]==h[4] or a[4]==i[4]:
        m=[a[4],b[4],c[4],d[4],e[4],f[4],g[4],h[4],i[4]]
        if a[4]==b[4]:
            for q in l:
                if q not in m:
                    a[4]=q
        if a[4]==c[4]:
            for q in l:
                if q not in m:
                    a[4]=q
        if a[4]==d[4]:
            for q in l:
                if q not in m:
                    a[4]=q
        if a[4]==e[4]:
            for q in l:
                if q not in m:
                    a[4]=q
        if a[4]==f[4]:
            for q in l:
                if q not in m:
                    a[4]=q
        if a[4]==g[4]:
            for q in l:
                if q not in m:
                    a[4]=q
        if a[4]==h[4]:
            for q in l:
                if q not in m:
                    a[4]=q
        if a[4]==i[4]:
            for q in l:
                if q not in m:
                    a[4]=q
        p=p+1
    if a[5]==b[5] or a[5]==c[5] or a[5]==d[5] or a[5]==e[5] or a[5]==f[5] or a[5]==g[5] or a[5]==h[5] or a[5]==i[5]:
        m=[a[5],b[5],c[5],d[5],e[5],f[5],g[5],h[5],i[5]]
        if a[5]==b[5]:
            for q in l:
                if q not in m:
                    a[5]=q
        if a[5]==c[5]:
            for q in l:
                if q not in m:
                    a[5]=q
        if a[5]==d[5]:
            for q in l:
                if q not in m:
                    a[5]=q
        if a[5]==e[5]:
            for q in l:
                if q not in m:
                    a[5]=q
        if a[5]==f[5]:
            for q in l:
                if q not in m:
                    a[5]=q
        if a[5]==g[5]:
            for q in l:
                if q not in m:
                    a[5]=q
        if a[5]==h[5]:
            for q in l:
                if q not in m:
                    a[5]=q
        if a[5]==i[5]:
            for q in l:
                if q not in m:
                    a[5]=q
        p=p+1
    if a[6]==b[6] or a[6]==c[6] or a[6]==d[6] or a[6]==e[6] or a[6]==f[6] or a[6]==g[6] or a[6]==h[6] or a[6]==i[6]:
        m=[a[6],b[6],c[6],d[6],e[6],f[6],g[6],h[6],i[6]]
        if a[6]==b[6]:
            for q in l:
                if q not in m:
                    a[6]=q
        if a[6]==c[6]:
            for q in l:
                if q not in m:
                    a[6]=q
        if a[6]==d[6]:
            for q in l:
                if q not in m:
                    a[6]=q
        if a[6]==e[6]:
            for q in l:
                if q not in m:
                    a[6]=q
        if a[6]==f[6]:
            for q in l:
                if q not in m:
                    a[6]=q
        if a[6]==g[6]:
            for q in l:
                if q not in m:
                    a[6]=q
        if a[6]==h[6]:
            for q in l:
                if q not in m:
                    a[6]=q
        if a[6]==i[6]:
            for q in l:
                if q not in m:
                    a[6]=q
        p=p+1
    if a[7]==b[7] or a[7]==c[7] or a[7]==d[7] or a[7]==e[7] or a[7]==f[7] or a[7]==g[7] or a[7]==h[7] or a[7]==i[7]:
        m=[a[7],b[7],c[7],d[7],e[7],f[7],g[7],h[7],i[7]]
        if a[7]==b[7]:
            for q in l:
                if q not in m:
                    a[7]=q
        if a[7]==c[7]:
            for q in l:
                if q not in m:
                    a[7]=q
        if a[7]==d[7]:
            for q in l:
                if q not in m:
                    a[7]=q
        if a[7]==e[7]:
            for q in l:
                if q not in m:
                    a[7]=q
        if a[7]==f[7]:
            for q in l:
                if q not in m:
                    a[7]=q
        if a[7]==g[7]:
            for q in l:
                if q not in m:
                    a[7]=q
        if a[7]==h[7]:
            for q in l:
                if q not in m:
                    a[7]=q
        if a[7]==i[7]:
            for q in l:
                if q not in m:
                    a[7]=q
        p=p+1
    if a[8]==b[8] or a[8]==c[8] or a[8]==d[8] or a[8]==e[8] or a[8]==f[8] or a[8]==g[8] or a[8]==h[8] or a[8]==i[8]:
        m=[a[8],b[8],c[8],d[8],e[8],f[8],g[8],h[8],i[8]]
        if a[8]==b[8]:
            for q in l:
                if q not in m:
                    a[8]=q
        if a[8]==c[8]:
            for q in l:
                if q not in m:
                    a[8]=q
        if a[8]==d[8]:
            for q in l:
                if q not in m:
                    a[8]=q
        if a[8]==e[8]:
            for q in l:
                if q not in m:
                    a[8]=q
        if a[8]==f[8]:
            for q in l:
                if q not in m:
                    a[8]=q
        if a[8]==g[8]:
            for q in l:
                if q not in m:
                    a[8]=q
        if a[8]==h[8]:
            for q in l:
                if q not in m:
                    a[8]=q
        if a[8]==i[8]:
            for q in l:
                if q not in m:
                    a[8]=q
        p=p+1
    if b[0]==a[0] or b[0]==c[0] or b[0]==d[0] or b[0]==e[0] or b[0]==f[0] or b[0]==g[0] or b[0]==h[0] or b[0]==i[0]:
        m=[b[0],a[0],c[0],d[0],e[0],f[0],g[0],h[0],i[0]]
        if b[0]==a[0]:
            for q in l:
                if q not in m:
                    b[0]=q
        if b[0]==c[0]:
            for q in l:
                if q not in m:
                    b[0]=q
        if b[0]==d[0]:
            for q in l:
                if q not in m:
                    b[0]=q
        if b[0]==e[0]:
            for q in l:
                if q not in m:
                    b[0]=q
        if b[0]==f[0]:
            for q in l:
                if q not in m:
                    b[0]=q
        if b[0]==g[0]:
            for q in l:
                if q not in m:
                    b[0]=q
        if b[0]==h[0]:
            for q in l:
                if q not in m:
                    b[0]=q
        if b[0]==i[0]:
            for q in l:
                if q not in m:
                    b[0]=q
        p=p+1
    if b[1]==a[1] or b[1]==c[1] or b[1]==d[1] or b[1]==e[1] or b[1]==f[1] or b[1]==g[1] or b[1]==h[1] or b[1]==i[1]:
        m=[b[1],a[1],c[1],d[1],e[1],f[1],g[1],h[1],i[1]]
        if b[1]==a[1]:
            for q in l:
                if q not in m:
                    b[1]=q
        if b[1]==c[1]:
            for q in l:
                if q not in m:
                    b[1]=q
        if b[1]==d[1]:
            for q in l:
                if q not in m:
                    b[1]=q
        if b[1]==e[1]:
            for q in l:
                if q not in m:
                    b[1]=q
        if b[1]==f[1]:
            for q in l:
                if q not in m:
                    b[1]=q
        if b[1]==g[1]:
            for q in l:
                if q not in m:
                    b[1]=q
        if b[1]==h[1]:
            for q in l:
                if q not in m:
                    b[1]=q
        if b[1]==i[1]:
            for q in l:
                if q not in m:
                    b[1]=q
        p=p+1
    if b[2]==a[2] or b[2]==c[2] or b[2]==d[2] or b[2]==e[2] or b[2]==f[2] or b[2]==g[2] or b[2]==h[2] or b[2]==i[2]:
        m=[b[2],a[2],c[2],d[2],e[2],f[2],g[2],h[2],i[2]]
        if b[2]==a[2]:
            for q in l:
                if q not in m:
                    b[2]=q
        if b[2]==c[2]:
            for q in l:
                if q not in m:
                    b[2]=q
        if b[2]==d[2]:
            for q in l:
                if q not in m:
                    b[2]=q
        if b[2]==e[2]:
            for q in l:
                if q not in m:
                    b[2]=q
        if b[2]==f[2]:
            for q in l:
                if q not in m:
                    b[2]=q
        if b[2]==g[2]:
            for q in l:
                if q not in m:
                    b[2]=q
        if b[2]==h[2]:
            for q in l:
                if q not in m:
                    b[2]=q
        if b[2]==i[2]:
            for q in l:
                if q not in m:
                    b[2]=q
        p=p+1
    if b[3]==a[3] or b[3]==c[3] or b[3]==d[3] or b[3]==e[3] or b[3]==f[3] or b[3]==g[3] or b[3]==h[3] or b[3]==i[3]:
        m=[b[3],a[3],c[3],d[3],e[3],f[3],g[3],h[3],i[3]]
        if b[3]==a[3]:
            for q in l:
                if q not in m:
                    b[3]=q
        if b[3]==c[3]:
            for q in l:
                if q not in m:
                    b[3]=q
        if b[3]==d[3]:
            for q in l:
                if q not in m:
                    b[3]=q
        if b[3]==e[3]:
            for q in l:
                if q not in m:
                    b[3]=q
        if b[3]==f[3]:
            for q in l:
                if q not in m:
                    b[3]=q
        if b[3]==g[3]:
            for q in l:
                if q not in m:
                    b[3]=q
        if b[3]==h[3]:
            for q in l:
                if q not in m:
                    b[3]=q
        if b[3]==i[3]:
            for q in l:
                if q not in m:
                    b[3]=q
        p=p+1
    if b[4]==a[4] or b[4]==c[4] or b[4]==d[4] or b[4]==e[4] or b[4]==f[4] or b[4]==g[4] or b[4]==h[4] or b[4]==i[4]:
        m=[b[4],a[4],c[4],d[4],e[4],f[4],g[4],h[4],i[4]]
        if b[4]==a[4]:
            for q in l:
                if q not in m:
                    b[4]=q
        if b[4]==c[4]:
            for q in l:
                if q not in m:
                    b[4]=q
        if b[4]==d[4]:
            for q in l:
                if q not in m:
                    b[4]=q
        if b[4]==e[4]:
            for q in l:
                if q not in m:
                    b[4]=q
        if b[4]==f[4]:
            for q in l:
                if q not in m:
                    b[4]=q
        if b[4]==g[4]:
            for q in l:
                if q not in m:
                    b[4]=q
        if b[4]==h[4]:
            for q in l:
                if q not in m:
                    b[4]=q
        if b[4]==i[4]:
            for q in l:
                if q not in m:
                    b[4]=q
        p=p+1
    if b[5]==a[5] or b[5]==c[5] or b[5]==d[5] or b[5]==e[5] or b[5]==f[5] or b[5]==g[5] or b[5]==h[5] or b[5]==i[5]:
        m=[b[5],a[5],c[5],d[5],e[5],f[5],g[5],h[5],i[5]]
        if b[5]==a[5]:
            for q in l:
                if q not in m:
                    b[5]=q
        if b[5]==c[5]:
            for q in l:
                if q not in m:
                    b[5]=q
        if b[5]==d[5]:
            for q in l:
                if q not in m:
                    b[5]=q
        if b[5]==e[5]:
            for q in l:
                if q not in m:
                    b[5]=q
        if b[5]==f[5]:
            for q in l:
                if q not in m:
                    b[5]=q
        if b[5]==g[5]:
            for q in l:
                if q not in m:
                    b[5]=q
        if b[5]==h[5]:
            for q in l:
                if q not in m:
                    b[5]=q
        if b[5]==i[5]:
            for q in l:
                if q not in m:
                    b[5]=q
        p=p+1
    if b[6]==a[6] or b[6]==c[6] or b[6]==d[6] or b[6]==e[6] or b[6]==f[6] or b[6]==g[6] or b[6]==h[6] or b[6]==i[6]:
        m=[b[6],a[6],c[6],d[6],e[6],f[6],g[6],h[6],i[6]]
        if b[6]==a[6]:
            for q in l:
                if q not in m:
                    b[6]=q
        if b[6]==c[6]:
            for q in l:
                if q not in m:
                    b[6]=q
        if b[6]==d[6]:
            for q in l:
                if q not in m:
                    b[6]=q
        if b[6]==e[6]:
            for q in l:
                if q not in m:
                    b[6]=q
        if b[6]==f[6]:
            for q in l:
                if q not in m:
                    b[6]=q
        if b[6]==g[6]:
            for q in l:
                if q not in m:
                    b[6]=q
        if b[6]==h[6]:
            for q in l:
                if q not in m:
                    b[6]=q
        if b[6]==i[6]:
            for q in l:
                if q not in m:
                    b[6]=q
        p=p+1
    if b[7]==a[7] or b[7]==c[7] or b[7]==d[7] or b[7]==e[7] or b[7]==f[7] or b[7]==g[7] or b[7]==h[7] or b[7]==i[7]:
        m=[b[7],a[7],c[7],d[7],e[7],f[7],g[7],h[7],i[7]]
        if b[7]==a[7]:
            for q in l:
                if q not in m:
                    b[7]=q
        if b[7]==c[7]:
            for q in l:
                if q not in m:
                    b[7]=q
        if b[7]==d[7]:
            for q in l:
                if q not in m:
                    b[7]=q
        if b[7]==e[7]:
            for q in l:
                if q not in m:
                    b[7]=q
        if b[7]==f[7]:
            for q in l:
                if q not in m:
                    b[7]=q
        if b[7]==g[7]:
            for q in l:
                if q not in m:
                    b[7]=q
        if b[7]==h[7]:
            for q in l:
                if q not in m:
                    b[7]=q
        if b[7]==i[7]:
            for q in l:
                if q not in m:
                    b[7]=q
        p=p+1
    if b[8]==a[8] or b[8]==c[8] or b[8]==d[8] or b[8]==e[8] or b[8]==f[8] or b[8]==g[8] or b[8]==h[8] or b[8]==i[8]:
        m=[b[8],a[8],c[8],d[8],e[8],f[8],g[8],h[8],i[8]]
        if b[8]==a[8]:
            for q in l:
                if q not in m:
                    b[8]=q
        if b[8]==c[8]:
            for q in l:
                if q not in m:
                    b[8]=q
        if b[8]==d[8]:
            for q in l:
                if q not in m:
                    b[8]=q
        if b[8]==e[8]:
            for q in l:
                if q not in m:
                    b[8]=q
        if b[8]==f[8]:
            for q in l:
                if q not in m:
                    b[8]=q
        if b[8]==g[8]:
            for q in l:
                if q not in m:
                    b[8]=q
        if b[8]==h[8]:
            for q in l:
                if q not in m:
                    b[8]=q
        if b[8]==i[8]:
            for q in l:
                if q not in m:
                    b[8]=q
        p=p+1
    if c[0]==a[0] or c[0]==b[0] or c[0]==d[0] or c[0]==e[0] or c[0]==f[0] or c[0]==g[0] or c[0]==h[0] or c[0]==i[0]:
        m=[c[0],a[0],b[0],d[0],e[0],f[0],g[0],h[0],i[0]]
        if c[0]==a[0]:
            for q in l:
                if q not in m:
                    c[0]=q
        if c[0]==b[0]:
            for q in l:
                if q not in m:
                    c[0]=q
        if c[0]==d[0]:
            for q in l:
                if q not in m:
                    c[0]=q
        if c[0]==e[0]:
            for q in l:
                if q not in m:
                    c[0]=q
        if c[0]==f[0]:
            for q in l:
                if q not in m:
                    c[0]=q
        if c[0]==g[0]:
            for q in l:
                if q not in m:
                    c[0]=q
        if c[0]==h[0]:
            for q in l:
                if q not in m:
                    c[0]=q
        if c[0]==i[0]:
            for q in l:
                if q not in m:
                    c[0]=q
        p=p+1
    if c[1]==a[1] or c[1]==b[1] or c[1]==d[1] or c[1]==e[1] or c[1]==f[1] or c[1]==g[1] or c[1]==h[1] or c[1]==i[1]:
        m=[c[1],a[1],b[1],d[1],e[1],f[1],g[1],h[1],i[1]]
        if c[1]==a[1]:
            for q in l:
                if q not in m:
                    c[1]=q
        if c[1]==b[1]:
            for q in l:
                if q not in m:
                    c[1]=q
        if c[1]==d[1]:
            for q in l:
                if q not in m:
                    c[1]=q
        if c[1]==e[1]:
            for q in l:
                if q not in m:
                    c[1]=q
        if c[1]==f[1]:
            for q in l:
                if q not in m:
                    c[1]=q
        if c[1]==g[1]:
            for q in l:
                if q not in m:
                    c[1]=q
        if c[1]==h[1]:
            for q in l:
                if q not in m:
                    c[1]=q
        if c[1]==i[1]:
            for q in l:
                if q not in m:
                    c[1]=q
        p=p+1
    if c[2]==a[2] or c[2]==b[2] or c[2]==d[2] or c[2]==e[2] or c[2]==f[2] or c[2]==g[2] or c[2]==h[2] or c[2]==i[2]:
        m=[c[2],a[2],b[2],d[2],e[2],f[2],g[2],h[2],i[2]]
        if c[2]==a[2]:
            for q in l:
                if q not in m:
                    c[2]=q
        if c[2]==b[2]:
            for q in l:
                if q not in m:
                    c[2]=q
        if c[2]==d[2]:
            for q in l:
                if q not in m:
                    c[2]=q
        if c[2]==e[2]:
            for q in l:
                if q not in m:
                    c[2]=q
        if c[2]==f[2]:
            for q in l:
                if q not in m:
                    c[2]=q
        if c[2]==g[2]:
            for q in l:
                if q not in m:
                    c[2]=q
        if c[2]==h[2]:
            for q in l:
                if q not in m:
                    c[2]=q
        if c[2]==i[2]:
            for q in l:
                if q not in m:
                    c[2]=q
        p=p+1
    if c[3]==a[3] or c[3]==b[3] or c[3]==d[3] or c[3]==e[3] or c[3]==f[3] or c[3]==g[3] or c[3]==h[3] or c[3]==i[3]:
        m=[c[3],a[3],b[3],d[3],e[3],f[3],g[3],h[3],i[3]]
        if c[3]==a[3]:
            for q in l:
                if q not in m:
                    c[3]=q
        if c[3]==b[3]:
            for q in l:
                if q not in m:
                    c[3]=q
        if c[3]==d[3]:
            for q in l:
                if q not in m:
                    c[3]=q
        if c[3]==e[3]:
            for q in l:
                if q not in m:
                    c[3]=q
        if c[3]==f[3]:
            for q in l:
                if q not in m:
                    c[3]=q
        if c[3]==g[3]:
            for q in l:
                if q not in m:
                    c[3]=q
        if c[3]==h[3]:
            for q in l:
                if q not in m:
                    c[3]=q
        if c[3]==i[3]:
            for q in l:
                if q not in m:
                    c[3]=q
        p=p+1
    if c[4]==a[4] or c[4]==b[4] or c[4]==d[4] or c[4]==e[4] or c[4]==f[4] or c[4]==g[4] or c[4]==h[4] or c[4]==i[4]:
        m=[c[4],a[4],b[4],d[4],e[4],f[4],g[4],h[4],i[4]]
        if c[4]==a[4]:
            for q in l:
                if q not in m:
                    c[4]=q
        if c[4]==b[4]:
            for q in l:
                if q not in m:
                    c[4]=q
        if c[4]==d[4]:
            for q in l:
                if q not in m:
                    c[4]=q
        if c[4]==e[4]:
            for q in l:
                if q not in m:
                    c[4]=q
        if c[4]==f[4]:
            for q in l:
                if q not in m:
                    c[4]=q
        if c[4]==g[4]:
            for q in l:
                if q not in m:
                    c[4]=q
        if c[4]==h[4]:
            for q in l:
                if q not in m:
                    c[4]=q
        if c[4]==i[4]:
            for q in l:
                if q not in m:
                    c[4]=q
        p=p+1
    if c[5]==a[5] or c[5]==b[5] or c[5]==d[5] or c[5]==e[5] or c[5]==f[5] or c[5]==g[5] or c[5]==h[5] or c[5]==i[5]:
        m=[c[5],a[5],b[5],d[5],e[5],f[5],g[5],h[5],i[5]]
        if c[5]==a[5]:
            for q in l:
                if q not in m:
                    c[5]=q
        if c[5]==b[5]:
            for q in l:
                if q not in m:
                    c[5]=q
        if c[5]==d[5]:
            for q in l:
                if q not in m:
                    c[5]=q
        if c[5]==e[5]:
            for q in l:
                if q not in m:
                    c[5]=q
        if c[5]==f[5]:
            for q in l:
                if q not in m:
                    c[5]=q
        if c[5]==g[5]:
            for q in l:
                if q not in m:
                    c[5]=q
        if c[5]==h[5]:
            for q in l:
                if q not in m:
                    c[5]=q
        if c[5]==i[5]:
            for q in l:
                if q not in m:
                    c[5]=q
        p=p+1
    if c[6]==a[6] or c[6]==b[6] or c[6]==d[6] or c[6]==e[6] or c[6]==f[6] or c[6]==g[6] or c[6]==h[6] or c[6]==i[6]:
        m=[c[6],a[6],b[6],d[6],e[6],f[6],g[6],h[6],i[6]]
        if c[6]==a[6]:
            for q in l:
                if q not in m:
                    c[6]=q
        if c[6]==b[6]:
            for q in l:
                if q not in m:
                    c[6]=q
        if c[6]==d[6]:
            for q in l:
                if q not in m:
                    c[6]=q
        if c[6]==e[6]:
            for q in l:
                if q not in m:
                    c[6]=q
        if c[6]==f[6]:
            for q in l:
                if q not in m:
                    c[6]=q
        if c[6]==g[6]:
            for q in l:
                if q not in m:
                    c[6]=q
        if c[6]==h[6]:
            for q in l:
                if q not in m:
                    c[6]=q
        if c[6]==i[6]:
            for q in l:
                if q not in m:
                    c[6]=q
        p=p+1
    if c[7]==a[7] or c[7]==b[7] or c[7]==d[7] or c[7]==e[7] or c[7]==f[7] or c[7]==g[7] or c[7]==h[7] or c[7]==i[7]:
        m=[c[7],a[7],b[7],d[7],e[7],f[7],g[7],h[7],i[7]]
        if c[7]==a[7]:
            for q in l:
                if q not in m:
                    c[7]=q
        if c[7]==b[7]:
            for q in l:
                if q not in m:
                    c[7]=q
        if c[7]==d[7]:
            for q in l:
                if q not in m:
                    c[7]=q
        if c[7]==e[7]:
            for q in l:
                if q not in m:
                    c[7]=q
        if c[7]==f[7]:
            for q in l:
                if q not in m:
                    c[7]=q
        if c[7]==g[7]:
            for q in l:
                if q not in m:
                    c[7]=q
        if c[7]==h[7]:
            for q in l:
                if q not in m:
                    c[7]=q
        if c[7]==i[7]:
            for q in l:
                if q not in m:
                    c[7]=q
        p=p+1
    if c[8]==a[8] or c[8]==b[8] or c[8]==d[8] or c[8]==e[8] or c[8]==f[8] or c[8]==g[8] or c[8]==h[8] or c[8]==i[8]:
        m=[c[8],a[8],b[8],d[8],e[8],f[8],g[8],h[8],i[8]]
        if c[8]==a[8]:
            for q in l:
                if q not in m:
                    c[8]=q
        if c[8]==b[8]:
            for q in l:
                if q not in m:
                    c[8]=q
        if c[8]==d[8]:
            for q in l:
                if q not in m:
                    c[8]=q
        if c[8]==e[8]:
            for q in l:
                if q not in m:
                    c[8]=q
        if c[8]==f[8]:
            for q in l:
                if q not in m:
                    c[8]=q
        if c[8]==g[8]:
            for q in l:
                if q not in m:
                    c[8]=q
        if c[8]==h[8]:
            for q in l:
                if q not in m:
                    c[8]=q
        if c[8]==i[8]:
            for q in l:
                if q not in m:
                    c[8]=q
        p=p+1
    if d[0]==a[0] or d[0]==b[0] or d[0]==c[0] or d[0]==e[0] or d[0]==f[0] or d[0]==g[0] or d[0]==h[0] or d[0]==i[0]:
        m=[d[0],a[0],b[0],c[0],e[0],f[0],g[0],h[0],i[0]]
        if d[0]==a[0]:
            for q in l:
                if q not in m:
                    d[0]=q
        if d[0]==b[0]:
            for q in l:
                if q not in m:
                    d[0]=q
        if d[0]==c[0]:
            for q in l:
                if q not in m:
                    d[0]=q
        if d[0]==e[0]:
            for q in l:
                if q not in m:
                    d[0]=q
        if d[0]==f[0]:
            for q in l:
                if q not in m:
                    d[0]=q
        if d[0]==g[0]:
            for q in l:
                if q not in m:
                    d[0]=q
        if d[0]==h[0]:
            for q in l:
                if q not in m:
                    d[0]=q
        if d[0]==i[0]:
            for q in l:
                if q not in m:
                    d[0]=q
        p=p+1
    if d[1]==a[1] or d[1]==b[1] or d[1]==c[1] or d[1]==e[1] or d[1]==f[1] or d[1]==g[1] or d[1]==h[1] or d[1]==i[1]:
        m=[d[1],a[1],b[1],c[1],e[1],f[1],g[1],h[1],i[1]]
        if d[1]==a[1]:
            for q in l:
                if q not in m:
                    d[1]=q
        if d[1]==b[1]:
            for q in l:
                if q not in m:
                    d[1]=q
        if d[1]==c[1]:
            for q in l:
                if q not in m:
                    d[1]=q
        if d[1]==e[1]:
            for q in l:
                if q not in m:
                    d[1]=q
        if d[1]==f[1]:
            for q in l:
                if q not in m:
                    d[1]=q
        if d[1]==g[1]:
            for q in l:
                if q not in m:
                    d[1]=q
        if d[1]==h[1]:
            for q in l:
                if q not in m:
                    d[1]=q
        if d[1]==i[1]:
            for q in l:
                if q not in m:
                    d[1]=q
        p=p+1
    if d[2]==a[2] or d[2]==b[2] or d[2]==c[2] or d[2]==e[2] or d[2]==f[2] or d[2]==g[2] or d[2]==h[2] or d[2]==i[2]:
        m=[d[2],a[2],b[2],c[2],e[2],f[2],g[2],h[2],i[2]]
        if d[2]==a[2]:
            for q in l:
                if q not in m:
                    d[2]=q
        if d[2]==b[2]:
            for q in l:
                if q not in m:
                    d[2]=q
        if d[2]==c[2]:
            for q in l:
                if q not in m:
                    d[2]=q
        if d[2]==e[2]:
            for q in l:
                if q not in m:
                    d[2]=q
        if d[2]==f[2]:
            for q in l:
                if q not in m:
                    d[2]=q
        if d[2]==g[2]:
            for q in l:
                if q not in m:
                    d[2]=q
        if d[2]==h[2]:
            for q in l:
                if q not in m:
                    d[2]=q
        if d[2]==i[2]:
            for q in l:
                if q not in m:
                    d[2]=q
        p=p+1
    if d[3]==a[3] or d[3]==b[3] or d[3]==c[3] or d[3]==e[3] or d[3]==f[3] or d[3]==g[3] or d[3]==h[3] or d[3]==i[3]:
        m=[d[3],a[3],b[3],c[3],e[3],f[3],g[3],h[3],i[3]]
        if d[3]==a[3]:
            for q in l:
                if q not in m:
                    d[3]=q
        if d[3]==b[3]:
            for q in l:
                if q not in m:
                    d[3]=q
        if d[3]==c[3]:
            for q in l:
                if q not in m:
                    d[3]=q
        if d[3]==e[3]:
            for q in l:
                if q not in m:
                    d[3]=q
        if d[3]==f[3]:
            for q in l:
                if q not in m:
                    d[3]=q
        if d[3]==g[3]:
            for q in l:
                if q not in m:
                    d[3]=q
        if d[3]==h[3]:
            for q in l:
                if q not in m:
                    d[3]=q
        if d[3]==i[3]:
            for q in l:
                if q not in m:
                    d[3]=q
        p=p+1
    if d[4]==a[4] or d[4]==b[4] or d[4]==c[4] or d[4]==e[4] or d[4]==f[4] or d[4]==g[4] or d[4]==h[4] or d[4]==i[4]:
        m=[d[4],a[4],b[4],c[4],e[4],f[4],g[4],h[4],i[4]]
        if d[4]==a[4]:
            for q in l:
                if q not in m:
                    d[4]=q
        if d[4]==b[4]:
            for q in l:
                if q not in m:
                    d[4]=q
        if d[4]==c[4]:
            for q in l:
                if q not in m:
                    d[4]=q
        if d[4]==e[4]:
            for q in l:
                if q not in m:
                    d[4]=q
        if d[4]==f[4]:
            for q in l:
                if q not in m:
                    d[4]=q
        if d[4]==g[4]:
            for q in l:
                if q not in m:
                    d[4]=q
        if d[4]==h[4]:
            for q in l:
                if q not in m:
                    d[4]=q
        if d[4]==i[4]:
            for q in l:
                if q not in m:
                    d[4]=q
        p=p+1
    if d[5]==a[5] or d[5]==b[5] or d[5]==c[5] or d[5]==e[5] or d[5]==f[5] or d[5]==g[5] or d[5]==h[5] or d[5]==i[5]:
        m=[d[5],a[5],b[5],c[5],e[5],f[5],g[5],h[5],i[5]]
        if d[5]==a[5]:
            for q in l:
                if q not in m:
                    d[5]=q
        if d[5]==b[5]:
            for q in l:
                if q not in m:
                    d[5]=q
        if d[5]==c[5]:
            for q in l:
                if q not in m:
                    d[5]=q
        if d[5]==e[5]:
            for q in l:
                if q not in m:
                    d[5]=q
        if d[5]==f[5]:
            for q in l:
                if q not in m:
                    d[5]=q
        if d[5]==g[5]:
            for q in l:
                if q not in m:
                    d[5]=q
        if d[5]==h[5]:
            for q in l:
                if q not in m:
                    d[5]=q
        if d[5]==i[5]:
            for q in l:
                if q not in m:
                    d[5]=q
        p=p+1
    if d[6]==a[6] or d[6]==b[6] or d[6]==c[6] or d[6]==e[6] or d[6]==f[6] or d[6]==g[6] or d[6]==h[6] or d[6]==i[6]:
        m=[d[6],a[6],b[6],c[6],e[6],f[6],g[6],h[6],i[6]]
        if d[6]==a[6]:
            for q in l:
                if q not in m:
                    d[6]=q
        if d[6]==b[6]:
            for q in l:
                if q not in m:
                    d[6]=q
        if d[6]==c[6]:
            for q in l:
                if q not in m:
                    d[6]=q
        if d[6]==e[6]:
            for q in l:
                if q not in m:
                    d[6]=q
        if d[6]==f[6]:
            for q in l:
                if q not in m:
                    d[6]=q
        if d[6]==g[6]:
            for q in l:
                if q not in m:
                    d[6]=q
        if d[6]==h[6]:
            for q in l:
                if q not in m:
                    d[6]=q
        if d[6]==i[6]:
            for q in l:
                if q not in m:
                    d[6]=q
        p=p+1
    if d[7]==a[7] or d[7]==b[7] or d[7]==c[7] or d[7]==e[7] or d[7]==f[7] or d[7]==g[7] or d[7]==h[7] or d[7]==i[7]:
        m=[d[7],a[7],b[7],c[7],e[7],f[7],g[7],h[7],i[7]]
        if d[7]==a[7]:
            for q in l:
                if q not in m:
                    d[7]=q
        if d[7]==b[7]:
            for q in l:
                if q not in m:
                    d[7]=q
        if d[7]==c[7]:
            for q in l:
                if q not in m:
                    d[7]=q
        if d[7]==e[7]:
            for q in l:
                if q not in m:
                    d[7]=q
        if d[7]==f[7]:
            for q in l:
                if q not in m:
                    d[7]=q
        if d[7]==g[7]:
            for q in l:
                if q not in m:
                    d[7]=q
        if d[7]==h[7]:
            for q in l:
                if q not in m:
                    d[7]=q
        if d[7]==i[7]:
            for q in l:
                if q not in m:
                    d[7]=q
        p=p+1
    if d[8]==a[8] or d[8]==b[8] or d[8]==c[8] or d[8]==e[8] or d[8]==f[8] or d[8]==g[8] or d[8]==h[8] or d[8]==i[8]:
        m=[d[8],a[8],b[8],c[8],e[8],f[8],g[8],h[8],i[8]]
        if d[8]==a[8]:
            for q in l:
                if q not in m:
                    d[8]=q
        if d[8]==b[8]:
            for q in l:
                if q not in m:
                    d[8]=q
        if d[8]==c[8]:
            for q in l:
                if q not in m:
                    d[8]=q
        if d[8]==e[8]:
            for q in l:
                if q not in m:
                    d[8]=q
        if d[8]==f[8]:
            for q in l:
                if q not in m:
                    d[8]=q
        if d[8]==g[8]:
            for q in l:
                if q not in m:
                    d[8]=q
        if d[8]==h[8]:
            for q in l:
                if q not in m:
                    d[8]=q
        if d[8]==i[8]:
            for q in l:
                if q not in m:
                    d[8]=q
        p=p+1
    if e[0]==a[0] or e[0]==b[0] or e[0]==c[0] or e[0]==d[0] or e[0]==f[0] or e[0]==g[0] or e[0]==h[0] or e[0]==i[0]:
        m=[e[0],a[0],b[0],c[0],d[0],f[0],g[0],h[0],i[0]]
        if e[0]==a[0]:
            for q in l:
                if q not in m:
                    e[0]=q
        if e[0]==b[0]:
            for q in l:
                if q not in m:
                    e[0]=q
        if e[0]==c[0]:
            for q in l:
                if q not in m:
                    e[0]=q
        if e[0]==d[0]:
            for q in l:
                if q not in m:
                    e[0]=q
        if e[0]==f[0]:
            for q in l:
                if q not in m:
                    e[0]=q
        if e[0]==g[0]:
            for q in l:
                if q not in m:
                    e[0]=q
        if e[0]==h[0]:
            for q in l:
                if q not in m:
                    e[0]=q
        if e[0]==i[0]:
            for q in l:
                if q not in m:
                    e[0]=q
        p=p+1
    if e[1]==a[1] or e[1]==b[1] or e[1]==c[1] or e[1]==d[1] or e[1]==f[1] or e[1]==g[1] or e[1]==h[1] or e[1]==i[1]:
        m=[e[1],a[1],b[1],c[1],d[1],f[1],g[1],h[1],i[1]]
        if e[1]==a[1]:
            for q in l:
                if q not in m:
                    e[1]=q
        if e[1]==b[1]:
            for q in l:
                if q not in m:
                    e[1]=q
        if e[1]==c[1]:
            for q in l:
                if q not in m:
                    e[1]=q
        if e[1]==d[1]:
            for q in l:
                if q not in m:
                    e[1]=q
        if e[1]==f[1]:
            for q in l:
                if q not in m:
                    e[1]=q
        if e[1]==g[1]:
            for q in l:
                if q not in m:
                    e[1]=q
        if e[1]==h[1]:
            for q in l:
                if q not in m:
                    e[1]=q
        if e[1]==i[1]:
            for q in l:
                if q not in m:
                    e[1]=q
        p=p+1
    if e[2]==a[2] or e[2]==b[2] or e[2]==c[2] or e[2]==d[2] or e[2]==f[2] or e[2]==g[2] or e[2]==h[2] or e[2]==i[2]:
        m=[e[2],a[2],b[2],c[2],d[2],f[2],g[2],h[2],i[2]]
        if e[2]==a[2]:
            for q in l:
                if q not in m:
                    e[2]=q
        if e[2]==b[2]:
            for q in l:
                if q not in m:
                    e[2]=q
        if e[2]==c[2]:
            for q in l:
                if q not in m:
                    e[2]=q
        if e[2]==d[2]:
            for q in l:
                if q not in m:
                    e[2]=q
        if e[2]==f[2]:
            for q in l:
                if q not in m:
                    e[2]=q
        if e[2]==g[2]:
            for q in l:
                if q not in m:
                    e[2]=q
        if e[2]==h[2]:
            for q in l:
                if q not in m:
                    e[2]=q
        if e[2]==i[2]:
            for q in l:
                if q not in m:
                    e[2]=q
        p=p+1
    if e[3]==a[3] or e[3]==b[3] or e[3]==c[3] or e[3]==d[3] or e[3]==f[3] or e[3]==g[3] or e[3]==h[3] or e[3]==i[3]:
        m=[e[3],a[3],b[3],c[3],d[3],f[3],g[3],h[3],i[3]]
        if e[3]==a[3]:
            for q in l:
                if q not in m:
                    e[3]=q
        if e[3]==b[3]:
            for q in l:
                if q not in m:
                    e[3]=q
        if e[3]==c[3]:
            for q in l:
                if q not in m:
                    e[3]=q
        if e[3]==d[3]:
            for q in l:
                if q not in m:
                    e[3]=q
        if e[3]==f[3]:
            for q in l:
                if q not in m:
                    e[3]=q
        if e[3]==g[3]:
            for q in l:
                if q not in m:
                    e[3]=q
        if e[3]==h[3]:
            for q in l:
                if q not in m:
                    e[3]=q
        if e[3]==i[3]:
            for q in l:
                if q not in m:
                    e[3]=q
        p=p+1
    if e[4]==a[4] or e[4]==b[4] or e[4]==c[4] or e[4]==d[4] or e[4]==f[4] or e[4]==g[4] or e[4]==h[4] or e[4]==i[4]:
        m=[e[4],a[4],b[4],c[4],d[4],f[4],g[4],h[4],i[4]]
        if e[4]==a[4]:
            for q in l:
                if q not in m:
                    e[4]=q
        if e[4]==b[4]:
            for q in l:
                if q not in m:
                    e[4]=q
        if e[4]==c[4]:
            for q in l:
                if q not in m:
                    e[4]=q
        if e[4]==d[4]:
            for q in l:
                if q not in m:
                    e[4]=q
        if e[4]==f[4]:
            for q in l:
                if q not in m:
                    e[4]=q
        if e[4]==g[4]:
            for q in l:
                if q not in m:
                    e[4]=q
        if e[4]==h[4]:
            for q in l:
                if q not in m:
                    e[4]=q
        if e[4]==i[4]:
            for q in l:
                if q not in m:
                    e[4]=q
        p=p+1
    if e[5]==a[5] or e[5]==b[5] or e[5]==c[5] or e[5]==d[5] or e[5]==f[5] or e[5]==g[5] or e[5]==h[5] or e[5]==i[5]:
        m=[e[5],a[5],b[5],c[5],d[5],f[5],g[5],h[5],i[5]]
        if e[5]==a[5]:
            for q in l:
                if q not in m:
                    e[5]=q
        if e[5]==b[5]:
            for q in l:
                if q not in m:
                    e[5]=q
        if e[5]==c[5]:
            for q in l:
                if q not in m:
                    e[5]=q
        if e[5]==d[5]:
            for q in l:
                if q not in m:
                    e[5]=q
        if e[5]==f[5]:
            for q in l:
                if q not in m:
                    e[5]=q
        if e[5]==g[5]:
            for q in l:
                if q not in m:
                    e[5]=q
        if e[5]==h[5]:
            for q in l:
                if q not in m:
                    e[5]=q
        if e[5]==i[5]:
            for q in l:
                if q not in m:
                    e[5]=q
        p=p+1
    if e[6]==a[6] or e[6]==b[6] or e[6]==c[6] or e[6]==d[6] or e[6]==f[6] or e[6]==g[6] or e[6]==h[6] or e[6]==i[6]:
        m=[e[6],a[6],b[6],c[6],d[6],f[6],g[6],h[6],i[6]]
        if e[6]==a[6]:
            for q in l:
                if q not in m:
                    e[6]=q
        if e[6]==b[6]:
            for q in l:
                if q not in m:
                    e[6]=q
        if e[6]==c[6]:
            for q in l:
                if q not in m:
                    e[6]=q
        if e[6]==d[6]:
            for q in l:
                if q not in m:
                    e[6]=q
        if e[6]==f[6]:
            for q in l:
                if q not in m:
                    e[6]=q
        if e[6]==g[6]:
            for q in l:
                if q not in m:
                    e[6]=q
        if e[6]==h[6]:
            for q in l:
                if q not in m:
                    e[6]=q
        if e[6]==i[6]:
            for q in l:
                if q not in m:
                    e[6]=q
        p=p+1
    if e[7]==a[7] or e[7]==b[7] or e[7]==c[7] or e[7]==d[7] or e[7]==f[7] or e[7]==g[7] or e[7]==h[7] or e[7]==i[7]:
        m=[e[7],a[7],b[7],c[7],d[7],f[7],g[7],h[7],i[7]]
        if e[7]==a[7]:
            for q in l:
                if q not in m:
                    e[7]=q
        if e[7]==b[7]:
            for q in l:
                if q not in m:
                    e[7]=q
        if e[7]==c[7]:
            for q in l:
                if q not in m:
                    e[7]=q
        if e[7]==d[7]:
            for q in l:
                if q not in m:
                    e[7]=q
        if e[7]==f[7]:
            for q in l:
                if q not in m:
                    e[7]=q
        if e[7]==g[7]:
            for q in l:
                if q not in m:
                    e[7]=q
        if e[7]==h[7]:
            for q in l:
                if q not in m:
                    e[7]=q
        if e[7]==i[7]:
            for q in l:
                if q not in m:
                    e[7]=q
        p=p+1
    if e[8]==a[8] or e[8]==b[8] or e[8]==c[8] or e[8]==d[8] or e[8]==f[8] or e[8]==g[8] or e[8]==h[8] or e[8]==i[8]:
        m=[e[8],a[8],b[8],c[8],d[8],f[8],g[8],h[8],i[8]]
        if e[8]==a[8]:
            for q in l:
                if q not in m:
                    e[8]=q
        if e[8]==b[8]:
            for q in l:
                if q not in m:
                    e[8]=q
        if e[8]==c[8]:
            for q in l:
                if q not in m:
                    e[8]=q
        if e[8]==d[8]:
            for q in l:
                if q not in m:
                    e[8]=q
        if e[8]==f[8]:
            for q in l:
                if q not in m:
                    e[8]=q
        if e[8]==g[8]:
            for q in l:
                if q not in m:
                    e[8]=q
        if e[8]==h[8]:
            for q in l:
                if q not in m:
                    e[8]=q
        if e[8]==i[8]:
            for q in l:
                if q not in m:
                    e[8]=q
        p=p+1
    if f[0]==a[0] or f[0]==b[0] or f[0]==c[0] or f[0]==d[0] or f[0]==e[0] or f[0]==g[0] or f[0]==h[0] or f[0]==i[0]:
        m=[f[0],a[0],b[0],c[0],d[0],e[0],g[0],h[0],i[0]]
        if f[0]==a[0]:
            for q in l:
                if q not in m:
                    f[0]=q
        if f[0]==b[0]:
            for q in l:
                if q not in m:
                    f[0]=q
        if f[0]==c[0]:
            for q in l:
                if q not in m:
                    f[0]=q
        if f[0]==d[0]:
            for q in l:
                if q not in m:
                    f[0]=q
        if f[0]==e[0]:
            for q in l:
                if q not in m:
                    f[0]=q
        if f[0]==g[0]:
            for q in l:
                if q not in m:
                    f[0]=q
        if f[0]==h[0]:
            for q in l:
                if q not in m:
                    f[0]=q
        if f[0]==i[0]:
            for q in l:
                if q not in m:
                    f[0]=q
        p=p+1
    if f[1]==a[1] or f[1]==b[1] or f[1]==c[1] or f[1]==d[1] or f[1]==e[1] or f[1]==g[1] or f[1]==h[1] or f[1]==i[1]:
        m=[f[1],a[1],b[1],c[1],d[1],e[1],g[1],h[1],i[1]]
        if f[1]==a[1]:
            for q in l:
                if q not in m:
                    f[1]=q
        if f[1]==b[1]:
            for q in l:
                if q not in m:
                    f[1]=q
        if f[1]==c[1]:
            for q in l:
                if q not in m:
                    f[1]=q
        if f[1]==d[1]:
            for q in l:
                if q not in m:
                    f[1]=q
        if f[1]==e[1]:
            for q in l:
                if q not in m:
                    f[1]=q
        if f[1]==g[1]:
            for q in l:
                if q not in m:
                    f[1]=q
        if f[1]==h[1]:
            for q in l:
                if q not in m:
                    f[1]=q
        if f[1]==i[1]:
            for q in l:
                if q not in m:
                    f[1]=q
        p=p+1
    if f[2]==a[2] or f[2]==b[2] or f[2]==c[2] or f[2]==d[2] or f[2]==e[2] or f[2]==g[2] or f[2]==h[2] or f[2]==i[2]:
        m=[f[2],a[2],b[2],c[2],d[2],e[2],g[2],h[2],i[2]]
        if f[2]==a[2]:
            for q in l:
                if q not in m:
                    f[2]=q
        if f[2]==b[2]:
            for q in l:
                if q not in m:
                    f[2]=q
        if f[2]==c[2]:
            for q in l:
                if q not in m:
                    f[2]=q
        if f[2]==d[2]:
            for q in l:
                if q not in m:
                    f[2]=q
        if f[2]==e[2]:
            for q in l:
                if q not in m:
                    f[2]=q
        if f[2]==g[2]:
            for q in l:
                if q not in m:
                    f[2]=q
        if f[2]==h[2]:
            for q in l:
                if q not in m:
                    f[2]=q
        if f[2]==i[2]:
            for q in l:
                if q not in m:
                    f[2]=q
        p=p+1
    if f[3]==a[3] or f[3]==b[3] or f[3]==c[3] or f[3]==d[3] or f[3]==e[3] or f[3]==g[3] or f[3]==h[3] or f[3]==i[3]:
        m=[f[3],a[3],b[3],c[3],d[3],e[3],g[3],h[3],i[3]]
        if f[3]==a[3]:
            for q in l:
                if q not in m:
                    f[3]=q
        if f[3]==b[3]:
            for q in l:
                if q not in m:
                    f[3]=q
        if f[3]==c[3]:
            for q in l:
                if q not in m:
                    f[3]=q
        if f[3]==d[3]:
            for q in l:
                if q not in m:
                    f[3]=q
        if f[3]==e[3]:
            for q in l:
                if q not in m:
                    f[3]=q
        if f[3]==g[3]:
            for q in l:
                if q not in m:
                    f[3]=q
        if f[3]==h[3]:
            for q in l:
                if q not in m:
                    f[3]=q
        if f[3]==i[3]:
            for q in l:
                if q not in m:
                    f[3]=q
        p=p+1
    if f[4]==a[4] or f[4]==b[4] or f[4]==c[4] or f[4]==d[4] or f[4]==e[4] or f[4]==g[4] or f[4]==h[4] or f[4]==i[4]:
        m=[f[4],a[4],b[4],c[4],d[4],e[4],g[4],h[4],i[4]]
        if f[4]==a[4]:
            for q in l:
                if q not in m:
                    f[4]=q
        if f[4]==b[4]:
            for q in l:
                if q not in m:
                    f[4]=q
        if f[4]==c[4]:
            for q in l:
                if q not in m:
                    f[4]=q
        if f[4]==d[4]:
            for q in l:
                if q not in m:
                    f[4]=q
        if f[4]==e[4]:
            for q in l:
                if q not in m:
                    f[4]=q
        if f[4]==g[4]:
            for q in l:
                if q not in m:
                    f[4]=q
        if f[4]==h[4]:
            for q in l:
                if q not in m:
                    f[4]=q
        if f[4]==i[4]:
            for q in l:
                if q not in m:
                    f[4]=q
        p=p+1
    if f[5]==a[5] or f[5]==b[5] or f[5]==c[5] or f[5]==d[5] or f[5]==e[5] or f[5]==g[5] or f[5]==h[5] or f[5]==i[5]:
        m=[f[5],a[5],b[5],c[5],d[5],e[5],g[5],h[5],i[5]]
        if f[5]==a[5]:
            for q in l:
                if q not in m:
                    f[5]=q
        if f[5]==b[5]:
            for q in l:
                if q not in m:
                    f[5]=q
        if f[5]==c[5]:
            for q in l:
                if q not in m:
                    f[5]=q
        if f[5]==d[5]:
            for q in l:
                if q not in m:
                    f[5]=q
        if f[5]==e[5]:
            for q in l:
                if q not in m:
                    f[5]=q
        if f[5]==g[5]:
            for q in l:
                if q not in m:
                    f[5]=q
        if f[5]==h[5]:
            for q in l:
                if q not in m:
                    f[5]=q
        if f[5]==i[5]:
            for q in l:
                if q not in m:
                    f[5]=q
        p=p+1
    if f[6]==a[6] or f[6]==b[6] or f[6]==c[6] or f[6]==d[6] or f[6]==e[6] or f[6]==g[6] or f[6]==h[6] or f[6]==i[6]:
        m=[f[6],a[6],b[6],c[6],d[6],e[6],g[6],h[6],i[6]]
        if f[6]==a[6]:
            for q in l:
                if q not in m:
                    f[6]=q
        if f[6]==b[6]:
            for q in l:
                if q not in m:
                    f[6]=q
        if f[6]==c[6]:
            for q in l:
                if q not in m:
                    f[6]=q
        if f[6]==d[6]:
            for q in l:
                if q not in m:
                    f[6]=q
        if f[6]==e[6]:
            for q in l:
                if q not in m:
                    f[6]=q
        if f[6]==g[6]:
            for q in l:
                if q not in m:
                    f[6]=q
        if f[6]==h[6]:
            for q in l:
                if q not in m:
                    f[6]=q
        if f[6]==i[6]:
            for q in l:
                if q not in m:
                    f[6]=q
        p=p+1
    if f[7]==a[7] or f[7]==b[7] or f[7]==c[7] or f[7]==d[7] or f[7]==e[7] or f[7]==g[7] or f[7]==h[7] or f[7]==i[7]:
        m=[f[7],a[7],b[7],c[7],d[7],e[7],g[7],h[7],i[7]]
        if f[7]==a[7]:
            for q in l:
                if q not in m:
                    f[7]=q
        if f[7]==b[7]:
            for q in l:
                if q not in m:
                    f[7]=q
        if f[7]==c[7]:
            for q in l:
                if q not in m:
                    f[7]=q
        if f[7]==d[7]:
            for q in l:
                if q not in m:
                    f[7]=q
        if f[7]==e[7]:
            for q in l:
                if q not in m:
                    f[7]=q
        if f[7]==g[7]:
            for q in l:
                if q not in m:
                    f[7]=q
        if f[7]==h[7]:
            for q in l:
                if q not in m:
                    f[7]=q
        if f[7]==i[7]:
            for q in l:
                if q not in m:
                    f[7]=q
        p=p+1
    if f[8]==a[8] or f[8]==b[8] or f[8]==c[8] or f[8]==d[8] or f[8]==e[8] or f[8]==g[8] or f[8]==h[8] or f[8]==i[8]:
        m=[f[8],a[8],b[8],c[8],d[8],e[8],g[8],h[8],i[8]]
        if f[8]==a[8]:
            for q in l:
                if q not in m:
                    f[8]=q
        if f[8]==b[8]:
            for q in l:
                if q not in m:
                    f[8]=q
        if f[8]==c[8]:
            for q in l:
                if q not in m:
                    f[8]=q
        if f[8]==d[8]:
            for q in l:
                if q not in m:
                    f[8]=q
        if f[8]==e[8]:
            for q in l:
                if q not in m:
                    f[8]=q
        if f[8]==g[8]:
            for q in l:
                if q not in m:
                    f[8]=q
        if f[8]==h[8]:
            for q in l:
                if q not in m:
                    f[8]=q
        if f[8]==i[8]:
            for q in l:
                if q not in m:
                    f[8]=q
        p=p+1
    if g[0]==a[0] or g[0]==b[0] or g[0]==c[0] or g[0]==d[0] or g[0]==e[0] or g[0]==f[0] or g[0]==h[0] or g[0]==i[0]:
        m=[g[0],a[0],b[0],c[0],d[0],e[0],f[0],h[0],i[0]]
        if g[0]==a[0]:
            for q in l:
                if q not in m:
                    g[0]=q
        if g[0]==b[0]:
            for q in l:
                if q not in m:
                    g[0]=q
        if g[0]==c[0]:
            for q in l:
                if q not in m:
                    g[0]=q
        if g[0]==d[0]:
            for q in l:
                if q not in m:
                    g[0]=q
        if g[0]==e[0]:
            for q in l:
                if q not in m:
                    g[0]=q
        if g[0]==f[0]:
            for q in l:
                if q not in m:
                    g[0]=q
        if g[0]==h[0]:
            for q in l:
                if q not in m:
                    g[0]=q
        if g[0]==i[0]:
            for q in l:
                if q not in m:
                    g[0]=q
        p=p+1
    if g[1]==a[1] or g[1]==b[1] or g[1]==c[1] or g[1]==d[1] or g[1]==e[1] or g[1]==f[1] or g[1]==h[1] or g[1]==i[1]:
        m=[g[1],a[1],b[1],c[1],d[1],e[1],f[1],h[1],i[1]]
        if g[1]==a[1]:
            for q in l:
                if q not in m:
                    g[1]=q
        if g[1]==b[1]:
            for q in l:
                if q not in m:
                    g[1]=q
        if g[1]==c[1]:
            for q in l:
                if q not in m:
                    g[1]=q
        if g[1]==d[1]:
            for q in l:
                if q not in m:
                    g[1]=q
        if g[1]==e[1]:
            for q in l:
                if q not in m:
                    g[1]=q
        if g[1]==f[1]:
            for q in l:
                if q not in m:
                    g[1]=q
        if g[1]==h[1]:
            for q in l:
                if q not in m:
                    g[1]=q
        if g[1]==i[1]:
            for q in l:
                if q not in m:
                    g[1]=q
        p=p+1
    if g[2]==a[2] or g[2]==b[2] or g[2]==c[2] or g[2]==d[2] or g[2]==e[2] or g[2]==f[2] or g[2]==h[2] or g[2]==i[2]:
        m=[g[2],a[2],b[2],c[2],d[2],e[2],f[2],h[2],i[2]]
        if g[2]==a[2]:
            for q in l:
                if q not in m:
                    g[2]=q
        if g[2]==b[2]:
            for q in l:
                if q not in m:
                    g[2]=q
        if g[2]==c[2]:
            for q in l:
                if q not in m:
                    g[2]=q
        if g[2]==d[2]:
            for q in l:
                if q not in m:
                    g[2]=q
        if g[2]==e[2]:
            for q in l:
                if q not in m:
                    g[2]=q
        if g[2]==f[2]:
            for q in l:
                if q not in m:
                    g[2]=q
        if g[2]==h[2]:
            for q in l:
                if q not in m:
                    g[2]=q
        if g[2]==i[2]:
            for q in l:
                if q not in m:
                    g[2]=q
        p=p+1
    if g[3]==a[3] or g[3]==b[3] or g[3]==c[3] or g[3]==d[3] or g[3]==e[3] or g[3]==f[3] or g[3]==h[3] or g[3]==i[3]:
        m=[g[3],a[3],b[3],c[3],d[3],e[3],f[3],h[3],i[3]]
        if g[3]==a[3]:
            for q in l:
                if q not in m:
                    g[3]=q
        if g[3]==b[3]:
            for q in l:
                if q not in m:
                    g[3]=q
        if g[3]==c[3]:
            for q in l:
                if q not in m:
                    g[3]=q
        if g[3]==d[3]:
            for q in l:
                if q not in m:
                    g[3]=q
        if g[3]==e[3]:
            for q in l:
                if q not in m:
                    g[3]=q
        if g[3]==f[3]:
            for q in l:
                if q not in m:
                    g[3]=q
        if g[3]==h[3]:
            for q in l:
                if q not in m:
                    g[3]=q
        if g[3]==i[3]:
            for q in l:
                if q not in m:
                    g[3]=q
        p=p+1
    if g[4]==a[4] or g[4]==b[4] or g[4]==c[4] or g[4]==d[4] or g[4]==e[4] or g[4]==f[4] or g[4]==h[4] or g[4]==i[4]:
        m=[g[4],a[4],b[4],c[4],d[4],e[4],f[4],h[4],i[4]]
        if g[4]==a[4]:
            for q in l:
                if q not in m:
                    g[4]=q
        if g[4]==b[4]:
            for q in l:
                if q not in m:
                    g[4]=q
        if g[4]==c[4]:
            for q in l:
                if q not in m:
                    g[4]=q
        if g[4]==d[4]:
            for q in l:
                if q not in m:
                    g[4]=q
        if g[4]==e[4]:
            for q in l:
                if q not in m:
                    g[4]=q
        if g[4]==f[4]:
            for q in l:
                if q not in m:
                    g[4]=q
        if g[4]==h[4]:
            for q in l:
                if q not in m:
                    g[4]=q
        if g[4]==i[4]:
            for q in l:
                if q not in m:
                    g[4]=q
        p=p+1
    if g[5]==a[5] or g[5]==b[5] or g[5]==c[5] or g[5]==d[5] or g[5]==e[5] or g[5]==f[5] or g[5]==h[5] or g[5]==i[5]:
        m=[g[5],a[5],b[5],c[5],d[5],e[5],f[5],h[5],i[5]]
        if g[5]==a[5]:
            for q in l:
                if q not in m:
                    g[5]=q
        if g[5]==b[5]:
            for q in l:
                if q not in m:
                    g[5]=q
        if g[5]==c[5]:
            for q in l:
                if q not in m:
                    g[5]=q
        if g[5]==d[5]:
            for q in l:
                if q not in m:
                    g[5]=q
        if g[5]==e[5]:
            for q in l:
                if q not in m:
                    g[5]=q
        if g[5]==f[5]:
            for q in l:
                if q not in m:
                    g[5]=q
        if g[5]==h[5]:
            for q in l:
                if q not in m:
                    g[5]=q
        if g[5]==i[5]:
            for q in l:
                if q not in m:
                    g[5]=q
        p=p+1
    if g[6]==a[6] or g[6]==b[6] or g[6]==c[6] or g[6]==d[6] or g[6]==e[6] or g[6]==f[6] or g[6]==h[6] or g[6]==i[6]:
        m=[g[6],a[6],b[6],c[6],d[6],e[6],f[6],h[6],i[6]]
        if g[6]==a[6]:
            for q in l:
                if q not in m:
                    g[6]=q
        if g[6]==b[6]:
            for q in l:
                if q not in m:
                    g[6]=q
        if g[6]==c[6]:
            for q in l:
                if q not in m:
                    g[6]=q
        if g[6]==d[6]:
            for q in l:
                if q not in m:
                    g[6]=q
        if g[6]==e[6]:
            for q in l:
                if q not in m:
                    g[6]=q
        if g[6]==f[6]:
            for q in l:
                if q not in m:
                    g[6]=q
        if g[6]==h[6]:
            for q in l:
                if q not in m:
                    g[6]=q
        if g[6]==i[6]:
            for q in l:
                if q not in m:
                    g[6]=q
        p=p+1
    if g[7]==a[7] or g[7]==b[7] or g[7]==c[7] or g[7]==d[7] or g[7]==e[7] or g[7]==f[7] or g[7]==h[7] or g[7]==i[7]:
        m=[g[7],a[7],b[7],c[7],d[7],e[7],f[7],h[7],i[7]]
        if g[7]==a[7]:
            for q in l:
                if q not in m:
                    g[7]=q
        if g[7]==b[7]:
            for q in l:
                if q not in m:
                    g[7]=q
        if g[7]==c[7]:
            for q in l:
                if q not in m:
                    g[7]=q
        if g[7]==d[7]:
            for q in l:
                if q not in m:
                    g[7]=q
        if g[7]==e[7]:
            for q in l:
                if q not in m:
                    g[7]=q
        if g[7]==f[7]:
            for q in l:
                if q not in m:
                    g[7]=q
        if g[7]==h[7]:
            for q in l:
                if q not in m:
                    g[7]=q
        if g[7]==i[7]:
            for q in l:
                if q not in m:
                    g[7]=q
        p=p+1
    if g[8]==a[8] or g[8]==b[8] or g[8]==c[8] or g[8]==d[8] or g[8]==e[8] or g[8]==f[8] or g[8]==h[8] or g[8]==i[8]:
        m=[g[8],a[8],b[8],c[8],d[8],e[8],f[8],h[8],i[8]]
        if g[8]==a[8]:
            for q in l:
                if q not in m:
                    g[8]=q
        if g[8]==b[8]:
            for q in l:
                if q not in m:
                    g[8]=q
        if g[8]==c[8]:
            for q in l:
                if q not in m:
                    g[8]=q
        if g[8]==d[8]:
            for q in l:
                if q not in m:
                    g[8]=q
        if g[8]==e[8]:
            for q in l:
                if q not in m:
                    g[8]=q
        if g[8]==f[8]:
            for q in l:
                if q not in m:
                    g[8]=q
        if g[8]==h[8]:
            for q in l:
                if q not in m:
                    g[8]=q
        if g[8]==i[8]:
            for q in l:
                if q not in m:
                    g[8]=q
        p=p+1
    if h[0]==a[0] or h[0]==b[0] or h[0]==c[0] or h[0]==d[0] or h[0]==e[0] or h[0]==f[0] or h[0]==g[0] or h[0]==i[0]:
        m=[h[0],a[0],b[0],c[0],d[0],e[0],f[0],g[0],i[0]]
        if h[0]==a[0]:
            for q in l:
                if q not in m:
                    h[0]=q
        if h[0]==b[0]:
            for q in l:
                if q not in m:
                    h[0]=q
        if h[0]==c[0]:
            for q in l:
                if q not in m:
                    h[0]=q
        if h[0]==d[0]:
            for q in l:
                if q not in m:
                    h[0]=q
        if h[0]==e[0]:
            for q in l:
                if q not in m:
                    h[0]=q
        if h[0]==f[0]:
            for q in l:
                if q not in m:
                    h[0]=q
        if h[0]==g[0]:
            for q in l:
                if q not in m:
                    h[0]=q
        if h[0]==i[0]:
            for q in l:
                if q not in m:
                    h[0]=q
        p=p+1
    if h[1]==a[1] or h[1]==b[1] or h[1]==c[1] or h[1]==d[1] or h[1]==e[1] or h[1]==f[1] or h[1]==g[1] or h[1]==i[1]:
        m=[h[1],a[1],b[1],c[1],d[1],e[1],f[1],g[1],i[1]]
        if h[1]==a[1]:
            for q in l:
                if q not in m:
                    h[1]=q
        if h[1]==b[1]:
            for q in l:
                if q not in m:
                    h[1]=q
        if h[1]==c[1]:
            for q in l:
                if q not in m:
                    h[1]=q
        if h[1]==d[1]:
            for q in l:
                if q not in m:
                    h[1]=q
        if h[1]==e[1]:
            for q in l:
                if q not in m:
                    h[1]=q
        if h[1]==f[1]:
            for q in l:
                if q not in m:
                    h[1]=q
        if h[1]==g[1]:
            for q in l:
                if q not in m:
                    h[1]=q
        if h[1]==i[1]:
            for q in l:
                if q not in m:
                    h[1]=q
        p=p+1
    if h[2]==a[2] or h[2]==b[2] or h[2]==c[2] or h[2]==d[2] or h[2]==e[2] or h[2]==f[2] or h[2]==g[2] or h[2]==i[2]:
        m=[h[2],a[2],b[2],c[2],d[2],e[2],f[2],g[2],i[2]]
        if h[2]==a[2]:
            for q in l:
                if q not in m:
                    h[2]=q
        if h[2]==b[2]:
            for q in l:
                if q not in m:
                    h[2]=q
        if h[2]==c[2]:
            for q in l:
                if q not in m:
                    h[2]=q
        if h[2]==d[2]:
            for q in l:
                if q not in m:
                    h[2]=q
        if h[2]==e[2]:
            for q in l:
                if q not in m:
                    h[2]=q
        if h[2]==f[2]:
            for q in l:
                if q not in m:
                    h[2]=q
        if h[2]==g[2]:
            for q in l:
                if q not in m:
                    h[2]=q
        if h[2]==i[2]:
            for q in l:
                if q not in m:
                    h[2]=q
        p=p+1
    if h[3]==a[3] or h[3]==b[3] or h[3]==c[3] or h[3]==d[3] or h[3]==e[3] or h[3]==f[3] or h[3]==g[3] or h[3]==i[3]:
        m=[h[3],a[3],b[3],c[3],d[3],e[3],f[3],g[3],i[3]]
        if h[3]==a[3]:
            for q in l:
                if q not in m:
                    h[3]=q
        if h[3]==b[3]:
            for q in l:
                if q not in m:
                    h[3]=q
        if h[3]==c[3]:
            for q in l:
                if q not in m:
                    h[3]=q
        if h[3]==d[3]:
            for q in l:
                if q not in m:
                    h[3]=q
        if h[3]==e[3]:
            for q in l:
                if q not in m:
                    h[3]=q
        if h[3]==f[3]:
            for q in l:
                if q not in m:
                    h[3]=q
        if h[3]==g[3]:
            for q in l:
                if q not in m:
                    h[3]=q
        if h[3]==i[3]:
            for q in l:
                if q not in m:
                    h[3]=q
        p=p+1
    if h[4]==a[4] or h[4]==b[4] or h[4]==c[4] or h[4]==d[4] or h[4]==e[4] or h[4]==f[4] or h[4]==g[4] or h[4]==i[4]:
        m=[h[4],a[4],b[4],c[4],d[4],e[4],f[4],g[4],i[4]]
        if h[4]==a[4]:
            for q in l:
                if q not in m:
                    h[4]=q
        if h[4]==b[4]:
            for q in l:
                if q not in m:
                    h[4]=q
        if h[4]==c[4]:
            for q in l:
                if q not in m:
                    h[4]=q
        if h[4]==d[4]:
            for q in l:
                if q not in m:
                    h[4]=q
        if h[4]==e[4]:
            for q in l:
                if q not in m:
                    h[4]=q
        if h[4]==f[4]:
            for q in l:
                if q not in m:
                    h[4]=q
        if h[4]==g[4]:
            for q in l:
                if q not in m:
                    h[4]=q
        if h[4]==i[4]:
            for q in l:
                if q not in m:
                    h[4]=q
        p=p+1
    if h[5]==a[5] or h[5]==b[5] or h[5]==c[5] or h[5]==d[5] or h[5]==e[5] or h[5]==f[5] or h[5]==g[5] or h[5]==i[5]:
        m=[h[5],a[5],b[5],c[5],d[5],e[5],f[5],g[5],i[5]]
        if h[5]==a[5]:
            for q in l:
                if q not in m:
                    h[5]=q
        if h[5]==b[5]:
            for q in l:
                if q not in m:
                    h[5]=q
        if h[5]==c[5]:
            for q in l:
                if q not in m:
                    h[5]=q
        if h[5]==d[5]:
            for q in l:
                if q not in m:
                    h[5]=q
        if h[5]==e[5]:
            for q in l:
                if q not in m:
                    h[5]=q
        if h[5]==f[5]:
            for q in l:
                if q not in m:
                    h[5]=q
        if h[5]==g[5]:
            for q in l:
                if q not in m:
                    h[5]=q
        if h[5]==i[5]:
            for q in l:
                if q not in m:
                    h[5]=q
        p=p+1
    if h[6]==a[6] or h[6]==b[6] or h[6]==c[6] or h[6]==d[6] or h[6]==e[6] or h[6]==f[6] or h[6]==g[6] or h[6]==i[6]:
        m=[h[6],a[6],b[6],c[6],d[6],e[6],f[6],g[6],i[6]]
        if h[6]==a[6]:
            for q in l:
                if q not in m:
                    h[6]=q
        if h[6]==b[6]:
            for q in l:
                if q not in m:
                    h[6]=q
        if h[6]==c[6]:
            for q in l:
                if q not in m:
                    h[6]=q
        if h[6]==d[6]:
            for q in l:
                if q not in m:
                    h[6]=q
        if h[6]==e[6]:
            for q in l:
                if q not in m:
                    h[6]=q
        if h[6]==f[6]:
            for q in l:
                if q not in m:
                    h[6]=q
        if h[6]==g[6]:
            for q in l:
                if q not in m:
                    h[6]=q
        if h[6]==i[6]:
            for q in l:
                if q not in m:
                    h[6]=q
        p=p+1
    if h[7]==a[7] or h[7]==b[7] or h[7]==c[7] or h[7]==d[7] or h[7]==e[7] or h[7]==f[7] or h[7]==g[7] or h[7]==i[7]:
        m=[h[7],a[7],b[7],c[7],d[7],e[7],f[7],g[7],i[7]]
        if h[7]==a[7]:
            for q in l:
                if q not in m:
                    h[7]=q
        if h[7]==b[7]:
            for q in l:
                if q not in m:
                    h[7]=q
        if h[7]==c[7]:
            for q in l:
                if q not in m:
                    h[7]=q
        if h[7]==d[7]:
            for q in l:
                if q not in m:
                    h[7]=q
        if h[7]==e[7]:
            for q in l:
                if q not in m:
                    h[7]=q
        if h[7]==f[7]:
            for q in l:
                if q not in m:
                    h[7]=q
        if h[7]==g[7]:
            for q in l:
                if q not in m:
                    h[7]=q
        if h[7]==i[7]:
            for q in l:
                if q not in m:
                    h[7]=q
        p=p+1
    if h[8]==a[8] or h[8]==b[8] or h[8]==c[8] or h[8]==d[8] or h[8]==e[8] or h[8]==f[8] or h[8]==g[8] or h[8]==i[8]:
        m=[h[8],a[8],b[8],c[8],d[8],e[8],f[8],g[8],i[8]]
        if h[8]==a[8]:
            for q in l:
                if q not in m:
                    h[8]=q
        if h[8]==b[8]:
            for q in l:
                if q not in m:
                    h[8]=q
        if h[8]==c[8]:
            for q in l:
                if q not in m:
                    h[8]=q
        if h[8]==d[8]:
            for q in l:
                if q not in m:
                    h[8]=q
        if h[8]==e[8]:
            for q in l:
                if q not in m:
                    h[8]=q
        if h[8]==f[8]:
            for q in l:
                if q not in m:
                    h[8]=q
        if h[8]==g[8]:
            for q in l:
                if q not in m:
                    h[8]=q
        if h[8]==i[8]:
            for q in l:
                if q not in m:
                    h[8]=q
        p=p+1
    if i[0]==a[0] or i[0]==b[0] or i[0]==c[0] or i[0]==d[0] or i[0]==e[0] or i[0]==f[0] or i[0]==g[0] or i[0]==h[0]:
        m=[i[0],a[0],b[0],c[0],d[0],e[0],f[0],g[0],h[0]]
        if i[0]==a[0]:
            for q in l:
                if q not in m:
                    i[0]=q
        if i[0]==b[0]:
            for q in l:
                if q not in m:
                    i[0]=q
        if i[0]==c[0]:
            for q in l:
                if q not in m:
                    i[0]=q
        if i[0]==d[0]:
            for q in l:
                if q not in m:
                    i[0]=q
        if i[0]==e[0]:
            for q in l:
                if q not in m:
                    i[0]=q
        if i[0]==f[0]:
            for q in l:
                if q not in m:
                    i[0]=q
        if i[0]==g[0]:
            for q in l:
                if q not in m:
                    i[0]=q
        if i[0]==h[0]:
            for q in l:
                if q not in m:
                    i[0]=q
        p=p+1
    if i[1]==a[1] or i[1]==b[1] or i[1]==c[1] or i[1]==d[1] or i[1]==e[1] or i[1]==f[1] or i[1]==g[1] or i[1]==h[1]:
        m=[i[1],a[1],b[1],c[1],d[1],e[1],f[1],g[1],h[1]]
        if i[1]==a[1]:
            for q in l:
                if q not in m:
                    i[1]=q
        if i[1]==b[1]:
            for q in l:
                if q not in m:
                    i[1]=q
        if i[1]==c[1]:
            for q in l:
                if q not in m:
                    i[1]=q
        if i[1]==d[1]:
            for q in l:
                if q not in m:
                    i[1]=q
        if i[1]==e[1]:
            for q in l:
                if q not in m:
                    i[1]=q
        if i[1]==f[1]:
            for q in l:
                if q not in m:
                    i[1]=q
        if i[1]==g[1]:
            for q in l:
                if q not in m:
                    i[1]=q
        if i[1]==h[1]:
            for q in l:
                if q not in m:
                    i[1]=q
        p=p+1
    if i[2]==a[2] or i[2]==b[2] or i[2]==c[2] or i[2]==d[2] or i[2]==e[2] or i[2]==f[2] or i[2]==g[2] or i[2]==h[2]:
        m=[i[2],a[2],b[2],c[2],d[2],e[2],f[2],g[2],h[2]]
        if i[2]==a[2]:
            for q in l:
                if q not in m:
                    i[2]=q
        if i[2]==b[2]:
            for q in l:
                if q not in m:
                    i[2]=q
        if i[2]==c[2]:
            for q in l:
                if q not in m:
                    i[2]=q
        if i[2]==d[2]:
            for q in l:
                if q not in m:
                    i[2]=q
        if i[2]==e[2]:
            for q in l:
                if q not in m:
                    i[2]=q
        if i[2]==f[2]:
            for q in l:
                if q not in m:
                    i[2]=q
        if i[2]==g[2]:
            for q in l:
                if q not in m:
                    i[2]=q
        if i[2]==h[2]:
            for q in l:
                if q not in m:
                    i[2]=q
        p=p+1
    if i[3]==a[3] or i[3]==b[3] or i[3]==c[3] or i[3]==d[3] or i[3]==e[3] or i[3]==f[3] or i[3]==g[3] or i[3]==h[3]:
        m=[i[3],a[3],b[3],c[3],d[3],e[3],f[3],g[3],h[3]]
        if i[3]==a[3]:
            for q in l:
                if q not in m:
                    i[3]=q
        if i[3]==b[3]:
            for q in l:
                if q not in m:
                    i[3]=q
        if i[3]==c[3]:
            for q in l:
                if q not in m:
                    i[3]=q
        if i[3]==d[3]:
            for q in l:
                if q not in m:
                    i[3]=q
        if i[3]==e[3]:
            for q in l:
                if q not in m:
                    i[3]=q
        if i[3]==f[3]:
            for q in l:
                if q not in m:
                    i[3]=q
        if i[3]==g[3]:
            for q in l:
                if q not in m:
                    i[3]=q
        if i[3]==h[3]:
            for q in l:
                if q not in m:
                    i[3]=q
        p=p+1
    if i[4]==a[4] or i[4]==b[4] or i[4]==c[4] or i[4]==d[4] or i[4]==e[4] or i[4]==f[4] or i[4]==g[4] or i[4]==h[4]:
        m=[i[4],a[4],b[4],c[4],d[4],e[4],f[4],g[4],h[4]]
        if i[4]==a[4]:
            for q in l:
                if q not in m:
                    i[4]=q
        if i[4]==b[4]:
            for q in l:
                if q not in m:
                    i[4]=q
        if i[4]==c[4]:
            for q in l:
                if q not in m:
                    i[4]=q
        if i[4]==d[4]:
            for q in l:
                if q not in m:
                    i[4]=q
        if i[4]==e[4]:
            for q in l:
                if q not in m:
                    i[4]=q
        if i[4]==f[4]:
            for q in l:
                if q not in m:
                    i[4]=q
        if i[4]==g[4]:
            for q in l:
                if q not in m:
                    i[4]=q
        if i[4]==h[4]:
            for q in l:
                if q not in m:
                    i[4]=q
        p=p+1
    if i[5]==a[5] or i[5]==b[5] or i[5]==c[5] or i[5]==d[5] or i[5]==e[5] or i[5]==f[5] or i[5]==g[5] or i[5]==h[5]:
        m=[i[5],a[5],b[5],c[5],d[5],e[5],f[5],g[5],h[5]]
        if i[5]==a[5]:
            for q in l:
                if q not in m:
                    i[5]=q
        if i[5]==b[5]:
            for q in l:
                if q not in m:
                    i[5]=q
        if i[5]==c[5]:
            for q in l:
                if q not in m:
                    i[5]=q
        if i[5]==d[5]:
            for q in l:
                if q not in m:
                    i[5]=q
        if i[5]==e[5]:
            for q in l:
                if q not in m:
                    i[5]=q
        if i[5]==f[5]:
            for q in l:
                if q not in m:
                    i[5]=q
        if i[5]==g[5]:
            for q in l:
                if q not in m:
                    i[5]=q
        if i[5]==h[5]:
            for q in l:
                if q not in m:
                    i[5]=q
        p=p+1
    if i[6]==a[6] or i[6]==b[6] or i[6]==c[6] or i[6]==d[6] or i[6]==e[6] or i[6]==f[6] or i[6]==g[6] or i[6]==h[6]:
        m=[i[6],a[6],b[6],c[6],d[6],e[6],f[6],g[6],h[6]]
        if i[6]==a[6]:
            for q in l:
                if q not in m:
                    i[6]=q
        if i[6]==b[6]:
            for q in l:
                if q not in m:
                    i[6]=q
        if i[6]==c[6]:
            for q in l:
                if q not in m:
                    i[6]=q
        if i[6]==d[6]:
            for q in l:
                if q not in m:
                    i[6]=q
        if i[6]==e[6]:
            for q in l:
                if q not in m:
                    i[6]=q
        if i[6]==f[6]:
            for q in l:
                if q not in m:
                    i[6]=q
        if i[6]==g[6]:
            for q in l:
                if q not in m:
                    i[6]=q
        if i[6]==h[6]:
            for q in l:
                if q not in m:
                    i[6]=q
        p=p+1
    if i[7]==a[7] or i[7]==b[7] or i[7]==c[7] or i[7]==d[7] or i[7]==e[7] or i[7]==f[7] or i[7]==g[7] or i[7]==h[7]:
        m=[i[7],a[7],b[7],c[7],d[7],e[7],f[7],g[7],h[7]]
        if i[7]==a[7]:
            for q in l:
                if q not in m:
                    i[7]=q
        if i[7]==b[7]:
            for q in l:
                if q not in m:
                    i[7]=q
        if i[7]==c[7]:
            for q in l:
                if q not in m:
                    i[7]=q
        if i[7]==d[7]:
            for q in l:
                if q not in m:
                    i[7]=q
        if i[7]==e[7]:
            for q in l:
                if q not in m:
                    i[7]=q
        if i[7]==f[7]:
            for q in l:
                if q not in m:
                    i[7]=q
        if i[7]==g[7]:
            for q in l:
                if q not in m:
                    i[7]=q
        if i[7]==h[7]:
            for q in l:
                if q not in m:
                    i[7]=q
        p=p+1
    if i[8]==a[8] or i[8]==b[8] or i[8]==c[8] or i[8]==d[8] or i[8]==e[8] or i[8]==f[8] or i[8]==g[8] or i[8]==h[8]:
        m=[i[8],a[8],b[8],c[8],d[8],e[8],f[8],g[8],h[8]]
        if i[8]==a[8]:
            for q in l:
                if q not in m:
                    i[8]=q
        if i[8]==b[8]:
            for q in l:
                if q not in m:
                    i[8]=q
        if i[8]==c[8]:
            for q in l:
                if q not in m:
                    i[8]=q
        if i[8]==d[8]:
            for q in l:
                if q not in m:
                    i[8]=q
        if i[8]==e[8]:
            for q in l:
                if q not in m:
                    i[8]=q
        if i[8]==f[8]:
            for q in l:
                if q not in m:
                    i[8]=q
        if i[8]==g[8]:
            for q in l:
                if q not in m:
                    i[8]=q
        if i[8]==h[8]:
            for q in l:
                if q not in m:
                    i[8]=q
        p=p+1
    print("it ran again")
    board()
    if p==0:
        break

board()