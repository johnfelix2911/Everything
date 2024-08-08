import mysql.connector as mys
mycon=mys.connect(host='localhost',user='root',passwd='teenafelix@123')
mycursor=mycon.cursor()
q="create database if not exists school;"
mycursor.execute(q)
q="use school"
mycursor.execute(q)
q="create table if not exists student(adno int(5),name varchar(40),phone varchar(12),father varchar(30),mother varchar(30),address varchar(50),class int(2),rollno int(3),gender char(1),house varchar(30),cocurricular varchar(40),eng float(5,2),math float(5,2),phy float(5,2),chem float(5,2),comp float(5,2));"
mycursor.execute(q)
def insert():
        q="select adno from student;"
        mycursor.execute(q)
        d=mycursor.fetchall()
        if d==[]:
            adno=1000
        else:
            adno=d[len(d)-1][0]+1
        print("The student's admission number is",adno)
        name=input("Enter the student's name:").title()
        phno=input("Enter the student's contact number:")
        fat=input("Enter the name of the student's father:").title()
        mot=input("Enter the name of the student's mother:").title()
        add=input("Enter the student's official address:")
        while True:
            clss=int(input("Enter the student's class(as an integer value):"))
            if clss in [9,10,11,12]:
                break
            else:
                print("The class you have entered does not exist in this institution")
                x=input("Enter any value to try again")
        roll=rollno(name,clss)
        print("The student's roll number is ",roll)
        while True:
            g=input("Enter the student's gender(M/F):")
            gen=g.upper()
            if gen not in ['M','F']:
                print("Invalid input")
                x=input("Enter any value to try again")
            else:
                break
        if adno%4==0:
                house="Olympians"
        elif adno%4==1:
                house="Knights"
        elif adno%4==2:
                house="Spartans"
        else:
                house="Titans"
        print("The house assigned to the student is ",house)
        cocurr=input("Enter the cocurricular activity the student has opted:").title()
        eng=float(input("Enter the student's percentage score in the subject English:"))
        math=float(input("Enter the student's percentage score in the subject Mathematics:"))
        phy=float(input("Enter the student's percentage score in the subject Physics:"))
        chem=float(input("Enter the student's percentage score in the subject Chemistry:"))
        comp=float(input("Enter the student's percentage score in the subject Computer:"))
        print()
        q="insert into student values({},'{}','{}','{}','{}','{}',{},{},'{}','{}','{}',{},{},{},{},{});".format(adno,name,phno,fat,mot,add,clss,roll,gen,house,cocurr,eng,math,phy,chem,comp)
        mycursor.execute(q)
        mycon.commit()
        print("The details of the student named ",name," has been successfully added to the school's database")
        print()
        print()
