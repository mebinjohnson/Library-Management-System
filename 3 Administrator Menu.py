from Functions import *
design('*',25)
design('Administrative Menu',1)
design('*',25)
design('_',80)

#____________________________________________________________________________________________________________________________________________________
print()
menu=[' Display All Student Record',' Modify Student Record',' Create Book',' Display All Books',' Delete Book',' View Book',' View Student Record',' View Issued Books',' Back to Main Menu']
for x in range (len(menu)):
    print('\t',x+1,'. ',menu[x])


design('_',80)
select=input("Enter Your Selection (1-10): ")

import subprocess as sp
sp.call('cls',shell=True)



if select=='1':
    exec(compile(open( "31 Student Record.py").read(), "31 Student Record.py", 'exec'))
elif select=='2':
    exec(compile(open( "32 Modify Student Record.py").read(), "32 Modify Student Record.py", 'exec'))
elif select=='3':
    exec(compile(open("33 Create Book.py").read(), "33 Create Book.py", 'exec'))
elif select=='4':
    exec(compile(open( "34 Books Record.py").read(), "34 Books Record.py", 'exec'))
elif select=='5':
    exec(compile(open("35 Delete Book.py").read(), "35 Delete Book.py", 'exec'))
elif select=='6':
    exec(compile(open( "36 View Book.py").read(), "36 View Book.py", 'exec'))
elif select=='7':
    exec(compile(open("37 View Student.py").read(), "37 View Student.py", 'exec'))
elif select=='8':
    exec(compile(open("38 View Issued Books.py").read(), "38 View Issued Books.py", 'exec'))
elif select=='9':
    exec(compile(open( "0 Main.py").read(), "0 Main.py", 'exec'))
else:
    exec(compile(open('3 Administrator Menu.py').read(), '3 Administrator Menu.py', 'exec'))
    


input ()
