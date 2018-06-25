import csv
from Functions import *
#___________________________________________________________________________________________________________________________________________________
head=("Modify Student Record")
design1='*'*75
design2='*'*25
design3='_'*80

print(design2.center(80))
print(head.center(80))
print(design2.center(80))
#___________________________________________________________________________________________________________________________________________________

adno=input("Enter the Admission Number of Student : ")

print()

list=student_class()

pos=-1
pos=student_search(adno,list)

print(design3.center(80))


while pos!=-1:
    print(" Select Options Below to Modify Record :- ")
    opt=['Change Name', 'Change Grade', 'Change Section','Change House']
    for x in range (len(opt)):
        print('\t',x+1,'. ',opt[x])

    selct=input("\nEnter Your Selection : ")

    print(design3.center(80))
    if selct=='1':
       new_name=input("Enter Name Modification : ")
       pos.student_name=new_name
       
    elif selct=='2':
        pos.student_grade=input("Enter New Grade : ")
        
    elif selct=='3':
        new_section=input("Enter New Section : ")
        pos.student_section=new_section
    elif selct=='4':
         new_house=input("Enter New House: ")
         pos.student_house=new_house
    else:
         break
    print("\n\tModification Successfull")
    print(design3.center(80))
    print("New Modified Record :-\n")
    print('\tAdmin Number\t\t :',pos.student_no)
    print('\tName of Student\t\t :',pos.student_name)
    print('\tGrade\t\t\t :',pos.student_grade)
    print('\tSection\t\t\t :',pos.student_section)
    print('\tHouse\t\t\t :',pos.student_house)
    break
else:
    print(design3.center(80))
    print("Match Not Found with Admin Number")


student_save(list)

#___________________________________________________________________________________________________________________________________________________
menu_end('32 Modify Student Record.py')