def search():
    while True:
        try:
            print("1)Search by admission number")
            print("2)Search by name")
            print("3)Search by class and roll number")
            print("4)Display the students belonging to a particular class")
            print("5)Display the students belonging to a particular house")
            print("6)Display the students who have opted a particular cocurricular acivity")
            ch=int(input("Enter your choice:"))
            if ch==1:
                ad=int(input("Enter the admission number:"))
                q="select * from student"
                mycursor.execute(q)
                d=mycursor.fetchall()
                for i in range(5000000):
                    i=i+1
                print("Searching",end='')
                for i in range(5000000):
                    i=i+1
                print(".",end='')
                for i in range(5000000):
                    i=i+1
                print(".",end='')
                for i in range(5000000):
                    i=i+1
                print(".",end='')
                for i in range(5000000):
                    i=i+1
                print(".",end='')
                for i in range(5000000):
                    i=i+1
                print(".")
                for i in d:
                    if i[0]==ad:
                        print("Name:",i[1])
                        print("Contact Number:",i[2])
                        print("Father:",i[3])
                        print("Mother:",i[4])
                        print("Address:",i[5])
                        print("Class:",i[6])
                        print("Roll number:",i[7])
                        ch=input("Do you wish to view the marks of the student?(Y/N)")
                        if ch.upper()=='Y':
                            print("English",i[11])
                            print("Mathematics:",i[12])
                            print("Physics:",i[13])
                            print("Chemistry:",i[14])
                            print("Computer:",i[15])
                        break
                else:
                    print("No such student exists")
            if ch==2:
                n=input("Enter the student's name").title()
                q="select * from student;"
                mycursor.execute(q)
                d=mycursor.fetchall()
                for i in range(5000000):
                    i=i+1
                print("Searching",end='')
                for i in range(5000000):
                    i=i+1
                print(".",end='')
                for i in range(5000000):
                    i=i+1
                print(".",end='')
                for i in range(5000000):
                    i=i+1
                print(".",end='')
                for i in range(5000000):
                    i=i+1
                print(".",end='')
                for i in range(5000000):
                    i=i+1
                print(".")
                for i in d:
                    if i[1]==n:
                        print("Admission number:",i[0])
                        print("Name:",i[1])
                        print("Contact Number:",i[2])
                        print("Father:",i[3])
                        print("Mother:",i[4])
                        print("Address:",i[5])
                        print("Class:",i[6])
                        print("Roll number:",i[7])
                        ch=input("Do you wish to view the marks of the student?(Y/N)")
                        if ch.upper()=='Y':
                            print("English",i[11])
                            print("Mathematics:",i[12])
                            print("Physics:",i[13])
                            print("Chemistry:",i[14])
                            print("Computer:",i[15])
                        print()
                        print()
                        break
                else:
                    print("No such student exists")
            if ch==3:
                while True:
                    cl=int(input("Enter the class to which the student belongs to:"))
                    if cl in [9,10,11,12]:
                        break
                    else:
                        print("The class you have entered does not exist in this institution")
                r=int(input("Enter the student's roll number"))
                q="select * from student;"
                mycursor.execute(q)
                d=mycursor.fetchall()
                for i in range(5000000):
                    i=i+1
                print("Searching",end='')
                for i in range(5000000):
                    i=i+1
                print(".",end='')
                for i in range(5000000):
                    i=i+1
                print(".",end='')
                for i in range(5000000):
                    i=i+1
                print(".",end='')
                for i in range(5000000):
                    i=i+1
                print(".",end='')
                for i in range(5000000):
                    i=i+1
                print(".")
                for i in d:
                    if i[6]==cl:
                        if i[7]==r:
                            print("Admission number:",i[0])
                            print("Name:",i[1])
                            print("Contact Number:",i[2])
                            print("Father:",i[3])
                            print("Mother:",i[4])
                            print("Address:",i[5])
                            print("Class:",i[6])
                            print("Roll number:",i[7])
                            ch=input("Do you wish to view the marks of the student?(Y/N)")
                            if ch.upper()=='Y':
                                print("English",i[11])
                                print("Mathematics:",i[12])
                                print("Physics:",i[13])
                                print("Chemistry:",i[14])
                                print("Computer:",i[15])
                            break
                else:
                    print("No such student exists")
            if ch==4:
                cl=int(input("Enter the class whose student list is to be generated:"))
                q="select * from student;"
                mycursor.execute(q)
                d=mycursor.fetchall()
                l=[]
                for i in range(10000000):
                    i=i+1
                print("Generating",end='')
                for i in range(5000000):
                    i=i+1
                print(".",end='')
                for i in range(5000000):
                    i=i+1
                print(".",end='')
                for i in range(5000000):
                    i=i+1
                print(".",end='')
                for i in range(5000000):
                    i=i+1
                print(".",end='')
                for i in range(5000000):
                    i=i+1
                print(".")
                for i in d:
                    if i[6]==cl:
                        l.append([i[1],i[7]])
                for j in range(len(l)):
                    for k in range(len(l)-j-1):
                        if l[k][1]>l[k+1][1]:
                            l[k],l[k+1]=l[k+1],l[k]
                if l==[]:
                        print("There is no such class in this institution")
                else:
                        print("STUDENTS OF CLASS ",cl," ARE AS FOLLOWS:")
                        for i in l:
                                print(i[1],")",i[0])
                print()
                print()
            if ch==5:
                h=input("Enter the house whose student list is to be generated:").title()
                q="select * from student;"
                mycursor.execute(q)
                d=mycursor.fetchall()
                l=[]
                for i in range(10000000):
                    i=i+1
                print("Please wait",end='')
                for i in range(10000000):
                    i=i+1
                print(".",end='')
                for i in range(10000000):
                    i=i+1
                print(".",end='')
                for i in range(10000000):
                    i=i+1
                print(".",end='')
                for i in range(10000000):
                    i=i+1
                print(".",end='')
                for i in range(10000000):
                    i=i+1
                print(".")
                for i in d:
                    if i[9]==h:
                        l.append(i[1])
                if l==[]:
                        print("There is no such house in this institution")
                else:
                        print("THE STUDENTS BELONGING TO HOUSE ",h.upper()," ARE AS FOLLOWS:")
                        for i in l:
                                print(i)
                print()
                print()
            if ch==6:
                c=input("Enter the cocurricular activity whose student list is to be generated:").title()
                q="select * from student;"
                mycursor.execute(q)
                d=mycursor.fetchall()
                l=[]
                for i in range(5000000):
                    i=i+1
                print("Please wait",end='')
                for i in range(5000000):
                    i=i+1
                print(".",end='')
                for i in range(5000000):
                    i=i+1
                print(".",end='')
                for i in range(5000000):
                    i=i+1
                print(".",end='')
                for i in range(5000000):
                    i=i+1
                print(".",end='')
                for i in range(5000000):
                    i=i+1
                print(".")
                for i in d:
                        if i[10]==c:
                                l.append(i[1])
                print("THE STUDENTS WHO HAVE OPTED THAT ACTIVITY ARE AS FOLLOWS:")
                if l==[]:
                        print("No student has opted this activity")
                else:
                        for i in l:
                                print(i)
                print()
                print()
            print("Enter 1 to continue searching")
            print("Enter 2 to return to the main menu")
            cho=int(input("Enter your choice:"))
            if cho==2:
                break
        except:
            print("Invalid input")
            x=input("Enter any value to continue")
