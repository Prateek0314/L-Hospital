from os import name
import tkinter as tk                
from tkinter import Button, font  as tkfont

from mysql.connector.cursor import CursorBase
from getkey import uniquekey
from tkinter.constants import INSERT
import mysql.connector
from mysql.connector import errorcode
from afs import *
unikey=uniquekey()
idd1=''
class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, RegisterPage,RegisterPatient,RegisterDoctor,LoginPage,DoctorPage,PatientPage,PharmacyPage,AppointmentPage,ViewPatients,WritePres,ViewPres):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="green")
        self.controller = controller
        self.controller.title("L'Hospital")
        self.controller.state('zoomed')
        headingLabel1=tk.Label(self,text="L'Hospital",font=('Times New Roman',45),fg='white',bg='green')
        headingLabel1.pack(pady=25)
        space=tk.Label(self,height=4,bg='green')
        space.pack()
        def Register():
            controller.show_frame("RegisterPage")
        def Enter():
            controller.show_frame("LoginPage")
        button1=tk.Button(self,text="Login",command=Enter,width=20,height=2)
        button1.pack(pady=10)
        button=tk.Button(self,text="Register ",command=Register,width=20,height=2)
        button.pack(pady=10)


class RegisterPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='green')
        self.controller = controller
        headingLabel1=tk.Label(self,text="L'Hospital",font=('Times New Roman',45),fg='white',bg='green')
        headingLabel1.pack(pady=25)
        main_menu=tk.Label(self,text='',font=('Times New Roman',25),fg='white',bg='green')
        main_menu.pack()
        selection=tk.Label(self,text='Please make a selection',font=('Times New Roman',25),fg='white',bg='green',anchor='w')
        selection.pack(fill='x')
        button_frame=tk.Frame(self,bg='green')
        button_frame.pack(fill="both",expand=True)
        def MenuPage():
            controller.show_frame("StartPage")
        button=tk.Button(button_frame,text="Go back",command=MenuPage,height=1,width=10)
        button.grid(row=0,column=0,pady=5,padx=20)
        def RegisterP():
            controller.show_frame("RegisterPatient")
        show_database=tk.Button(button_frame,text="Register Patient",command=RegisterP,height=5,width=50)
        show_database.grid(row=1,column=0,pady=5)
        def RegisterD():
            controller.show_frame("RegisterDoctor")
        search_database=tk.Button(button_frame,text="Register Doctor",command=RegisterD,height=5,width=50)
        search_database.grid(row=2,column=0,pady=5)


class RegisterPatient(tk.Frame):

    def __init__(self, parent, controller,bg='green'):
        tk.Frame.__init__(self, parent,bg='green')
        self.controller = controller
        headingLabel1=tk.Label(self,text="Register Patient",font=('Times New Roman',45),fg='white',bg='green')
        headingLabel1.pack(pady=25)
        button_frame=tk.Frame(self,bg='green')
        button_frame.pack(fill="both",expand=True)
        def MenuPage():
            controller.show_frame("RegisterPage")
        button=tk.Button(button_frame,text="Go back",command=MenuPage,height=1,width=10)
        button.grid(row=0,column=1,pady=5,padx=20)
        user_label=tk.Label(button_frame,text="Enter user",height=5,width=10,bg="green")
        user_label.grid(row=1,column=0,pady=5,padx=20)
        password_label=tk.Label(button_frame,text="Enter password",height=5,width=20,bg="green")
        password_label.grid(row=2,column=0,pady=5,padx=20)
        user1=tk.Entry(button_frame,font=('Times New Roman',20))
        user1.grid(row=1,column=1,pady=5,padx=20)
        password1=tk.Entry(button_frame,font=('Times New Roman',20),show="*")
        password1.grid(row=2,column=1,pady=5,padx=20)
        def add():
            user=str(user1.get())
            password=str(password1.get())
            con=mysql.connector.connect(host="remotemysql.com",user="nWVwUT8fN5",passwd='QQxCT6BPUx',database='nWVwUT8fN5',port='3306')
            con.autocommit=True
            cursor=con.cursor()
            from module import id1
            t=id1()
            cursor.execute("SELECT * FROM Login;")
            d=cursor.fetchall()
            for i in range(len(d)):
                if d[i][0]==t:
                    t=id1()
                else:
                    continue
            cursor.execute("INSERT INTO Login VALUES('{}','{}','{}','Patient',NULL) ".format(t,user,password))
            display=tk.Text(button_frame,height=10,width=30)
            display.grid(row=3,column=1)
            display.insert(tk.END,"Added User Successfully.Your ID number is '{}'".format(t))        
        user_button=tk.Button(button_frame,text="Add",command=add)
        user_button.grid(row=6,column=1,pady=5,padx=20)


