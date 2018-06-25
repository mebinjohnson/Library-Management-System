from Functions import *


design('*',25)
design('View Issued Book',1)
design('*',25)

#___________________________________________________________________________________________________________________________________________________
list2=book_class()

design('-',80)
print('Book Number\tBook Name \t\tBook Issued by(Adno) \tTime-Date')
design('-',80)
for x in list2:
    if x.book_avail=='no':
        name=''
        cnt=0
        for i in x.book_name:
            cnt+=1
            name+=i
            if cnt>22:
                break

        print(x.book_no,'\t|\t',name,'  |  ',x.book_issue,'    |    ',x.book_time)

design('_',80)
print()
print("Total Books in Database\t:\t",Books.total_books)
print("Available Books\t\t:\t",Books.avail_books)
print("Issued Books\t\t:\t",Books.issued_books-1)
#___________________________________________________________________________________________________________________________________________________
menu_end('38 View Issued Books.py')