def updation():
            print("SELECT THE MODE BY WHICH YOU WANT TO UPDATE THE STUDENT DATABASE:")
            print("1)by admission number")
            print("2)by name")
            ch=int(input("Enter your choice:"))
            if ch==1:
                a=int(input("Enter the admission number of the student whose record you want to update:"))
                q="select * from student;"
                mycursor.execute(q)
                d=mycursor.fetchall()
                q="delete from student where adno={};".format(a)
                mycursor.execute(q)
                for i in d:
                    if i[0]==a:
                        c=input("Do you want to update the student's name?(Y/N)")
                        if c.upper()=='Y':
                            n=input("Enter the new name:").title()
                            r=rollno(n,i[6])
                            print(r)
                        else:
                            n=i[1]
                            r=i[7]
                        c=input("Do you want to update the student's contact number?(Y/N)")
                        if c.upper()=='Y':
                            p=input("Enter the new contact number:")
                        else:
                            p=i[2]
                        c=input("Do you want to update the student's address?(Y/N)")
                        if c.upper()=='Y':
                            ad=input("Enter the new address:")
                        else:
                            ad=i[5]
                        c=input("Do you want to change the name of the student's father?(Y/N)")
                        if c.upper()=='Y':
                                fat=input("Enter the new name:").title()
                        else:
                                fat=i[3]
                        c=input("Do you want to change the name of the student's mother?(Y/N)")
                        if c.upper()=='Y':
                                mot=input("Enter the new name:").title()
                        else:
                                mot=i[4]
                        c=input("Do you want to change the student's coccurricular activity?(Y/N)")
                        if c.upper()=='Y':
                                cocurr=input("Enter the new activity the student has opted:")
                        else:
                                cocurr=i[10]
                        c=input("Do you want to update the marks of the student?(Y/N)")
                        if c.upper()=='Y':
                                c=input("Do you want to edit English marks?(Y/N)")
                                if c.upper()=='Y':
                                        m1=float(input("Enter the new mark:"))
                                else:
                                        m1=i[11]
                                c=input("Do you want to edit Mathematics marks?(Y/N)")
                                if c.upper()=='Y':
                                        m2=float(input("Enter the new mark:"))
                                else:
                                        m2=i[12]
                                c=input("Do you want to edit Physics marks?(Y/N)")
                                if c.upper()=='Y':
                                        m3=float(input("Enter the new mark:"))
                                else:
                                        m3=i[13]
                                c=input("Do you want to edit Chemistry marks?(Y/N)")
                                if c.upper()=='Y':
                                        m4=float(input("Enter the new mark:"))
                                else:
                                        m4=i[14]
                                c=input("Do you want to edit Computer marks?(Y/N)")
                                if c.upper()=='Y':
                                        m5=float(input("Enter the new mark:"))
                                else:
                                        m5=i[15]
                        else:
                                m1=i[11]
                                m2=i[12]
                                m3=i[13]
                                m4=i[14]
                                m5=i[15]
                        adno=a
                        name=n
                        phno=p
                        add=ad
                        clss=i[6]
                        roll=r
                        gen=i[8]
                        house=i[9]
                        eng=m1
                        math=m2
                        phy=m3
                        chem=m4
                        comp=m5
                        q="insert into student values({},'{}','{}','{}','{}','{}',{},{},'{}','{}','{}',{},{},{},{},{});".format(adno,name,phno,fat,mot,add,clss,roll,gen,house,cocurr,eng,math,phy,chem,comp)
                        mycursor.execute(q)
                        mycon.commit()
                        print("The record has been successfully updated")
                        break
                else:
                    print("No such student exists")
            if ch==2:
                name=input("Enter the name of the student").title()
                q="select * from student;"
                mycursor.execute(q)
                d=mycursor.fetchall()
                q="delete from student where name='{}':".format(name)
                mycursor.execute(q)
                for i in d:
                    if i[1]==name:
                        c=input("Do you want to update the student's contact number?(Y/N)")
                        if c.upper()=='Y':
                            p=input("Enter the new contact number:")
                        else:
                            p=i[2]
                        c=input("Do you want to update the student's address?(Y/N)")
                        if ch.upper()=='Y':
                            ad=input("Enter the new address:")
                        else:
                            ad=i[5]
                        c=input("Do you want to change the name of the student's father?(Y/N)")
                        if c.upper()=='Y':
                                fat=input("Enter the new name:").title()
                        else:
                                fat=i[3]
                        c=input("Do you want to change the name of the student's mother?(Y/N)")
                        if c.upper()=='Y':
                                mot=input("Enter the new name:").title()
                        else:
                                mot=i[4]
                        c=input("Do you want to change the student's coccurricular activity?(Y/N)")
                        if c.upper()=='Y':
                                cocurr=input("Enter the new activity the student has opted:")
                        else:
                                cocurr=i[10]
                        c=input("Do you want to update the marks of the student?(Y/N)")
                        if c.upper()=='Y':
                                c=input("Do you want to edit English marks?(Y/N)")
                                if c.upper()=='Y':
                                        m1=float(input("Enter the new mark:"))
                                else:
                                        m1=i[11]
                                c=input("Do you want to edit Mathematics marks?(Y/N)")
                                if c.upper()=='Y':
                                        m1=float(input("Enter the new mark:"))
                                else:
                                        m1=i[12]
                                c=input("Do you want to edit Physics marks?(Y/N)")
                                if c.upper()=='Y':
                                        m1=float(input("Enter the new mark:"))
                                else:
                                        m1=i[13]
                                c=input("Do you want to edit Chemistry marks?(Y/N)")
                                if c.upper()=='Y':
                                        m1=float(input("Enter the new mark:"))
                                else:
                                        m1=i[14]
                                c=input("Do you want to edit Computer marks?(Y/N)")
                                if c.upper()=='Y':
                                        m1=float(input("Enter the new mark:"))
                                else:
                                        m1=i[15]
                        else:
                                m1=i[11]
                                m2=i[12]
                                m3=i[13]
                                m4=i[14]
                                m5=i[15]
                        adno=i[0]
                        phno=p
                        add=ad
                        clss=i[6]
                        gen=i[8]
                        house=i[9]
                        q="insert into student values({},'{}','{}','{}','{}','{}',{},{},'{}','{}','{}',{},{},{},{},{});".format(adno,name,phno,fat,mot,add,clss,roll,gen,house,cocurr,eng,math,phy,chem,comp)
                        mycursor.execute(q)
                        mycon.commit()
                        break
                else:
                    print("No such student exists")
            if ch not in [1,2]:
                    print("Invalid choice")
                    x=input("Enter any value to continue")
                    print()
                    print()