class RegisterDoctor(tk.Frame):
    def __init__(self, parent, controller,bg='green'):
        tk.Frame.__init__(self, parent,bg='green')
        self.controller = controller
        headingLabel1=tk.Label(self,text="Register Doctor",font=('Times New Roman',45),fg='white',bg='green')
        headingLabel1.pack(pady=25)
        button_frame=tk.Frame(self,bg='green')
        button_frame.pack(fill="both",expand=True)
        def MenuPage():
            controller.show_frame("RegisterPage")
        button=tk.Button(button_frame,text="Go back",command=MenuPage,height=1,width=10)
        button.grid(row=0,column=1,pady=5,padx=20)
        user_label=tk.Label(button_frame,text="Enter user-id",height=5,width=10,bg="green")
        user_label.grid(row=1,column=0,pady=5,padx=20)
        password_label=tk.Label(button_frame,text="Enter password",height=5,width=30,bg="green")
        password_label.grid(row=2,column=0,pady=5,padx=20)
        Key_Label=tk.Label(button_frame,text="Enter the unique key",height=5,width=30,bg="green")
        Key_Label.grid(row=3,column=0,pady=5,padx=20)
        Key_Entry=tk.Entry(button_frame,font=('Times New Roman',20))
        Key_Entry.grid(row=3,column=1,pady=5,padx=20)
        dept_label=tk.Label(button_frame,text="Enter the department",height=5,width=30,bg="green")
        dept_label.grid(row=4,column=0,pady=5,padx=20)
        dept_entry=tk.Entry(button_frame,font=('Times New Roman',20))
        dept_entry.grid(row=4,column=1,pady=5,padx=20)
        user1=tk.Entry(button_frame,font=('Times New Roman',20))
        user1.grid(row=1,column=1,pady=5,padx=20)
        password1=tk.Entry(button_frame,font=('Times New Roman',20),show="*")
        password1.grid(row=2,column=1,pady=5,padx=20)
        def add():
            user=str(user1.get())
            password=str(password1.get())
            key1=str(Key_Entry.get())
            dept=str(dept_entry.get())
            if key1==uniquekey():
                con=mysql.connector.connect(host="remotemysql.com",user="nWVwUT8fN5",passwd='QQxCT6BPUx',database='nWVwUT8fN5',port='3306')
                con.autocommit=True
                cursor=con.cursor()
                from module import id1
                t=id1()
                cursor.execute("SELECT * FROM Login;")
                d=cursor.fetchall()
                for i in range(len(d)):
                    if d[i][0]==t:
                        t=id1()
                    else:
                        continue
                cursor.execute("INSERT INTO Login VALUES('{}','{}','{}','Doctor','{}') ".format(t,user,password,dept))
                cursor.execute("INSERT INTO Doctor VALUES('{}','{}','{}','NULL') ".format(t,user,dept))
                display=tk.Text(button_frame,height=10,width=30)
                display.grid(row=5,column=1)
                display.insert(tk.END,"Added User Successfully. Your ID number is '{}'".format(t))
            else:
                display=tk.Text(button_frame,height=10,width=30)
                display.grid(row=5,column=1)
                display.insert(tk.END,"Key is invalid")   
        user_button=tk.Button(button_frame,text="Add",command=add)
        user_button.grid(row=6,column=1,pady=5,padx=20)
