from Functions import *

design('*',25)
design('Books Record',1)
design('*',25)
#___________________________________________________________________________________________________________________________________________________
list2=book_class()

design('*',80)

print("Book No.\t             Avalibility\t\t     Books Name")
design('*',80)

for i in list2:
               print(i.book_no,'\t.\t',i.book_name)

#___________________________________________________________________________________________________________________________________________________
menu_end('34 Books Record.py')