def totstrength():
    q="select * from student;"
    mycursor.execute(q)
    d=mycursor.fetchall()
    c=0
    for i in d:
        c=c+1
    print("The strength of the institution is ",c)
def classstrgth():
    while True:
        clss=int(input("Enter the class whose strength you want to know:"))
        if clss in [9,10,11,12]:
            break
        else:
            print("The class you have entered does not exist in this institution")
            x=input("Enter any value to try again")
    q="select * from student;"
    mycursor.execute(q)
    d=mycursor.fetchall()
    c=0
    for i in d:
        if i[6]==clss:
            c=c+1
    print("Total strength of class ",clss," is ",c)
def rank():
    clss=int(input("Enter the class whose ranklist you want:"))
    l1=[]
    q="select * from student;"
    mycursor.execute(q)
    d=mycursor.fetchall()
    l=[]
    for i in d:
        if i[6]==clss:
            l1.append(i)
    for i in l1:
        t=i[12]+i[13]+i[14]+i[15]+i[11]
        p=(t/5)
        l.append([i,p])
    n=len(l)
    for i in range(n):
        for j in range(n-i-1):
            if l[j][1]<l[j+1][1]:
                l[j],l[j+1]=l[j+1],l[j]
    print("Ranklist of class ",clss," is as follows:")
    m=1
    for i in l:
        print(m,")",i[0][1]," (Percenatge score=",i[1],")")
        m=m+1