class ViewPres(tk.Frame):
     def __init__(self, parent, controller,bg='green'):
        tk.Frame.__init__(self, parent,bg='green')
        self.controller = controller
        headingLabel1=tk.Label(self,text="L'Pharmacy",font=('Times New Roman',45),fg='white',bg='green')
        headingLabel1.pack(pady=25)
        def LPage():
            controller.show_frame("PatientPage")
        backbutton=tk.Button(self,text="Go Back",command=LPage,width=20,height=2)
        backbutton.pack()   
        button_frame=tk.Frame(self,bg='green')
        button_frame.pack(fill="both",expand=True)
        idd2=r1()
        con=mysql.connector.connect(host="remotemysql.com",user="nWVwUT8fN5",passwd='QQxCT6BPUx',database='nWVwUT8fN5',port='3306')
        con.autocommit=True
        cursor=con.cursor()
        cursor.execute("SELECT * FROM Prescription WHERE PID='{}';".format(idd2))
        d=cursor.fetchall()
        if d==[]:
            display=tk.Text(button_frame,height=10,width=30)
            display.grid(row=3,column=1)
            display.insert(tk.END,"No prescription available")
        else:
            l=["id","name",'prescription']
            s=""
            for i in d:
                j=0
                for f in i:
                    s=s+l[j]+":-"+f
                    s=s+"\n"
                    j=j+1
                s=s+"\n"
                display=tk.Text(button_frame,height=10,width=30)
                display.grid(row=3,column=1)
                display.insert(tk.END,s)


class LoginPage(tk.Frame):
    def __init__(self, parent, controller,bg='green'):
        tk.Frame.__init__(self, parent,bg='green')
        self.controller = controller
        headingLabel1=tk.Label(self,text="Login Page",font=('Times New Roman',45),fg='white',bg='green')
        headingLabel1.pack(pady=25)
        button_frame=tk.Frame(self,bg='green')
        button_frame.pack(fill="both",expand=True)
        def LPage():
            controller.show_frame("StartPage")
        backbutton=tk.Button(button_frame,text="Go Back",command=LPage,width=20,height=2)
        backbutton.grid(row=0,column=0,pady=5, padx=20)
        user_label=tk.Label(button_frame,text="Enter ID Number",height=5,width=20,bg="green")
        user_label.grid(row=1,column=0,pady=5,padx=20)
        password_label=tk.Label(button_frame,text="Enter password",height=5,width=20,bg="green")
        password_label.grid(row=2,column=0,pady=5,padx=20)
        user1=tk.Entry(button_frame,font=('Times New Roman',20))
        user1.grid(row=1,column=1,pady=5,padx=20)
        password1=tk.Entry(button_frame,font=('Times New Roman',20),show="*")
        password1.grid(row=2,column=1,pady=5,padx=20)
        def login():
            id1=str(user1.get())
            global idd1
            idd1=id1
            w1(id1)
            password=str(password1.get())
            con=mysql.connector.connect(host="remotemysql.com",user="nWVwUT8fN5",passwd='QQxCT6BPUx',database='nWVwUT8fN5',port='3306')
            con.autocommit=True
            cursor=con.cursor()
            cursor.execute("SELECT * FROM Login WHERE id='{}' and password='{}'".format(id1,password))
            d=cursor.fetchall()
            cursor.close()
            con.close()
            type24=d[0][3]
            if id1==d[0][0]:
                if type24=="Doctor":
                    controller.show_frame("DoctorPage")
                elif type24=="Patient":
                    controller.show_frame("PatientPage")
                elif type24=="Pharmacy":
                    controller.show_frame("PharmacyPage")

        user_button=tk.Button(button_frame,text="Login",command=login)
        user_button.grid(row=6,column=1,pady=5,padx=20)

class DoctorPage(tk.Frame):
    def __init__(self, parent, controller,bg='green'):
        tk.Frame.__init__(self, parent,bg='green')
        self.controller = controller
        headingLabel1=tk.Label(self,text="Doctors Front",font=('Times New Roman',45),fg='white',bg='green')
        headingLabel1.pack(pady=25)
        button_frame=tk.Frame(self,bg='green')
        button_frame.pack(fill="both",expand=True)
        def LPage():
            controller.show_frame("LoginPage")
        backbutton=tk.Button(button_frame,text="Go Back",command=LPage,width=20,height=2)
        backbutton.grid(row=0,column=0,pady=5, padx=20)
        def VPage():
            controller.show_frame("ViewPatients")
        button1=tk.Button(button_frame,text="View Patients",command=VPage,width=20,height=2)
        button1.grid(row=1,column=0,pady=5, padx=20)
        def PresP():
            controller.show_frame("WritePres")
        button2=tk.Button(button_frame,text="Write a Prescription",command=PresP,width=20,height=2)
        button2.grid(row=2,column=0,pady=5, padx=20)
