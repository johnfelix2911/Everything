import os
import pickle
#Accepting data for List
def insertRec():
     print("Inserting Record".center(60))
     print(("-"*20).center(60))
     print("PLEASE FILL IN BLOCK LETTERS!\n".center(60))
     while True:
          try:
               stafId=int(input("Enter Staff Id "))     
               print("-"*18)               
          except ValueError:
               print("\nENTER A NUMERICAL VALUE!\n")
               continue
          name=input("Enter the name ")
          sadd=input("Enter the Staff Address ")
          scon=input("Enter the Contact No. ")        
          doj=input("Enter the Date of Join ")
          gen=input("Enter the Gender ")
          deptno=input("Enter the Department No ")
          sal=input("Enter the Salary ")          
          salgr=input("Enter the Salary Grade ")
          f=open("staff.dat","ab")
          rec=[stafId,name,sadd,scon,doj,gen,deptno,sal,salgr]
          pickle.dump(rec,f)
          f.close()
          if input("Do you want to add more?").upper()!='Y':
               break


     print('\n')
     print("Records Inserted".center(60))
     
def display(rec):
     print("Staff Id:",rec[0])
     print("-"*13)
     print("Name:",rec[1])
     print("Address:",rec[2])
     print("Contact No.:",rec[3])
     print("Date Of Join:",rec[4])
     print("Gender:",rec[5])
     print("Department No:",rec[6])
     print("Salary:",rec[7])
     print("Salary Grade:",rec[8])
     print("."*60)

#Reading the records
def readRec():
     
     try:
          f=open("staff.dat","rb")
          while True:
               try:
                    rec=pickle.load(f)
                    display(rec)
               except EOFError:
                    print("\nNO more records found")
                    break
          f.close()
     except FileNotFoundError:
          print("No files Found")
     

#Searching a record
def Search():
     print("Searching Records".center(60))
     print(("-"*20).center(60))
     try:
          infile = open('staff.dat', 'rb')
     except FileNotFoundError:
          print('No record found to search...')
          return     
     print("1. Search By Staff Id")
     print("2. Search By Name")
     print("3. Search By Gender")
     print("4. Search By Department No")
     print("="*60)
     ch=int(input("\nEnter the choice"))
     print()
     print("="*60)
     if ch==1:
          
          stid=int(input("\nEnter the Staff Id to be searched"))
          print("-"*60)
          f=open("staff.dat","rb")
          found=False
          while True:
               try:
                    rec=pickle.load(f)
                    if rec[0]==stid:
                         display(rec)
                         found=True
                         break

               except EOFError:
                    break
          if found==False:
               print("No Record Found")
          f.close()
     elif ch==2:
          sn=input("\nEnter the name of the staff")
          print("-"*60)
          f=open("staff.dat","rb")
          found=False
          while True:
               try:
                    rec=pickle.load(f)
                    if rec[1]==sn:
                         display(rec)
                         found=True
                         break

               except EOFError:
                    break
          if found==False:
               print("No Record Found")
          f.close()
     elif ch==3:
          sgen=input("\nEnter the gender")
          print("-"*60)
          f=open("staff.dat","rb")
          found=False
          while True:
               try:
                    rec=pickle.load(f)
                    if rec[5]==sgen:
                         display(rec)
                         found=True
                         break

               except EOFError:
                    break
          if found==False:
               print("No Record Found")
          f.close()
     elif ch==4:
          sdeptno=input("\nEnter the Department No")
          print("-"*60)
          f=open("staff.dat","rb")
          found=False
          while True:
               try:
                    rec=pickle.load(f)
                    if rec[6]==sdeptno:
                         display(rec)
                         found=True
                         break

               except EOFError:
                    break
          if found==False:
               print("No Record Found")
          f.close()

#Modifiying records
def Modify():
     print("Modify Record".center(60))
     print(("-"*20).center(60))
     print('\n')
     try:
          infile = open('staff.dat', 'rb')
     except FileNotFoundError:
          print('No record found to modify...')
          return
     found = False
     fout = open("temp.dat","wb")
     SId = int(input('Enter Staff Id: '))
     
     print("="*60)
     while True:
          try:
               staf = pickle.load(infile)
               if staf[0] == SId:

                    print('\nName:',staf[1])
                    ans=input('Do you want to edit(y/n)? ')
                    if ans in ['y','Y']:
                         staf[1] = input("Enter the name ")

                    print('\nAddress:',staf[2])
                    ans=input('Do you want to edit(y/n)? ')
                    if ans in ['y','Y']:
                         staf[2] =input("Enter the address: ")

                    print('\nContact Number:',staf[3])
                    ans=input('Do you want to edit(y/n)? ')
                    if ans in ['y','Y']:
                         staf[3] =input("Enter new Number: ")

                    print('\nDate Of Join:',staf[4])
                    ans=input('Do you want to edit(y/n)? ')
                    if ans in ['y','Y']:
                         staf[4] =input("Enter Date Of Join: ")

                    print('\nGender:',staf[5])
                    ans=input('Do you want to edit(y/n)? ')
                    if ans in ['y','Y']:
                         staf[5] =input("Enter the Gender: ")

                    print('\nDepartment No:',staf[6])
                    ans=input('Do you want to edit(y/n)? ')
                    if ans in ['y','Y']:
                         staf[6] =input("Enter the new Department No: ")
                         
                    print('\nSalary:',staf[7])
                    ans=input('Do you want to edit(y/n)? ')
                    if ans in ['y','Y']:
                         staf[7] =input("Enter the new salary: ")
                         
                    print('\nSalary Grade:',staf[8])
                    ans=input('Do you want to edit(y/n)? ')
                    if ans in ['y','Y']:
                         staf[8] =input("Enter new Salary Grade: ")
                         
                    pickle.dump(staf,fout)
                    found = True
                    break
               else:
                    pickle.dump(staf,fout)
          except EOFError:
               break
     if found == False:
          print('Record not Found')
     else:
          print()
          print("RECORD UPDATED".center(60))
        
     infile.close()
     fout.close()
     os.remove("staff.dat")
     os.rename("temp.dat","staff.dat")

#Deleting a record
def deleteRec(Id):
     try:
          f= open('staff.dat', 'rb')
     except FileNotFoundError:
          print('No record found to modify...')
          return

     reclst=[]
     found=False
     while True:
          try:
               rec=pickle.load(f)
               reclst.append(rec)
          except EOFError:
               break
     f.close()
     f1=open("staff2.dat","wb")
     for x in reclst:
          if x[0]==Id:
               found=True
               continue
          pickle.dump(x,f1)
     if found == False:
          print('Record not Found')
     else:
          print("\nRECORD DELETED".center(60))
     f.close()
     f1.close()
     os.remove("staff.dat")
     os.rename("staff2.dat","staff.dat")


