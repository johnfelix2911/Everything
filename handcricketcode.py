import random
print("WELCOME")
ch=int(input("enter 1 to continue"))
if ch==1:
    w=int(input("how many wickets do you want to play for?"))
    ch=input("odd(o) or even(e)?")
    z=1
    while z==1:
        x=int(input("enter your toss:"))
        if x>=0 and x<=6:
            z=10
        else:
            z=1
            print("sorry the value you have entered is not between 0 and 6")
    y=random.randint(0,6)
    if ch=='o':
        s=x+y
        if s%2==1:
            r=1
        else:
            r=0
    else:
        s=x+y
        if s%2==0:
            r=1
        else:
            r=0
    if r==1:
        print("you have won the toss")
    else:
        print("you have lost the toss")
    if r==1:
        print("enter 1 to bat first and 2 to bowl first")
        ch=int(input())
        if ch==1:
            wo=0
            sc1=0
            print("start batting")
            while wo<w:
                b=int(input("enter the number"))
                t=random.randint(0,6)
                if b==t:
                    wo=wo+1
                    print("WICKET")
                else:
                    sc1=sc1+b
            print("your batting is over")
            print("your score is "+str(sc1))
            print("time to bowl")
            wo=0
            sc2=0
            print("start bowling")
            while wo<w:
                b=random.randint(0,6)
                t=int(input("enter a number"))
                if b==t:
                    wo=wo+1
                    print("WICKET")
                else:
                    sc2=sc2+b
            print("your bowling is over too")
            print("computer's score is "+str(sc2))
            if sc1>sc2:
                print("you have WON")
            elif sc1==sc2:
                print("DRAW")
            else:
                print("LOSS")
        else:
            wo=0
            sc1=0
            print("start bowling")
            while wo<w:
                t=int(input("enter the number"))
                b=random.randint(0,6)
                if b==t:
                    wo=wo+1
                    print("WICKET")
                else:
                    sc1=sc1+b
            print("your bowling is over")
            print("computer's score is"+str(sc1))
            print("time to bat")
            wo=0
            sc2=0
            print("start batting")
            while wo<w:
                t=random.randint(0,6)
                b=int(input("enter a number"))
                if b==t:
                    wo=wo+1
                    print("WICKET")
                else:
                    sc2=sc2+b
            print("your batting is over too")
            print("your score is"+str(sc2))
            if sc2>sc1:
                print("you have WON")
            elif sc1==sc2:
                print("DRAW")
            else:
                print("LOSS")
    else:
        p=random.choice((1,2))
        sc1=0
        sc2=0
        if p==1:
            print("you have to bat first")
            print("start batting")
            wo=0
            while wo<w:
                b=int(input("enter a number"))
                t=random.randint(0,6)
                if b==t:
                    print("WICKET")
                    wo=wo+1
                else:
                    sc1=sc1+b
            print("you batting is over")
            print("you score is",sc1)
            wo=0
            while wo<w:
                print("start bowling")
                b=int(input("enter a number"))
                t=random.randint(0,6)
                if b==t:
                    print("WICKET")
                    wo=wo+1
                else:
                    sc2=sc2+t
            print("the computer's score is",sc2)
            if sc1>sc2:
                print("you have won")
            elif sc1==sc2:
                print("its a draw")
            else:
                print("you have lost")
        else:
            print("you have to bowl first")
            print("start bowling")
            wo=0
            while wo<w:
                b=int(input("enter a number"))
                t=random.randint(0,6)
                if b==t:
                    print("WICKET")
                    wo=wo+1
                else:
                    sc1=sc1+t
            print("now its your turn to bat")
            wo=0
            while wo<w:
                b=int(input("enter a number"))
                t=random.randint(0,6)
                if b==t:
                    print("WICKET")
                    wo=wo+1
                else:
                    sc2=sc2+b
            if sc1>sc2:
                print("you have lost")
            elif sc1==sc2:
                print("it is a draw")
            else:
                print("you have won")
            
