class Books:
    avail_books=0
    total_books=0
    issued_books=0
    def __init__(self,no=0000,name='',avail='',issue='',time=''):
                 self.book_no=no
                 self.book_name=name
                 self.book_avail=avail
                 self.book_issue=issue
                 self.book_time=time
                 self.book_count()
        
    def __str__(self):
                print(str(self.book_no),str(self.book_name),str(self.book_avail))
    def book_count(self):
            Books.total_books+=1
            if self.book_avail=='yes':
                Books.avail_books+=1
            else:
                Books.issued_books+=1

#___________________________________________________________________________________________________________________________________________________

class Student:
    total_students=0
    def __init__(self,no=0000,name='',issue='',bookno=0000,grade='',section='',house=''):
        self.student_no=no
        self.student_name=name
        self.student_issue=issue
        self.student_bookno=bookno
        self.student_grade=grade
        self.student_section=section
        self.student_house=house
    def __str__(self):
        print(str(self.student_no,self.student_name))
#___________________________________________________________________________________________________________________________________________________
           
def student_class():
    import pickle
    
    Student.students_issued=0
    student_list=[]
    file1=open("Student_ID.log",'rb')
    obj=Student()
    try:
        while True:
            obj=pickle.load(file1)
            student_list.append(obj)
    except EOFError:
        file1.close()
    Student.total_students=len(student_list)
    return student_list

#print Student.total_students()
#___________________________________________________________________________________________________________________________________________________

def book_class():
    import pickle
    Books.avail_books=0
    Books.total_books=0
    Books.issued_books=0
    book_list=[]
    file1=open("Book_ID.log",'rb')
    obj=Books()
    try:
        while True:
            obj=pickle.load(file1)
            book_list.append(obj)
            obj.book_count()
    except EOFError:
        file1.close()
    return book_list

#___________________________________________________________________________________________________________________________________________________

def design(char,no=1):
    design=str(char)*int(no)
    print(design.center(80))

#___________________________________________________________________________________________________________________________________________________

def refresh(file):
    exec(compile(open( str(file)).read(), str(file), 'exec'))    

#___________________________________________________________________________________________________________________________________________________  

def menu_end(file_name= "0 Main.py"):
    design3='_'*80
    print(design3.center(80))
    print ("Selection:\n\t1. Main Menu \n\t2. Administrator Menu \n\t3. Reload \n\t4. Exit")
    select=input("Enter Selection (1-3) : ")
    import subprocess as sp
    sp.call('cls',shell=True)
    import os
    if select=='4':
        exit()
    if select=='2':
        exec(compile(open( "3 Administrator Menu.py").read(), "3 Administrator Menu.py", 'exec'))
    if select=='3':
        exec(compile(open(str(file_name)).read(), str(file_name), 'exec'))
    else:
        exec(compile(open( "0 Main.py").read(), "0 Main.py", 'exec'))

#___________________________________________________________________________________________________________________________________________________
def student_search(num,slist,state='print'):
    s_pos=-1
    for x in slist:
       if str(x.student_no)==str(num):
           s_pos=x
           if state!='dont print':
               print("\n\tMatch Found with : ",s_pos.student_name)
           break
    return s_pos
#___________________________________________________________________________________________________________________________________________________

def book_search(num,slist,state='print'):
    s_pos=-1
    for x in slist:
       if str(x.book_no)==str(num):
           s_pos=x
           if state!='dont print':
               print("\n\tMatch Found with : ",s_pos.book_name)
           break
    return s_pos
#___________________________________________________________________________________________________________________________________________________    

def book_save(save_list):
    import pickle
    file1=open("Book_ID.log",'wb')
    for x in save_list:
        pickle.dump(x,file1)
    file1.close()
 
#___________________________________________________________________________________________________________________________________________________

def student_save(save_list):
    import pickle
    file1=open("Student_ID.log",'wb')
    for x in save_list:
        pickle.dump(x,file1)
    file1.close()
#___________________________________________________________________________________________________________________________________________________

