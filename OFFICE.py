
import pickle
#office add
def add():
            emp=[]
            f1=open("employee2.dat","ab+")
            ans='y'
            while ans=='y':
                        eno=int(input("Enter the Staff NO: "))
                        name=input("Enter the name: ")
                        age=int(input("Enter the age:"))
                        gender=input("Sex: (M/F)")
                        dept=input("Enter the department: ")
                        salary=int(input("Enter the salary (In Rs): "))
                        emp.append([eno,name,age,gender,dept,salary])
                        pickle.dump(emp,f1)
                        ans=input("Add more record? ").lower()
            f1.close()

#salary updation
def updation():
            file=open("employee2.dat","rb+")
            eno=int(input("Enter the staff NO to be updated: "))
            file.seek(0)
            try:
                        while True:
                                    pos=file.tell()
                                    data=pickle.load(file)
                                    for row in data:
                                                if row[0]==eno:
                                                   row[1]=int(input("Enter the salary to be updated:"))
                                                   file.seek(pos)
                                                   pickle.dump(data,file)
                                                   print("The new salary is:",row[1])
                                                   break
            except Exception:
                        file.close()

#office deletion
def deletion():
            fin=open("employee2.dat","rb")
            data=pickle.load(fin)
            print("The records are:",data)
            fin.close()
            eno=int(input("Enter the Staff NO to be deleted: "))
            fout=open("employee2.dat","ab")
            emplst=[]
            for r1 in data:
                        if r1[0]==eno:
                                    continue
                        emplst.append[r1]
            pickle.dump(emplst,fout)
            fout.close()
            fin=open("employee2.dat","rb")
            data=pickle.load(fin)
            print("The record after the deletion",data)
            fin.close()

#office search
def search():
            emp=[]
            f2=open('employee2.dat','rb')
            eno=int(input("Enter the employee no to be searched"))
            found=False
            try:
                        while True:
                                    emp=pickle.load(f2)    #loading data in emplst
            except:
                        f2.close()
            print("%15s"%"Staff No","%15s"%"Staff Name","%15s"%"Age","%15s"%"Sex","%15s"%"Department","%15s"%"Salary")
            print("******************************************************************************************************")
            for e in emp:
                        #print(e)
                        if e[0]==eno:
                                    print("%15s"%e[0],"%16s"%e[1],"%17s"%e[2],"%17s"%e[3],"%17s"%e[4],"%16s"%e[5])
                                    found = True
                                    break
            if found ==False:
                        print("## Sorry employee not found!! ##")
            f2.close()

