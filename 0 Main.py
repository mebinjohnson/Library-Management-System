from Functions import *
#___________________________________________________________________________________________________________________________________________________
design('*',75)
design("L I B R A R Y           M A N  A G E R",1)
design('*',50)
print()
print("#Student Adno Range\t:\t(1234-1377)")
print("#BookNo Range\t\t:\t(1111-2136)") 

print()

design('*',25)
design("Main Menu",1)
design('*',25)
#___________________________________________________________________________________________________________________________________________________

print ("\t1. Book Issue \n\t2. Book Deposit\n\t3. Administrator Menu\n\t4. Exit")
print()
select=input("Enter Your Selection (1-4): ")

import subprocess as sp
sp.call('cls',shell=True)
#___________________________________________________________________________________________________________________________________________________
if select=='1':
    exec(compile(open( "1 Book Issue.py").read(), "1 Book Issue.py", 'exec'))
if select=='2':
    exec(compile(open( "2 Book Deposit.py").read(), "2 Book Deposit.py", 'exec'))
elif select=='3':
    exec(compile(open( "3 Administrator Menu.py").read(), "3 Administrator Menu.py", 'exec'))
elif select=='4':
    exit()
else:
    exec(compile(open( "0 Main.py").read(), "0 Main.py", 'exec'))
#___________________________________________________________________________________________________________________________________________________