def deletion():
    print("SELECT FROM THE FOLLOWING:")
    print("1)Delete by admission number")
    print("2)Delete by name")
    ch=int(input("Enter your choice:"))
    print()
    print()
    if ch==1:
        ad=int(input("Enter the admission number of the student you want to delete:"))
        q="select * from student where adno={};".format(ad)
        mycursor.execute(q)
        d=mycursor.fetchall()
        l=d[0]
        q="delete from student where adno={};".format(ad)
        mycursor.execute(q)
        mycon.commit()
        print("The record of the student whose admission number is ",ad," has been successfully deleted from the school's database")
        q="select * from student;"
        mycursor.execute(q)
        d=mycursor.fetchall()
        l=[]
        for i in d:
                l.append(i[1].lower())
        l.sort()
        m=[]
        c=1
        for i in l:
                m.append([l[c-1],c])
                c=c+1
        for i in d:
                q="delete from student where adno={};".format(i[0])
                mycursor.execute(q)
                adno=i[0]
                name=i[1]
                phno=i[2]
                fat=i[3]
                mot=i[4]
                add=i[5]
                clss=i[6]
                for j in m:
                        if j[0].title()==name:
                                roll=j[1]
                gen=i[8]
                house=i[9]
                cocurr=i[10]
                eng=i[11]
                math=i[12]
                phy=i[13]
                chem=i[14]
                comp=i[15]
                q="insert into student values({},'{}','{}','{}','{}','{}',{},{},'{}','{}','{}',{},{},{},{},{});".format(adno,name,phno,fat,mot,add,clss,roll,gen,house,cocurr,eng,math,phy,chem,comp)
                mycursor.execute(q)
                mycon.commit()
    if ch==2:
        n=input("Enter the name of the student whose record you want to delete:").title()
        q="select * from student where name='{}';".format(n)
        mycursor.execute(q)
        d=mycursor.fetchall()
        l=d[0]
        q="delete from student where name='{}';".format(n)
        mycursor.execute(q)
        mycon.commit()
        print("The record of the student whose admission number is ",ad," has been successfully deleted from the school's database")
        q="select * from student;"
        mycursor.execute(q)
        d=mycursor.fetchall()
        l=[]
        for i in d:
                l.append(i[1].lower())
        l.sort()
        m=[]
        c=1
        for i in l:
                m.append([l[c-1],c])
                c=c+1
        print(m)
        for i in d:
                adno=i[0]
                name=i[1]
                phno=i[2]
                fat=i[3]
                mot=i[4]
                add=i[5]
                clss=i[6]
                for j in m:
                        if j[0].title()==name:
                                roll=j[1]
                gen=i[8]
                house=i[9]
                cocurr=i[10]
                eng=i[11]
                math=i[12]
                phy=i[13]
                chem=i[14]
                comp=i[15]
                q="insert into student values({},'{}','{}','{}','{}','{}',{},{},'{}','{}','{}',{},{},{},{},{});".format(adno,name,phno,fat,mot,add,clss,roll,gen,house,cocurr,eng,math,phy,chem,comp)
                mycon.commit()
