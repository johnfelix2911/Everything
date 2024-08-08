import pickle
import os
def create():
   teacher=[]
   f=open('teacher.dat','ab')
   clshan=[]
   ans='y'
   while ans=='y':
      tno=int(input("Enter teacher number:"))
      t=str(tno)
      name=input("Enter name of teacher:")
      sub=input("Enter subject taught:")
      dept=sub
      deptno=int(input("Enter Department number:"))
      doj=input("Enter date of join (DD/MM/YYYY):")
      se=input("Enter sex (Male/Female):")
      ag=int(input("Enter age of teacher:"))
      add=input("Enter address:")
      phno=input("Enter Phone number:")
      clstchof=input("Class teacher of (If not a Class Teacher enter 'NULL')(eg:XII-C):")
      ncls=int(input("Enter number of classes handled by teacher:"))
      print("In the format: XII-C")
      for i in range(ncls):
         s=input("Enter Class:")
         clshan.append(s)
      salary=int(input("Enter salary of the teacher:"))
      if salary>=30000:
          u='A'
      elif salary>=20000 and salary<30000:
         u='B'
      else:
         u='C'
      salarygrade=u
      
      teacher.append([t,name,sub,dept,doj,add,phno,clstchof,clshan,salary,salarygrade,se,ag,deptno])
      ans=input("Do you want to add more records?(Y/N)").lower()
   pickle.dump(teacher,f)
   f.close()
   print("Tearcher details successfully recorded.")
def search():
   tch=[]
   f=open("teacher.dat","rb")
   while True:
      try:
         tch=pickle.load(f)
      except EOFError:
         break
   while 1==1:
      print("Serach by:")
      print("1.Teacher number")
      print("2.Name of teacher")
      print("3.Department name")
      
      print("4.Class teacher")
      print("5.Department number")
      print("6.Exit from search menu")
      u=int(input("Enter your choice:"))
      if u==1:
         tnum=int(input("Enter teacher number to be searched:"))
         for i in tch:
            n=int(i[0])
            if(n==tnum):
               print("%10s"%"Tno.","%10s"%"Name","%10s"%"Subject","%10s"%"Department","%10s"%"Department no.","%10s"%"Date of join","%10s"%"Address","%10s"%"Age","%10s"%"Sex","%10s"%"Phone number","%10s"%"Class teacher","%10s"%"Classes handled","%10s"%"Salary","%10s"%"Salarygrade")
               print("%10s"%i[0],"%10s"%i[1],"10s"%i[2],"%10s"%i[3],"%10s"%i[13],"%10s"%i[4],"%10s"%i[5],"%10s"%i[12],"%10s"%i[11],"%10s"%i[6],"%10s"%i[7],"%10s"%i[8],"%10s"%i[9],"%10s"%i[10])
            else:
               print("Teacher number not found.")
      elif u==2:
         na=input("enter name of teacher to be serached:").upper()
         for i in tch:
            nm=str(i[1])
            if(nm.upper()==na):
                print("%10s"%"Tno.","%20s"%"Name","%20s"%"Subject","%20s"%"Department","%20s"%"Department no.","%20s"%"Date of join","%20s"%"Address","%20s"%"Age","%20s"%"Sex","%20s"%"Phone number","%20s"%"Class teacher","%20s"%"Classes handled","%20s"%"Salary","%20s"%"Salarygrade")
                print("%10s"%i[0],"%20s"%i[1],"%20s"%i[2],"%20s"%i[3],"%20s"%i[13],"%20s"%i[4],"%20s"%i[5],"%20s"%i[12],"%20s"%i[11],"%20s"%i[6],"%20s"%i[7],"%20s"%i[8],"%20s"%i[9],"%20s"%i[10])
            else:
               print("not found")
      elif u==3:
         print("**Departments available are same as subjects taught**")
         de=input("Enter Department name to be serached:").upper()
         for i in tch:
            if(i[3].upper()==de):
               print("%10s"%"Tno.","%20s"%"Name","%20s"%"Subject","%20s"%"Department","%20s"%"Department no.","%20s"%"Date of join","%20s"%"Address","%20s"%"Age","%20s"%"Sex","%20s"%"Phone number","%20s"%"Class teacher","%20s"%"Classes handled","%20s"%"Salary","%20s"%"Salarygrade")
               print("%10s"%i[0],"%20s"%i[1],"%20s"%i[2],"%20s"%i[3],"%20s"%i[13],"%20s"%i[4],"%20s"%i[5],"%20s"%i[12],"%20s"%i[11],"%20s"%i[6],"%20s"%i[7],"%20s"%i[8],"%20s"%i[9],"%20s"%i[10])
            else:
               print("Department not found")
      elif u==4:
         cl=input("Enter Class to be searched(eg: XII-C):").upper()
         for i in tch:
            if(i[7].upper()==cl):
               print("%10s"%"Tno.","%20s"%"Name","%20s"%"Subject","%20s"%"Department","%20s"%"Department no.","%20s"%"Date of join","%20s"%"Address","%20s"%"Age","%20s"%"Sex","%20s"%"Phone number","%20s"%"Class teacher","%20s"%"Classes handled","%20s"%"Salary","%20s"%"Salarygrade")
               print("%10s"%i[0],"%20s"%i[1],"%20s"%i[2],"%20s"%i[3],"%20s"%i[13],"%20s"%i[4],"%20s"%i[5],"%20s"%i[12],"%20s"%i[11],"%20s"%i[6],"%20s"%i[7],"%20s"%i[8],"%20s"%i[9],"%20s"%i[10])
            else:
               print("Class not found")
      elif u==5:
         dep=str(input("Enter Department No. :"))
         for i in tch:
                     s=str(i[13])
                     if s==dep:
                         print("%10s"%"Tno.","%20s"%"Name","%20s"%"Subject","%20s"%"Department","%20s"%"Department no.","%20s"%"Date of join","%20s"%"Address","%20s"%"Age","%20s"%"Sex","%20s"%"Phone number","%20s"%"Class teacher","%20s"%"Classes handled","%20s"%"Salary","%20s"%"Salarygrade")
                         print("%10s"%i[0],"%20s"%i[1],"%20s"%i[2],"%20s"%i[3],"%20s"%i[13],"%20s"%i[4],"%20s"%i[5],"%20s"%i[12],"%20s"%i[11],"%20s"%i[6],"%20s"%i[7],"%20s"%i[8],"%20s"%i[9],"%20s"%i[10])
                     else:
                        print("Invalid Department number")
      elif u==6:
                            break
                           
      else:
                            print('Sorry! Your choice is invalid')
