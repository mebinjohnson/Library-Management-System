from Functions import *
import time
import csv

design('*',25)
design('Create Book',1)
design('*',25)
#___________________________________________________________________________________________________________________________________________________

bookno=input("Enter the Book Number to Be Created: ")

list2=book_class()
bookpos=-1

bookpos=book_search(bookno,list2)


design('_',80)

while bookpos==-1:
   booknum=input('Re-Enter Book Number\t : ')
   if (booknum)==bookno:
      bookname=input( 'Book Name\t\t : ')
      newdata=Books(booknum,bookname,'yes','None','None')
      list2.append(newdata)
      book_save(list2)
      print('\n\tNew Book Added to Database')
   else:
      print("\n\tEntered Book Number Do Not Match")
      break
   break    
else:
    print("Book Number Already in Use")

#___________________________________________________________________________________________________________________________________________________
menu_end('33 Create Book.py')