class WritePres(tk.Frame):
    def __init__(self, parent, controller,bg='green'):
        tk.Frame.__init__(self, parent,bg='green')
        self.controller = controller
        headingLabel1=tk.Label(self,text="Doctors Front",font=('Times New Roman',45),fg='white',bg='green')
        headingLabel1.pack(pady=25)
        button_frame=tk.Frame(self,bg='green')
        button_frame.pack(fill="both",expand=True)
        idd2=r1()
        def LPage():
            controller.show_frame("DoctorPage")
        backbutton=tk.Button(button_frame,text="Go Back",command=LPage,width=20,height=2)
        backbutton.grid(row=0,column=0,pady=5, padx=20)
        con=mysql.connector.connect(host="remotemysql.com",user="nWVwUT8fN5",passwd='QQxCT6BPUx',database='nWVwUT8fN5',port='3306')
        con.autocommit=True
        cursor=con.cursor()
        cursor.execute("SELECT DOCNAME FROM Doctor WHERE DOCID='{}';".format(idd2))
        t=cursor.fetchall()
        t=reno(t)
        cursor.execute("SELECT PID, PNAME, APPTTIME FROM Patient WHERE DNAME='{}';".format(t))
        d=cursor.fetchall()
        l=['Patient ID, Patient Name, Appointment Time']
        a=""
        for i in d:
	        a+="Patient ID:"+i[0]+"\nPatient Name:"+i[1]+"\nAppointment Time:"+i[2]+"\n\n"
        display=tk.Text(button_frame,height=10,width=30)
        display.grid(row=7,column=0)
        display.insert(tk.END,a)
        user_label=tk.Label(button_frame,text="Enter Patient ID",height=5,width=20,bg="green")
        user_label.grid(row=2,column=0,pady=5,padx=20)
        pname_label=tk.Label(button_frame,text="Enter Patient Name",height=5,width=20,bg="green")
        pname_label.grid(row=3,column=0,pady=5,padx=20)
        pres_label=tk.Label(button_frame,text="Enter Prescription",height=5,width=20,bg="green")
        pres_label.grid(row=4,column=0,pady=5,padx=20)
        user1=tk.Entry(button_frame,font=('Times New Roman',20))
        user1.grid(row=2,column=1,pady=5,padx=20)
        pname1=tk.Entry(button_frame,font=('Times New Roman',20))
        pname1.grid(row=3,column=1,pady=5,padx=20)
        pres1=tk.Entry(button_frame,font=('Times New Roman',20))
        pres1.grid(row=4,column=1,pady=20,padx=80)
        def login():
            user=str(user1.get())
            pname=str(pname1.get())
            pres=str(pres1.get())
            con=mysql.connector.connect(host="remotemysql.com",user="nWVwUT8fN5",passwd='QQxCT6BPUx',database='nWVwUT8fN5',port='3306')
            con.autocommit=True
            cursor=con.cursor()
            cursor.execute("INSERT INTO Prescription Values('{}','{}','{}');".format(user,pname,pres))
            la3=tk.Label(button_frame,text="Prescription submitted",height=5,width=20,bg="green")
            la3.grid(row=5,column=1,pady=5,padx=20)
        user_button=tk.Button(button_frame,text="Submit Prescription",command=login)
        user_button.grid(row=6,column=1,pady=5,padx=20)