def update():
   try:
      f=open("teacher.dat","rb")
   except FileNotFoundError:
       print('No record found to update.')
       return
   found=False
   fi=open("newfile.dat","wb")
   
   em=str(input("Enter teacher number of teacher whose records to be updated:"))
   while True:
      try:
         i=pickle.load(f)
         print("hello")
         print(i[0])
         for x in range(len(i)):
            if i[x][0]==em:
               print("%10s"%"Tno.","%20s"%"Name","%20s"%"Subject","%20s"%"Department","%20s"%"Department no.","%20s"%"Date of join","%20s"%"Address","%20s"%"Age","%20s"%"Sex","%20s"%"Phone number","%20s"%"Class teacher","%20s"%"Classes handled","%20s"%"Salary","%20s"%"Salarygrade")
               print("%10s"%i[x][0],"%20s"%i[x][1],"%20s"%i[x][2],"%20s"%i[x][3],"%20s"%i[x][13],"%20s"%i[x][4],"%20s"%i[x][5],"%20s"%i[x][12],"%20s"%i[x][11],"%20s"%i[x][6],"%20s"%i[x][7],"%20s"%i[x][8],"%20s"%i[x][9],"%20s"%i[x][10])
               print("Updation of subject taught by teacher")
               print("**NOTE**: Updating this category  will lead to the updation of department and department number as well ")
               ans=input("Would you like to update the subject taught(y/n)?")
               if ans=='Y':
                  i[x][2]=input("Enter new subject:")
                  i[x][3]=input("Enter new department")
                  i[x][13]=input("Enter new department number:")
               ans=input("Do you want to update date of join(y/n):").upper()
               if ans=='Y':
                  i[x][4]=input("Enter new date:")
               ans=input("Do you want to update address of teacher(y/n):").upper()
               if ans=='Y':
                  i[x][5]=input("Enter new adress:")
               ans=input("Do you want to update phone number of teacher(y/n):").upper()
               if ans=='Y':
                  i[x][6]=input("Enter new phone number:")
               pickle.dump(i,fi)
               found=True
               break
            else:
               pickle.dump(i,fi)
      except EOFError:
         break
      
   if found == False:
      print('Record not Found')
   else:
      print("Records updated successfully!!!")
   fi.close()
   f.close()
   os.remove("teacher.dat")
   os.rename("newfile.dat","teacher.dat")
def delete():
   tch=[]
   f=open("teacher.dat","rb")
   while True:
      try:
         tch=pickle.load(f)
      except EOFError:
         break
   for i in tch:
      print("%10s"%"Tno.","%20s"%"Name","%20s"%"Subject","%20s"%"Department","%20s"%"Department no.","%20s"%"Date of join","%20s"%"Address","%20s"%"Age","%20s"%"Sex","%20s"%"Phone number","%20s"%"Class teacher","%20s"%"Classes handled","%20s"%"Salary","%20s"%"Salarygrade")
      print("%10s"%i[0],"%20s"%i[1],"%20s"%i[2],"%20s"%i[3],"%20s"%i[13],"%20s"%i[4],"%20s"%i[5],"%20s"%i[12],"%20s"%i[11],"%20s"%i[6],"%20s"%i[7],"%20s"%i[8],"%20s"%i[9],"%20s"%i[10])
            
      
   f.close()
   f=open("newfile.dat","wb")
   nr=[]
   em=int(input("Enter teacher number whoose record is to be deleted:"))
   
   for i in range(len(tch)):
      n=int(tch[i][0])
      if n==em:
        print("%10s"%"Tno.","%20s"%"Name","%20s"%"Subject","%20s"%"Department","%20s"%"Department no.","%20s"%"Date of join","%20s"%"Address","%20s"%"Age","%20s"%"Sex","%20s"%"Phone number","%20s"%"Class teacher","%20s"%"Classes handled","%20s"%"Salary","%20s"%"Salary grade")
        print("***********************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************")
        print("%10s"%tch[i][0],"%20s"%tch[i][1],"%20s"%tch[i][2],"%20s"%tch[i][3],"%20s"%tch[i][13],"%20s"%tch[i][4],"%20s"%tch[i][5],"%20s"%tch[i][12],"%20s"%tch[i][11],"%20s"%tch[i][6],"%20s"%tch[i][7],"%20s"%tch[i][8],"%20s"%tch[i][9],"%20s"%tch[i][10])
         
        
        break
      if  n==em and ans=='Y':
         continue
      else:
         nr.append(tch[i])
   print("Record deleted")
   pickle.dump(nr,f)
   f.close()
   os.remove("teacher.dat")
   os.rename("newfile.dat","teacher.dat")
