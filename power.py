while True:
    x=int(input("enter the number to be checked"))
    f=0
    if x==1:
        f=1
    while x>1:
        r=x%2
        if r==0:
            x=x/2
        else:
            f=1
            break
    if f==0:
        print("yes")
    else:
        print("no")
    ch=input("do you want to continue inputting values?(Y/N)")
    if ch.upper()!="Y":
        break