class PatientPage(tk.Frame):
    def __init__(self, parent, controller,bg='green'):
        tk.Frame.__init__(self, parent,bg='green')
        self.controller = controller
        headingLabel1=tk.Label(self,text="Patients Front",font=('Times New Roman',45),fg='white',bg='green')
        headingLabel1.pack(pady=25)
        button_frame=tk.Frame(self,bg='green')
        button_frame.pack(fill="both",expand=True)
        def LPage():
            controller.show_frame("LoginPage")
        backbutton=tk.Button(button_frame,text="Go Back",command=LPage,width=20,height=2)
        backbutton.grid(row=0,column=0,pady=5, padx=20)
        def ApPage():
            controller.show_frame("AppointmentPage")
        button1=tk.Button(button_frame,text="Book an Appointment",command=ApPage,width=20,height=2)
        button1.grid(row=1,column=0,pady=5, padx=20)
        def DpPage():
            controller.show_frame("ViewPres")
        button1=tk.Button(button_frame,text="View Prescriptions",command=DpPage,width=20,height=2)
        button1.grid(row=2,column=0,pady=5, padx=20)

class ViewPatients(tk.Frame):
    def __init__(self, parent, controller,bg='green'):
        tk.Frame.__init__(self, parent,bg='green')
        self.controller = controller
        headingLabel1=tk.Label(self,text="Doctors Front",font=('Times New Roman',45),fg='white',bg='green')
        headingLabel1.pack(pady=25)
        button_frame=tk.Frame(self,bg='green')
        button_frame.pack(fill="both",expand=True)
        def LPage():
            controller.show_frame("DoctorPage")
        backbutton=tk.Button(button_frame,text="Go Back",command=LPage,width=20,height=2)
        backbutton.grid(row=0,column=0,pady=5, padx=20)
        con=mysql.connector.connect(host="remotemysql.com",user="nWVwUT8fN5",passwd='QQxCT6BPUx',database='nWVwUT8fN5',port='3306')
        con.autocommit=True
        cursor=con.cursor()
        idd2=r1()
        cursor.execute("SELECT DOCNAME FROM Doctor WHERE DOCID='{}';".format(idd2))
        t=cursor.fetchall()
        t=reno(t)
        print(t)
        cursor.execute("SELECT PID, PNAME, APPTTIME FROM Patient WHERE DNAME='{}';".format(t))
        d=cursor.fetchall()
        print(d)
        l=['Patient ID, Patient Name, Appointment Time']
        a=""
        for i in d:
	        a+="Patient ID:"+i[0]+"\nPatient Name:"+i[1]+"\nAppointment Time:"+i[2]+"\n\n"
        display=tk.Text(button_frame,height=10,width=30)
        display.grid(row=7,column=0)
        display.insert(tk.END,a)

