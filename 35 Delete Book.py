head=("Delete Book")
design1='*'*75
design2='*'*25
design3='_'*80


from Functions import *

import csv

print(design2.center(80))
print(head.center(80))
print(design2.center(80))

bookno=input("Enter the Book Number to Be Deleted: ")

print()

list2=book_class()


bookpos=-1
cnt=0
for x in list2:
    if x.book_no==str(bookno):
        bookpos=x
        break
    cnt+=1

print(design3.center(80))

if bookpos!=-1:
    booknum=input('Re-Enter Book Number\t\t :')
    print(design3.center(80))

    if booknum==bookno:
            if bookpos.book_avail=='no':
                print()
                print("\nNOTE: Book Already Issued by Student.")
                list=student_class()
                pos=-1
                for x in list:
                    if x.student_no==bookpos.book_issue:
                        pos=x
                        break
                pos.student_issue='no'
                pos.student_bookno='None'
                student_save(list)
                print("\n\t Existing Book Issue Updated with Student-",pos.student_name)
            del bookpos
            list2.pop(cnt)

            book_save(list2)
            print(design3.center(80))
            print("Book Successfully Deleted.")
        
    else:
        print("\n\tBook Number Do Not Match.")        
else:
    print("Book Number Not in Database")

menu_end('35 Delete Book.py')
