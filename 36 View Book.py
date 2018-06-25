from Functions import *

design('*',25)
design('View Book',1)
design('*',25)

print() 

list2=book_class()

print("Total Books in Database\t:\t",Books.total_books)
print("Available Books\t\t:\t",Books.avail_books)
print("Issued  Books\t\t:\t",Books.issued_books)
print()

bookno=input("Enter the Book Number : ")


bookpos=-1
bookpos=book_search(bookno,list2,'dont print')
design('_',80)

if bookpos!=-1:
    print('Book Number\t\t :',bookpos.book_no)
    print('Book Name\t\t :',bookpos.book_name)

    print('Book Availability\t :', end=' ')
    print('Available' if bookpos.book_avail=='yes' else "Not Available")

    print('Book Issued by(Adno)\t :',bookpos.book_issue)
    if bookpos.book_issue!='None':
        list=student_class()
        pos=student_search(bookpos.book_issue,list,'dont print')
  
        print('Book Issued by(Name)\t :',pos.student_name)
        print('Book Issued Time-Date\t :',bookpos.book_time)
else:
    print("Book Not in Database")

menu_end('36 View Book.py')