class AppointmentPage(tk.Frame):
    def __init__(self, parent, controller,bg='green'):
        tk.Frame.__init__(self, parent,bg='green')
        self.controller = controller
        headingLabel1=tk.Label(self,text="Patients Front",font=('Times New Roman',45),fg='white',bg='green')
        headingLabel1.pack(pady=25)
        button_frame=tk.Frame(self,bg='green')
        button_frame.pack(fill="both",expand=True)
        con=mysql.connector.connect(host="remotemysql.com",user="nWVwUT8fN5",passwd='QQxCT6BPUx',database='nWVwUT8fN5',port='3306')
        con.autocommit=True
        cursor=con.cursor()
        cursor.execute("SELECT dept,type FROM `Login`;")
        d=cursor.fetchall()
        cursor.close()
        con.close()
        options=[]
        for i in d:
            if i[0] not in options and i[1]=='Doctor':
                options.append(i[0])
            else:
                continue
        clicked=tk.StringVar()
        clicked.set("Departments")
        def PatientP():
            controller.show_frame("PatientPage")
        button=tk.Button(button_frame,text="Go back",command=PatientP,height=1,width=10)
        button.grid(row=0,column=0,pady=5,padx=20)
        drop = tk.OptionMenu( button_frame,clicked,*options)
        drop.grid(row=1,column=0,pady=5,padx=20)
        options=[]
        def confirm():
            text=clicked.get()
            con=mysql.connector.connect(host="remotemysql.com",user="nWVwUT8fN5",passwd='QQxCT6BPUx',database='nWVwUT8fN5',port='3306')
            con.autocommit=True
            cursor=con.cursor()
            cursor.execute("SELECT user FROM `Login` WHERE dept='{}';".format(text))
            d=cursor.fetchall()
            cursor.close()
            con.close()
            for i in d:
                options.append(i)
            clicked1=tk.StringVar()
            clicked1.set("Doctors")
            drop1=tk.OptionMenu(button_frame,clicked1,*options)
            drop1.grid(row=2,column=0,pady=5,padx=20)
            def confirm1():
                name1=str(clicked1.get())
                name1=reno(name1)
                print(name1)
                con=mysql.connector.connect(host="remotemysql.com",user="nWVwUT8fN5",passwd='QQxCT6BPUx',database='nWVwUT8fN5',port='3306')
                con.autocommit=True
                cursor=con.cursor()
                cursor.execute("SELECT timings FROM Doctor WHERE DOCNAME LIKE '{}';".format(name1))
                t=cursor.fetchall()
                con.close()
                t=reno1(t)
                b=t
                b.pop()
                a=''
                for i in b:
                    a=a+i+','
                print(t)
                l1=['9a.m.','10a.m.','11a.m.','12p.m.','1p.m']
                #iterating through list of occupied times
                for i in t:
                    #checking if occupied timing present in free time list
                    if i in l1:
                        l=l1.remove(i)
                    else:
                        continue
                print(l1)
                clicked3=tk.StringVar()
                clicked3.set("Timings")
                drop3=tk.OptionMenu(button_frame,clicked3,*l1)
                drop3.grid(row=3,column=0,pady=5,padx=20)
                def confirm2():
                    timings=clicked3.get()
                    c=timings
                    timings=str(timings)
                    timings=a+str(timings)+','
                    con=mysql.connector.connect(host="remotemysql.com",user="nWVwUT8fN5",passwd='QQxCT6BPUx',database='nWVwUT8fN5',port='3306')
                    con.autocommit=True
                    cursor=con.cursor()
                    idnum=idd1
                    cursor.execute("INSERT INTO Patient(PID,PNAME) SELECT id,user FROM Login WHERE id='{}';".format(idnum))
                    cursor.execute("UPDATE Patient SET DNAME='{}',APPTTIME='{}' WHERE pid='{}';".format(name1,c,idnum))
                    cursor.execute("UPDATE Doctor SET Timings='{}' WHERE DOCNAME='{}';".format(timings,name1))
                    display=tk.Text(button_frame,height=10,width=30)
                    display.grid(row=7,column=0)
                    display.insert(tk.END,"Appointment added successfully".format(t))
                button3=tk.Button(button_frame,text="Confirm",command=confirm2)
                button3.grid(row=3,column=1,pady=5,padx=20)
            button2=tk.Button(button_frame,text="Confirm",command=confirm1)
            button2.grid(row=2, column=1, pady=5, padx=20)
        button1=tk.Button(button_frame,text="Confirm",command=confirm)
        button1.grid(row=1, column=1, pady=5, padx=20)


class PharmacyPage(tk.Frame):
    def __init__(self, parent, controller,bg='green'):
        tk.Frame.__init__(self, parent,bg='green')
        self.controller = controller
        headingLabel1=tk.Label(self,text="L'Pharmacy",font=('Times New Roman',45),fg='white',bg='green')
        headingLabel1.pack(pady=25)
        def LPage():
            controller.show_frame("LoginPage")
        backbutton=tk.Button(self,text="Go Back",command=LPage,width=20,height=2)
        backbutton.pack()
        con=mysql.connector.connect(host="remotemysql.com",user="nWVwUT8fN5",passwd='QQxCT6BPUx',database='nWVwUT8fN5',port='3306')
        con.autocommit=True
        cursor=con.cursor()
        cursor.execute("SELECT PID, PNAME, PRESC FROM Prescription;")
        t=cursor.fetchall()
        a=''
        for i in t:
            a+="Patient ID:"+i[0]+"\nPatient Name:"+i[1]+"\nPrescription:"+i[2]+"\n\n"
        display=tk.Text(self,height=10,width=30)
        display.pack(fill='both')
        display.insert(tk.END,a)  
if __name__ == "__main__":
    app = App()
    app.mainloop()