def rollno(name,clss):
        q="select * from student;"
        mycursor.execute(q)
        d=mycursor.fetchall()
        l=[]
        for i in d:
                if i[6]==clss:
                        l.append(i)
        n=len(l)
        s=name.split()
        for i in range(n):
                for j in range(n-i-1):
                        if l[j][7]>l[j+1][7]:
                                l[j],l[j+1]=l[j+1],l[j]
        if l==[]:
                roll=1
        elif len(l)==1:
                m=l[0][1].split()
                if s[0].lower()<m[0].lower():
                        roll=1
                        q="update student set rollno=rollno+1 where class={};".format(clss)
                        mycursor.execute(q)
                elif s[0].lower()==m[0].lower():
                        if s[1].lower()<m[1].lower():
                                roll=1
                                q="update student set rollno=rollno+1 where class={};".format(clss)
                                mycursor.execute(q)
                        else:
                                roll=2
                                q="update student set rollno=rollno+1 where class={} and rollno>1;".format(clss)
                                mycursor.execute(q)
                else:
                        roll=2
        else:
                for i in range(0,len(l)):
                        if i==0:
                                m=l[i][1].split()
                                if s[0].lower()<m[0].lower():
                                        roll=1
                                        q="update student set rollno=rollno+1 where class={};".format(clss)
                                        mycursor.execute(q)
                                        break
                                if s[0].lower()==m[0].lower():
                                        if s[1].lower()<m[1].lower():
                                                roll=1
                                                q="update student set rollno=rollno+1 where class={};".format(clss)
                                                mycursor.execute(q)
                                                break
                                        else:
                                                roll=2
                                                q="update student set rollno=rollno+1 where class={} and rollno>1;".format(clss)
                                                mycursor.execute(q)
                                                break
                        if i!=(len(l)-1):
                                m=l[i][1].split()
                                p=l[i+1][1].split()
                                if s[0].lower()>m[0].lower() and s[0].lower()<p[0].lower():
                                        roll=l[i][7]+1
                                        q="update student set rollno=rollno+1 where class={} and rollno>={};".format(clss,roll)
                                        mycursor.execute(q)
                                        break
                                if s[0].lower()==m[0].lower():
                                        if s[1].lower()<m[1].lower():
                                                roll=l[i][7]
                                                q="update student set rollno=rollno+1 where class={} and rollno>={};".format(clss,roll)
                                                mycursor.execute(q)
                                                break
                                        else:
                                                roll=l[i][7]+1
                                                q="update student set rollno=rollno+1 where class={} and rollno>={};".format(clss,roll)
                                                mycursor.execute(q)
                                                break
                        else:
                                m=l[i][1].split()
                                if s[0].lower()>m[0].lower():
                                        roll=l[i][7]+1
                                if s[0].lower()==m[0].lower():
                                        if s[1].lower()<m[1].lower():
                                                roll=l[i][7]
                                                q="update student set rollno=rollno+1 where class={} and rollno>={};".format(clss,roll)
                                                mycursor.execute(q)
                                        else:
                                                roll=l[i][7]+1
        return roll
