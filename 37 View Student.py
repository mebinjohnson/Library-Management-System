import csv
from Functions import *

design('*',25)
design('View Student',1)
design('*',25)
#___________________________________________________________________________

list=student_class()
list2=book_class()
design('_',80)

print("Total Students: \t",Student.total_students)
print("Student Issued:\t",Books.issued_books)
design('_',80)

adno=input("Enter the Admission Number of Student : ")


design('_',80)


pos=-1
pos=student_search(adno,list,'dont print')

if pos!=-1:
   bookno=pos.student_bookno
   bookpos=-1
   bookpos=book_search(bookno,list2,'dont print')
   print('Admin Number\t\t :',pos.student_no)
   print('Name of Student\t\t :',pos.student_name)
   print('Grade\t\t\t :',pos.student_grade)
   print('Section\t\t\t :',pos.student_section)
   print('House\t\t\t :',pos.student_house)
   print('Issued Book Number\t :', end=' ') 
   print('Null' if pos.student_bookno=='None' else pos.student_bookno)

   print('Issued Book\t\t :', end=' ')#pos.student_issue,
   print('None ' if pos.student_bookno=='None' else bookpos.book_name)
   print('Book Issued Time-Date\t :', end=' ')
   print('Null ' if  pos.student_bookno=='None' else bookpos.book_time)
else:
    print("\tStudent Not in Database")


menu_end('37 View Student.py')

