s=0
x=float(input("enter the angle in radian"))
n=int(input("enter the number of terms to be added"))
f=1
y=(1/x)
c=0
for i in range(1,2*n,2):
    c=c+1
    y=y*x*x
    if i%2==0:
        s=s-(y/f)
    else:
        s=s+(y/f)
    f=f*(i+1)*(i+2)
print("value=",s)