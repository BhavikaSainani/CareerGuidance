from tkinter import *
import tkinter.messagebox as yy
import mysql.connector as B
from tkinter import ttk
import smtplib
link=B.connect(host="localhost",user="root",password="waheguruji")
cur=link.cursor()
root=Tk()
root.geometry("1400x700")
d=Label(root,text="CAREER GUIDANCE", font= ("Britannic Bold",45), anchor="c",fg="white", bg="black")
d.place(x=0, y=0, relwidth=1)
#====================Variables=====================
score=0
x=IntVar()
firstscore=IntVar()
secondscore=IntVar()
thirdscore=IntVar()
fourthscore=IntVar()
fifthscore=IntVar()
Name=StringVar()
DOB=StringVar()
Age=StringVar()
Contact=StringVar()
Email=StringVar()
def main():
    ab=Frame(root,bd=5, relief=RIDGE)
    ab.place(x=0, y=75, width=1365, height= 700)
    a= Label(ab,text="WHAT ARE YOU LOOKING FOR?", font= ("Arial Rounded MT Bold",32),fg="skyblue4", bg="skyblue3")
    a.place(x=200, y=40,width=930,height=70)
    b=Button(ab,text="TRADITIONAL \n COURSES",font= ("Arial Rounded MT Bold",26),fg="skyblue4", bg="skyblue2",command=question1)
    b.place(x=200, y=200,width=350,height=90)
    c=Button(ab,text="PROFESSIONAL \n COURSES",font= ("Arial Rounded MT Bold",26),fg="skyblue4", bg="skyblue2",command=prof)
    c.place(x=780, y=200,width=350,height=90)
    bs=Button(ab,text="BACK",font=("Times New Roman",20),command=ab.destroy,bg="hotpink4",fg="white")
    bs.place(x=30,y=530,width=150,height=50)
##################################PROFESSIONAL###########################
def IBC():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from Investment_Banking_Course''' )
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=prof,fg="white", bg="black")
    back2.place(x=600,  y=489)
    def e_get(ev):
        a=" >Investment Banker \n >Branch Manager \n >Credit Manager \n >Financial Analyst"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Investment_Banking_Course and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Investment_Banking_Course", font= ("Arial Rounded MT Bold",22),fg="Red",bg="white")
    e.place(x=15, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=15, y=300)
    e= Label(Table,text=" >Investment Banker \n >Branch Manager \n >Credit Manager \n >Financial Analyst", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )

def HM():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from Diploma_in_Hotel_Management''' )
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=prof,fg="white", bg="black")
    back2.place(x=600,  y=489)
    def e_get(ev):
        a=" >Hotel Manager \n >Restaurant Manager \n >Front Office Manager \n >Convention Planner"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Diploma in Hotel Management and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Diploma_in_Hotel_Management", font= ("Arial Rounded MT Bold",22),fg="Red",bg="white")
    e.place(x=15, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=15, y=300)
    e= Label(Table,text=" >Hotel Manager \n >Restaurant Manager \n >Front Office Manager \n >Convention Planner", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )

def DE():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from Diploma_in_Engineering''' )
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=prof,fg="white", bg="black")
    back2.place(x=600,  y=489)
    def e_get(ev):
        a=" >Junior Mechanical Engineer \n >Junior Construction Engineer \n >IT Assistant \n >Electrical Assistant"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Diploma_in_Engineering and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Diploma_in_Engineering", font= ("Arial Rounded MT Bold",22),fg="Red",bg="white")
    e.place(x=15, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=15, y=300)
    e= Label(Table,text=" >Junior Mechanical Engineer \n >Junior Construction Engineer \n >IT Assistant \n >Electrical Assistant", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )

def EM():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from Diploma_in_Event_Management''' )
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=prof,fg="white", bg="black")
    back2.place(x=600,  y=489)
    def e_get(ev):
        a=" >Event Management Consultancy \n >Advertising Agencies \n >Event Budgeting \n >Event Accounting"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Diploma_in_Event_Management and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Diploma_in_Event_Management", font= ("Arial Rounded MT Bold",22),fg="Red",bg="white")
    e.place(x=15, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=15, y=300)
    e= Label(Table,text=" >Event Management Consultancy \n >Advertising Agencies \n >Event Budgeting \n >Event Accounting", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )

def DA():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from Diploma_in_Animation''' )
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=prof,fg="white", bg="black")
    back2.place(x=600,  y=489)
    def e_get(ev):
        a=" >Animator \n >Texture Artist \n >Image Editor \n >Lighting Artist"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Diploma_in_Animation and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Diploma_in_Animation", font= ("Arial Rounded MT Bold",22),fg="Red",bg="white")
    e.place(x=15, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=15, y=300)
    e= Label(Table,text=" >Animator \n >Texture Artist \n >Image Editor \n >Lighting Artist", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )


def DBM():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from Diploma_in_Business_Management''' )
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=prof,fg="white", bg="black")
    back2.place(x=600,  y=489)
    def e_get(ev):
        a=" >Business Consultant \n >Business Administration Researcher \n >Marketing Executive \n >Sales Executive"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Diploma_in_Business_Management and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Diploma_in_Business_Management", font= ("Arial Rounded MT Bold",22),fg="Red",bg="white")
    e.place(x=15, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=15, y=300)
    e= Label(Table,text=" >Business Consultant \n >Business Administration Researcher \n >Marketing Executive \n >Sales Executive", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )

def DIT():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from Diploma_in_Information_Technology''' )
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=prof,fg="white", bg="black")
    back2.place(x=600,  y=489)
    def e_get(ev):
        a=" >IT Specialist \n >IT Programmer \n >Web Developer \n >Computer Network Professional \n >Technical Consultant"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Diploma_in_Information_Technology and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Diploma_in_Information_Technology", font= ("Arial Rounded MT Bold",22),fg="Red",bg="white")
    e.place(x=15, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=15, y=300)
    e= Label(Table,text=" >IT Specialist \n >IT Programmer \n >Web Developer \n >Computer Network Professional \n >Technical Consultant", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )
    
def prof():
    eff=Frame(root,bd=5, relief=RIDGE,bg="rosybrown1")
    eff.place(x=0, y=75, width=1365, height= 700)
    back4=Button(eff, text= "Investment Banking Course",font= ("Arial Rounded MT Bold",25),command=IBC,fg="white", bg="hotpink4")
    back4.place(x=10, y=5)
    back4=Button(eff, text= "Diploma in Hotel Management",font= ("Arial Rounded MT Bold",25),command=HM,fg="white", bg="hotpink4")
    back4.place(x=10, y=95)
    back4=Button(eff, text= "Diploma in Engineering",font= ("Arial Rounded MT Bold",25),command=DE,fg="white", bg="hotpink4")
    back4.place(x=10, y=195)
    back4=Button(eff, text= "Diploma in Event Management",font= ("Arial Rounded MT Bold",25),command=EM,fg="white", bg="hotpink4")
    back4.place(x=10, y=285)
    back4=Button(eff, text= "Diploma in Animation",font= ("Arial Rounded MT Bold",25),command=DA,fg="white", bg="hotpink4")
    back4.place(x=10, y=375)
    back4=Button(eff, text= "Diploma in Business Management",font= ("Arial Rounded MT Bold",25),command=DBM,fg="white", bg="hotpink4")
    back4.place(x=10, y=465)
    back4=Button(eff, text= "Diploma in Information Technology",font= ("Arial Rounded MT Bold",25),command=DIT,fg="white", bg="hotpink4")
    back4.place(x=10, y=555)
    back4=Button(eff, text= "Back",font= ("Arial Rounded MT Bold",25),command=main,fg="white", bg="hotpink4")
    back4.place(x=800, y=500)
def database():
    cur.execute("create database if not exists bhaviii2")
    cur.execute ("use bhaviii2")
    cur.execute("create table if not exists Science (Sr_No int, Courses varchar(100), College varchar(100), City varchar(100),State varchar(100),Duration varchar(100))")
    cur.execute("delete from Science")
    cur.execute("insert into Science values(1, 'MBBS','St Johns Medical College', 'Bangalore', 'Karnataka','5 Years')")
    cur.execute("insert into Science values(2, 'MBBS','All India Institute of Medical Sciences', 'New Delhi', 'Delhi','5 Years')")
    cur.execute("insert into Science values(3, 'MBBS','Christian Medical College', 'Vellore','Tamil Nadu','5 Years')")
    cur.execute("insert into Science values(4, 'MBBS','Kasturba Medical College', 'Mangalore','Mangaluru','5 Years')")
    cur.execute("insert into Science values(5, 'MBBS','MS Ramaiah Medical College', 'Bangalore', 'Karnataka','5 Years')")
    cur.execute("insert into Science values(6, 'MBBS','Armed Forces Medical College', 'Pune', 'Maharashtra','5 Years')")
    cur.execute("insert into Science values(7, 'MBBS','Banaras Hindu University', 'Varanasi','Varanasi','5 Years')")
    cur.execute("insert into Science values(8, 'MBBS','Grant Medical College', 'Mumbai', 'Maharashtra','5 Years')")
    cur.execute("insert into Science values(9, 'MBBS','King Georges Medical University', 'Lucknow','Uttar Pradesh','5 Years')")
    cur.execute("insert into Science values(10, 'MBBS','B.J Medical College', 'Ahmedabad', 'Gujarat','5 Years')")
    cur.execute("insert into Science values(11, 'MBBS','B.J Medical College', 'Ahmedabad', 'Gujarat','5 Years')")
    cur.execute("insert into Science values(1, 'B.E/B.Tech','Sathyabama Institute of Science & Technology', 'Chennai', 'Tamil Nadu','3Years/ 4Years')")
    cur.execute("insert into Science values(2, 'B.E/B.Tech','Chandigarh University', 'Chandigarh', 'Punjab','3Years/ 4Years')")
    cur.execute("insert into Science values(3, 'B.E/B.Tech','Indian Institute of Technology', 'Mumbai', 'Maharashtra','3Years/ 4Years')")
    cur.execute("insert into Science values(4, 'B.E/B.Tech','LNM Institute of Information Technology', 'Jaipur', 'Rajasthan','3Years/ 4Years')")
    cur.execute("insert into Science values(5, 'B.E/B.Tech','Symbiosis International University', 'Pune', 'Maharashtra','3Years/ 4Years')")
    cur.execute("insert into Science values(6, 'B.E/B.Tech','Colloge of Engineering', 'Pune', 'Maharashtra','3Years/ 4Years')")
    cur.execute("insert into Science values(7, 'B.E/B.Tech','Institute of Technology, Nirma University', 'Ahmedabad', 'Gujarat','3Years/ 4Years')")
    cur.execute("insert into Science values(8, 'B.E/B.Tech','Indian institute of technology', 'Madras', 'Tamil Nadu','3Years/ 4Years')")
    cur.execute("insert into Science values(9, 'B.E/B.Tech','BMS College of Engineering', 'Bangalore', 'Karnataka','3Years/ 4Years')")
    cur.execute("insert into Science values(10, 'B.E/B.Tech','Andhra University College of Engineering', 'Viskhapatnam', 'Andhra Pradesh','3Years/ 4Years')")
    cur.execute("insert into Science values(1, 'Bachelor of Pharmacy', 'Institute of Chemical Technology', 'Mumbai', 'Maharashtra','4 Years')")
    cur.execute("insert into Science values(2, 'Bachelor of Pharmacy', 'Punjab University', 'Chandigarh', 'Punjab','4 Years')")
    cur.execute("insert into Science values(3, 'Bachelor of Pharmacy', 'L.M. College of Pharmacy', 'Ahmedabad', 'Gujarat','4 Years')")
    cur.execute("insert into Science values(4, 'Bachelor of Pharmacy', 'The Maharaja Sayajirao University', 'Vadodara', 'Gujarat','4 Years')")
    cur.execute("insert into Science values(5, 'Bachelor of Pharmacy', 'Birla Institute of Technology', 'Ranchi', 'Jharkhand','4 Years')")
    cur.execute("insert into Science values(6, 'Bachelor of Pharmacy', 'JSS College of Pharmacy', 'Ooty', 'Tamil Nadu','4 Years')")
    cur.execute("insert into Science values(7, 'Bachelor of Pharmacy', 'Poona College of Pharmacy', 'Pune', 'Maharashtra','4 Years')")
    cur.execute("insert into Science values(1, 'Bachelor of Homeopathic Medicine & Surgery', 'State Ayurvedic College & Hospital', 'Lucknow', 'Uttar Pradesh','5+Years')")
    cur.execute("insert into Science values(2, 'Bachelor of Homeopathic Medicine & Surgery', 'Lokmanya Homeopathic Medical College', 'Pune', 'Maharashtra','5+Years')")
    cur.execute("insert into Science values(3, 'Bachelor of Homeopathic Medicine & Surgery', 'National Institute of Homeopathy', 'Kolkata', 'West Bengal','5+Years')")
    cur.execute("insert into Science values(4, 'Bachelor of Homeopathic Medicine & Surgery', 'Ram Krishna College of Homeopathy & Medical Sciences', 'Bhopal', 'Madhya Pradesh','5+Years')")
    cur.execute("insert into Science values(5, 'Bachelor of Homeopathic Medicine & Surgery', 'Yenepoya University', 'Mangalore', 'Karnataka','5+Years')")
    cur.execute("insert into Science values(6, 'Bachelor of Homeopathic Medicine & Surgery', 'Naiminath Homeopathic Medical College Hospital & Research Centre', 'Agra', 'Uttar Pradesh','5+Years')")
    cur.execute("insert into Science values(7, 'Bachelor of Homeopathic Medicine & Surgery', 'Anand Homeopathic Medical College Hospital & Research Institute', 'Anand', 'Gujarat','5+Years')")
    cur.execute("insert into Science values(8, 'Bachelor of Homeopathic Medicine & Surgery', 'Sarvepalli Radhakrishnan University', 'Bhopal', 'Madhya Pradesh','5+Years')")
    cur.execute("insert into Science values(1, 'Bachelor of Science in Nursing', 'All India Institute of Medical Sciences', 'New Delhi', 'Delhi','3 Years')")
    cur.execute("insert into Science values(2, 'Bachelor of Science in Nursing', 'Aligarh Muslim University', 'Aligarh', 'Uttar Pradesh','3 Years')")
    cur.execute("insert into Science values(3, 'Bachelor of Science in Nursing', 'Christian Medical College', 'Ludhiana','Punjab','3 Years')")
    cur.execute("insert into Science values(4, 'Bachelor of Science in Nursing', 'King George Medical University', 'Lucknow', 'Uttar Pradesh','3 Years')")
    cur.execute("insert into Science values(5, 'Bachelor of Science in Nursing', 'M.M. Singhi Institute of Nursing', 'Ahmedabad', 'Gujarat','3 Years')")
    cur.execute("insert into Science values(6, 'Bachelor of Science in Nursing', 'Kasturba Medical College', 'Mangalore', 'Karnataka','3 Years')")
    cur.execute("insert into Science values(7, 'Bachelor of Science in Nursing', 'Guru Gobind Singh Indraprastha University', 'New Delhi', 'Delhi','3 Years')")
    cur.execute("insert into Science values(8, 'Bachelor of Science in Nursing', 'Saveetha Medical College', 'Chennai', 'Tamil Nadu','3 Years')")
    cur.execute("insert into Science values(1, 'Bachelor of Science in Information Technology', 'Thiagarajar College', 'Madurai', 'Tamil Nadu','3 Years')")
    cur.execute("insert into Science values(2, 'Bachelor of Science in Information Technology', 'Jai Hind College', 'Mumbai', 'Maharashtra','3 Years')")
    cur.execute("insert into Science values(3, 'Bachelor of Science in Information Technology', 'Dr. N.G.P.Arts & Science College', 'Coimbatore', 'Tamil Nadu','3 Years')")
    cur.execute("insert into Science values(4, 'Bachelor of Science in Information Technology', 'Birla Institute of Technology', 'Ranchi', 'Jharkhand','3 Years')")
    cur.execute("insert into Science values(5, 'Bachelor of Science in Information Technology', 'Brainware University', 'Kolkata', 'West Bengal','3 Years')")
    cur.execute("insert into Science values(6, 'Bachelor of Science in Information Technology', 'Vidyalankar School of Information Technology', 'Mumbai', 'Maharashtra','3 Years')")
    cur.execute("insert into Science values(7, 'Bachelor of Science in Information Technology', 'M.G Science Institute', 'Ahmedabad', 'Gujarat','3 Years')")
    cur.execute("insert into Science values(8, 'Bachelor of Science in Information Technology', 'GLS University', 'Ahmedabad', 'Gujarat','3 Years')")
    cur.execute("insert into Science values(9, 'Bachelor of Science in Information Technology', 'Government Holkar Science College', 'Indore', 'Madhya Pradesh','3 Years')")
    cur.execute("insert into Science values(10, 'Bachelor of Science in Information Technology', 'Bangalore University', 'Bangalore', 'Karnataka','3 Years')")
    link.commit()
database()
def database2():
    cur.execute ("use bhaviii2")
    cur.execute("create table if not exists Commerce (Sr_No int, Courses varchar(100), College varchar(100), City varchar(100),State varchar(100),Duration varchar(100))")
    cur.execute("delete from Commerce")
    cur.execute("insert into Commerce values(1, 'Bachelor of Commerce','H.L.College of Commerce', 'Ahmedabad', 'Gujarat','3 Years')")
    cur.execute("insert into Commerce values(2, 'Bachelor of Commerce','BML Munjal University', 'Gurgaon', 'Haryana','3 Years')")
    cur.execute("insert into Commerce values(3, 'Bachelor of Commerce','Loyala College', 'Chennai', 'Tamil Nadu','3 Years')")
    cur.execute("insert into Commerce values(4, 'Bachelor of Commerce','St.Xaviers College', 'Mumbai', 'Maharashtra','3 Years')")
    cur.execute("insert into Commerce values(5, 'Bachelor of Commerce','Hindu College', 'New Delhi', 'Delhi','3 Years')")
    cur.execute("insert into Commerce values(6, 'Bachelor of Commerce','Christ University', 'Bangalore', 'Karnataka','3 Years')")
    cur.execute("insert into Commerce values(7, 'Bachelor of Commerce','Symbiosis College of Commerce', 'Pune', 'Maharashtra','3 Years')")
    cur.execute("insert into Commerce values(8, 'Bachelor of Commerce','Gujarat University', 'Ahmedabad', 'Gujarat','3 Years')")
    cur.execute("insert into Commerce values(9, 'Bachelor of Commerce','Shri Ram College of Commerce', 'New Delhi', 'Delhi','3 Years')")
    cur.execute("insert into Commerce values(10, 'Bachelor of Commerce','St Johns Medical College', 'Bangalore', 'Karnataka','3 Years')")
    cur.execute("insert into Commerce values(11, 'Bachelor of Commerce','Nirma University', 'Ahmedabad', 'Gujarat','3 Years')")
    cur.execute("insert into Commerce values(1, 'Bachelor of Business Administration','Madras Christian University', 'Chennai', 'Tamil Nadu','3 Years')")
    cur.execute("insert into Commerce values(2, 'Bachelor of Business Administration','Jai Hind College', 'Mumbai', 'Maharashtra','3 Years')")
    cur.execute("insert into Commerce values(3, 'Bachelor of Business Administration','Deen Dayal Upadhyay College', 'Delhi', 'New Delhi','3 Years')")
    cur.execute("insert into Commerce values(4, 'Bachelor of Business Administration','Narsee Monjee Institute of Management Studies', 'Mumbai', 'Maharashtra','3 Years')")
    cur.execute("insert into Commerce values(5, 'Bachelor of Business Administration','Woxsen University', 'Hyderabad', 'Telangana','3 Years')")
    cur.execute("insert into Commerce values(6, 'Bachelor of Business Administration','KIIT School of Management', 'Bhubaneshwar', 'Orissa','3 Years')")
    cur.execute("insert into Commerce values(7, 'Bachelor of Business Administration','Jamia Millia Islamia University', 'New Delhi', 'Delhi','3 Years')")
    cur.execute("insert into Commerce values(8, 'Bachelor of Business Administration','Institute of Management,Nirma University', 'Ahmedabad', 'Gujarat','3 Years')")
    cur.execute("insert into Commerce values(9, 'Bachelor of Business Administration','Alliance University', 'Bangalore', 'Karnataka','3 Years')")
    cur.execute("insert into Commerce values(10, 'Bachelor of Business Administration','Lovely Professional University', 'Jalandhar', 'Punjab','3 Years')")
    cur.execute("insert into Commerce values(1, 'Chartered Accountancy','Arihant Institute of Commerce & Mangament', 'Bangalore', 'Karnataka','4+ Years')")
    cur.execute("insert into Commerce values(2, 'Chartered Accountancy','Indian Institute of Finance & Accounts', 'Pune', 'Maharashtra','4+ Years')")
    cur.execute("insert into Commerce values(3, 'Chartered Accountancy','EduPristine', 'Mumbai', 'Maharashtra','4+ Years')")
    cur.execute("insert into Commerce values(4, 'Chartered Accountancy','Arihant Institute of Commerce & Mangament', 'Bangalore', 'Karnataka','4+ Years')")
    cur.execute("insert into Commerce values(5, 'Chartered Accountancy','Institute of Chartered Accountants', 'Noida', 'Uttar Pradesh','4+ Years')")
    cur.execute("insert into Commerce values(6, 'Chartered Accountancy','Navkar Institute', 'Ahmedabad', 'Gujarat','4+ Years')")
    cur.execute("insert into Commerce values(7, 'Chartered Accountancy','ATM Global Business School', 'Delhi', 'New Delhi','4+ Years')")
    cur.execute("insert into Commerce values(8, 'Chartered Accountancy','FINPLAN-International Institute of Mangament', 'Mumbai', 'Maharashtra','4+ Years')")
    cur.execute("insert into Commerce values(9, 'Chartered Accountancy','Nizam College', 'Hyderabad', 'Karnataka','4+ Years')")
    cur.execute("insert into Commerce values(10, 'Chartered Accountancy','Shri Ram College of Commerce', 'Delhi', 'New Delhi','4+ Years')")
    cur.execute("insert into Commerce values(11, 'Chartered Accountancy','Ahmedabad Branch Of ICAI', 'Ahmedabad', 'Gujarat','4+ Years')")
    cur.execute("insert into Commerce values(1, 'Company Secretary','Institute of Company Secretaries of India', 'Delhi', 'New Delhi','3 Years')")
    cur.execute("insert into Commerce values(2, 'Company Secretary','Navkar Institute', 'Ahmedabad', 'Gujarat','3 Years')")
    cur.execute("insert into Commerce values(3, 'Company Secretary','Elite IIT', 'Bangalore', 'Karnataka','3 Years')")
    cur.execute("insert into Commerce values(4, 'Company Secretary','Ahmedabad Branch Of ICAI', 'Ahmedabad', 'Gujarat','3 Years')")
    cur.execute("insert into Commerce values(5, 'Company Secretary','Finovative Solutions', 'Mumbai', 'Maharashtra','3 Years')")
    cur.execute("insert into Commerce values(6, 'Company Secretary','Samarthya Institute of Professional Studies', 'Dehradun', 'Uttarakhand','3 Years')")
    cur.execute("insert into Commerce values(7, 'Company Secretary','Commerce & Management', 'Delhi', 'New Delhi','3 Years')")
    cur.execute("insert into Commerce values(8, 'Company Secretary','Sidharth Academy', 'Mumbai', 'Maharashtra','3 Years')")
    cur.execute("insert into Commerce values(9, 'Company Secretary','Expro Education', 'Delhi', 'New Delhi','3 Years')")
    cur.execute("insert into Commerce values(10, 'Company Secretary','Academy of Commerce', 'Gugaon', 'Haryana','3 Years')")
    cur.execute("insert into Commerce values(1, 'Bachelors of Law (LLB)','National Law School of India University', 'Bangalore', 'Karnataka','3 Years')")
    cur.execute("insert into Commerce values(2, 'Bachelors of Law (LLB)','Jindal Global Law School', 'Haryana', 'Punjab','3 Years')")
    cur.execute("insert into Commerce values(3, 'Bachelors of Law (LLB)','National Law University', 'Delhi', 'New Delhi','3 Years')")
    cur.execute("insert into Commerce values(4, 'Bachelors of Law (LLB)','Aligarh Muslim University', 'Aligarh', 'Uttar Pradesh','3 Years')")
    cur.execute("insert into Commerce values(5, 'Bachelors of Law (LLB)','Symbiosis Law School', 'Ahmedabad', 'Gujarat','3 Years')")
    cur.execute("insert into Commerce values(6, 'Bachelors of Law (LLB)','National Law Institute University', 'Bhopal', 'Madhya Pradesh','3 Years')")
    cur.execute("insert into Commerce values(7, 'Bachelors of Law (LLB)','Army Institute of Law', 'Mohali', 'Punjab','3 Years')")
    cur.execute("insert into Commerce values(8, 'Bachelors of Law (LLB)','Nirma University', 'Ahmedabad', 'Gujarat','3 Years')")
    cur.execute("insert into Commerce values(9, 'Bachelors of Law (LLB)','Chanakya National Law University', 'Patna', 'Bihar','3 Years')")
    cur.execute("insert into Commerce values(10, 'Bachelors of Law (LLB)','Banaras Hindu University', 'Varanasi', 'Uttar Pradesh','3 Years')")
    cur.execute("insert into Commerce values(1, 'Cost & Management Accountant','The Institute of Cost Accountants of India', 'Bangalore', 'Karnataka','3 Years')")
    cur.execute("insert into Commerce values(2, 'Cost & Management Accountant','Narsee Monjee College of Commerce & Economics', 'Mumbai', 'Maharashtra','3 Years')")
    cur.execute("insert into Commerce values(3, 'Cost & Management Accountant','Bharathy Educational Central', 'Namakkal', 'Uttar Pradesh','3 Years')")
    cur.execute("insert into Commerce values(4, 'Cost & Management Accountant','GC Rao Academy', 'Bangalore', 'Karnataka','3 Years')")
    cur.execute("insert into Commerce values(5, 'Cost & Management Accountant','Knowledge Academy Research & Education', 'Ernakulam', 'Kerala','3 Years')")
    cur.execute("insert into Commerce values(6, 'Cost & Management Accountant','Sahradaya College of Advanced Studies', 'Thrissur', 'Kerala','3 Years')")
    cur.execute("insert into Commerce values(7, 'Cost & Management Accountant','NGS Proffesional Academy', 'Hyderabad', 'Telangana','3 Years')")
    cur.execute("insert into Commerce values(8, 'Cost & Management Accountant','Jivkaran Institute of Business Administration', 'Anand', 'Gujarat','3 Years')")
    cur.execute("insert into Commerce values(9, 'Cost & Management Accountant','The Adamas University', 'Kolkata', 'West Bengal','3 Years')")
    cur.execute("insert into Commerce values(10, 'Cost & Management Accountant','International College of Financial Planning', 'Lucknow', 'Uttar Pradesh','3 Years')")
    cur.execute("insert into Commerce values(1, 'Certified Financial Planner','International College of Financial Planning', 'New Delhi', 'Delhi','3 Years')")
    cur.execute("insert into Commerce values(2, 'Certified Financial Planner','Indian Institute of Financial Planning', 'New Delhi', 'Delhi','3 Years')")
    cur.execute("insert into Commerce values(3, 'Certified Financial Planner','International College of Financial Planning', 'Mysore', 'Karnataka','3 Years')")
    cur.execute("insert into Commerce values(4, 'Certified Financial Planner','International College of Financial Planning', 'Chennai', 'Tamil Nadu','3 Years')")
    cur.execute("insert into Commerce values(5, 'Certified Financial Planner','Virtual Voyage College of Design, Media,Art & Management', 'Indore', 'Madhya Pradesh','3 Years')")
    cur.execute("insert into Commerce values(6, 'Certified Financial Planner','International College of Financial Planning', 'Mumbai', 'Maharashtra','3 Years')")
    cur.execute("insert into Commerce values(7, 'Certified Financial Planner','International College of Financial Planning', 'Kolkata', 'West Bengal','3 Years')")
    cur.execute("insert into Commerce values(8, 'Certified Financial Planner','International Institute of Financial Markets', 'New Delhi', 'Delhi','3 Years')")
    cur.execute("insert into Commerce values(1, 'Bachelors in Computer Application','Ambedkar Institute of Technology', 'New Delhi', 'Delhi','3 Years')")
    cur.execute("insert into Commerce values(2, 'Bachelors in Computer Application','Aliah University', 'Kolkata', 'West Bengal','3 Years')")
    cur.execute("insert into Commerce values(3, 'Bachelors in Computer Application','St Xaviers College', 'Ahmedabad', 'Gujarat','3 Years')")
    cur.execute("insert into Commerce values(4, 'Bachelors in Computer Application','Sutex Bank College of Computer Application & Science', 'Surat', 'Gujarat','3 Years')")
    cur.execute("insert into Commerce values(5, 'Bachelors in Computer Application','Nizam College', 'Hyderabad', 'Telangana','3 Years')")
    cur.execute("insert into Commerce values(6, 'Bachelors in Computer Application','JC Bose University of Science & Technology', 'Faridabad', 'Haryana','3 Years')")
    cur.execute("insert into Commerce values(7, 'Bachelors in Computer Application','Dr Babasaheb Ambedkar Open University', 'Ahmedabad', 'Gujarat','3 Years')")
    cur.execute("insert into Commerce values(8, 'Bachelors in Computer Application','Jain University', 'Bangalore', 'Karnataka','3 Years')")
    cur.execute("insert into Commerce values(9, 'Bachelors in Computer Application','Presidency College', 'Chennai', 'Tamil Nadu','3 Years')")
    cur.execute("insert into Commerce values(10, 'Bachelors in Computer Application','Government Holkar Science College', 'Indore', 'Madhya Pradesh','3 Years')")
    link.commit()
database2()
def database3():
    cur.execute ("use bhaviii2")
    cur.execute("create table if not exists Arts (Sr_No int, Courses varchar(100), College varchar(100), City varchar(100),State varchar(100),Duration varchar(100))")
    cur.execute("delete from Arts")
    cur.execute("insert into Arts values(1, 'Bachelor of Arts','Parul University', 'Vadodara', 'Gujarat','3 Years')")
    cur.execute("insert into Arts values(2, 'Bachelor of Arts','Shiv Nadar University', 'New Delhi', 'Delhi NCR','3 Years')")
    cur.execute("insert into Arts values(3, 'Bachelor of Arts','Loyola College', 'Chennai', 'Tamil Nadu','3 Years')")
    cur.execute("insert into Arts values(4, 'Bachelor of Arts','BML Munjal University', 'Gurgaon', 'Haryana','3 Years')")
    cur.execute("insert into Arts values(5, 'Bachelor of Arts','St. Xaviers College', 'Mumbai', 'Maharashtra','3 Years')")
    cur.execute("insert into Arts values(6, 'Bachelor of Arts','Christ University', 'Bangalore', 'Karnataka','3 Years')")
    cur.execute("insert into Arts values(7, 'Bachelor of Arts','Miranda House', 'New Delhi', 'Delhi NCR','3 Years')")
    cur.execute("insert into Arts values(8, 'Bachelor of Arts','Presidency College', 'Chennai', 'Tamil Nadu','3 Years')")
    cur.execute("insert into Arts values(9, 'Bachelor of Arts','Fergusson College', 'Pune', 'Maharashtra','3 Years')")
    cur.execute("insert into Arts values(10, 'Bachelor of Arts','St. Xaviers College', 'Ahmedabad', 'Gujarat','3 Years')")
    cur.execute("insert into Arts values(11, 'Bachelor of Arts','Kamla Nehru College for Women', 'Kapurthala', 'Punjab','3 Years')")
    cur.execute("insert into Arts values(1, 'Bachelor of Fine Arts','Kamla Nehru College for Women', 'Kapurthala', 'Punjab','3 Years')")
    cur.execute("insert into Arts values(2, 'Bachelor of Fine Arts','Banasthali Vidyapith', 'Jaipur', 'Rajasthan','3 Years')")
    cur.execute("insert into Arts values(3, 'Bachelor of Fine Arts','Chhatrapati Shahu Ji Maharaj University', 'Kanpur', 'Uttar Pradesh','3 Years')")
    cur.execute("insert into Arts values(4, 'Bachelor of Fine Arts','University of Lucknow', 'Lucknow', 'Uttar Pradesh','3 Years')")
    cur.execute("insert into Arts values(5, 'Bachelor of Fine Arts','J.V.Jain College', 'Saharanpur', 'Uttar Pradesh','3 Years')")
    cur.execute("insert into Arts values(6, 'Bachelor of Fine Arts','Atal Bihari Vajpayee Hindi Vishwavidyalaya', 'Bhopal', 'Madhya Pradesh','3 Years')")
    cur.execute("insert into Arts values(7, 'Bachelor of Fine Arts','Patna University', 'Patna', 'Bihar','3 Years')")
    cur.execute("insert into Arts values(8, 'Bachelor of Fine Arts','Dr Babasaheb Ambedkar Marathwada University', 'Aurangabad', 'Maharashtra','3 Years')")
    cur.execute("insert into Arts values(9, 'Bachelor of Fine Arts','Mahatma Gandhi Kashi Vidyapith', 'Varanasi', 'Uttar Pradesh','3 Years')")
    cur.execute("insert into Arts values(10, 'Bachelor of Fine Arts','Stella Maris College', 'Chennai', 'Tamil Nadu','3 Years')")
    cur.execute("insert into Arts values(11, 'Bachelor of Fine Arts','Pragjyotish College', 'Guwahati', 'Assam','3 Years')")
    cur.execute("insert into Arts values(1, 'Bachelor of Education','University of Bombay(Deptt of Education)', 'Mumbai', 'Maharashtra','2-4 Years')")
    cur.execute("insert into Arts values(2, 'Bachelor of Education','Andhra University', 'Vishakhapatnam', 'Andhra Pradesh','2-4 Years')")
    cur.execute("insert into Arts values(3, 'Bachelor of Education','Government College of Education', 'Chandigarh', 'Punjab','2-4 Years')")
    cur.execute("insert into Arts values(4, 'Bachelor of Education','St. Xaviers College of Education', 'Patna', 'Bihar','2-4 Years')")
    cur.execute("insert into Arts values(5, 'Bachelor of Education','D.M.College of Teacher Education', 'Imphal', 'Manipur','2-4 Years')")
    cur.execute("insert into Arts values(6, 'Bachelor of Education','Himachal Pradesh University(Department of Education)', 'Shimla', 'Himachal Pardesh','2-4 Years')")
    cur.execute("insert into Arts values(7, 'Bachelor of Education','A.G Teachers College', 'Ahmedabad', 'Gujarat','2-4 Years')")
    cur.execute("insert into Arts values(8, 'Bachelor of Education','University of Pune', 'Pune', 'Maharashtra','2-4 Years')")
    cur.execute("insert into Arts values(9, 'Bachelor of Education','Jamila Milia Islamia University', 'Delhi', 'New Delhi','2-4 Years')")
    cur.execute("insert into Arts values(10, 'Bachelor of Education','Kirorimal College of Education', 'Bhiwani', 'Haryana','2-4 Years')")
    cur.execute("insert into Arts values(1, 'Journalism & Mass Communication','Indian Institute of Mass Communication', 'New Delhi', 'Delhi','3 Years')")
    cur.execute("insert into Arts values(2, 'Journalism & Mass Communication','LJ Institute of Media & Communition', 'Ahmedabad', 'Gujarat','3 Years')")
    cur.execute("insert into Arts values(3, 'Journalism & Mass Communication','Symbiosis Institute of Media & Communition', 'Pune', 'Maharashtra','3 Years')")
    cur.execute("insert into Arts values(4, 'Journalism & Mass Communication','Savitribai Phule Pune University', 'Pune', 'Maharashtra','3 Years')")
    cur.execute("insert into Arts values(5, 'Journalism & Mass Communication','University of Hyderabad', 'Hyderabad', 'Telangana','3 Years')")
    cur.execute("insert into Arts values(6, 'Journalism & Mass Communication','Manipal Institute of Communication', 'Manipal', 'Karnataka','3 Years')")
    cur.execute("insert into Arts values(7, 'Journalism & Mass Communication','Xavier Institute of Communication', 'Mumbai', 'Maharashtra','3 Years')")
    cur.execute("insert into Arts values(8, 'Journalism & Mass Communication','Christ University', 'Bangalore', 'Karnataka','3 Years')")
    cur.execute("insert into Arts values(9, 'Journalism & Mass Communication','Indian Institute of Journalism & Media', 'Bangalore', 'Karnataka','3 Years')")
    cur.execute("insert into Arts values(10, 'Journalism & Mass Communication','Manorama School of Communication', 'Kottayam', 'Kerala','3 Years')")
    link.commit()
database3()
def reg_saving():
    global f1
    if Name.get()=="" or DOB.get()=="" or Age.get=="" or Contact.get()=="" or Email.get()=="":
        yy.showerror("Error","All fields are required")
    else:
        namehai=Name.get()
        birthhai=DOB.get()
        agehai=Age.get()
        number=Contact.get()
        idemail=Email.get()
        cur.execute("create database if not exists bhaviii2")
        cur.execute("use bhaviii2")
        cur.execute('''create table if not exists puff(Name varchar(25),DOB varchar(25),Age varchar(25),Contact varchar(25),Email varchar(50))''')
        sql="insert into puff(Name,DOB,Age,Contact,Email) values(%s,%s,%s,%s,%s)"
        cur.execute(sql,(namehai,birthhai,agehai,number,idemail,))
        link.commit()
        yy.showinfo("Information!!","Details Saved Successfully")
        main()
def op():
    reg_saving()
def register():
    f1=Frame(root,bd=2,relief=RIDGE,bg="papaya whip")
    f1.place(x=0,y=50,width=1400,height=800)
    tc=Label(root,text="CAREER GUIDANCE SYSTEM",font=("Berlin Sans FB Demi",45),fg="white",bg="hotpink4")
    tc.place(x=0,y=0,relwidth=1)
    mpo=Label(f1,text="FILL UP YOUR NECESSARY DETAILS!!!",font=("Berlin Sans FB Demi",24),fg="white",bg="pink2")
    mpo.place(x=0,y=20,relwidth=1)
    h1=Label(f1,text="Name",font=("Times New Roman",25,"bold"),fg="hotpink4",bg="papaya whip")
    h1.place(x=20,y=145)
    i=Entry(f1,font=("Comic Sans MS,",15),textvariable=Name)
    i.place(x=220,y=145,width=350,height=40)
    j=Label(f1,text="D.O.B",font=("Times New Roman",25,"bold"),fg="hotpink4",bg="papaya whip")
    j.place(x=20,y=205)
    tpo=Entry(f1,font=("Comic Sans MS,",15),textvariable=DOB)
    tpo.place(x=220,y=205,width=350,height=40)
    n=Label(f1,text="Age",font=("Times New Roman",25,"bold"),fg="hotpink4",bg="papaya whip")
    n.place(x=20,y=265)
    o=Entry(f1,font=("Comic Sans MS,",15),textvariable=Age)
    o.place(x=220,y=265,width=350,height=40)
    r=Label(f1,text="Contact",font=("Times New Roman",25,"bold"),fg="hotpink4",bg="papaya whip")
    r.place(x=20,y=325)
    s=Entry(f1,font=("Comic Sans MS,",15),textvariable=Contact)
    s.place(x=220,y=325,width=350,height=40)
    t=Label(f1,text="Email Id",font=("Times New Roman",25,"bold"),fg="hotpink4",bg="papaya whip")
    t.place(x=20,y=385)
    u=Entry(f1,font=("Comic Sans MS,",15),textvariable=Email)
    u.place(x=220,y=385,width=350,height=40)
    bs=Button(f1,text="SAVE",font=("Times New Roman",20),command=op,bg="hotpink4",fg="white")
    bs.place(x=880,y=530,width=150,height=50)
    bs=Button(f1,text="BACK",font=("Times New Roman",20),command=f1.destroy,bg="hotpink4",fg="white")
    bs.place(x=30,y=530,width=150,height=50)
register()
#############delete###########
def delete1():
    f1=Frame(root,bd=2,relief=RIDGE,bg="light cyan")
    f1.place(x=0,y=50,width=1400,height=800)
    tc=Label(root,text="CAREER GUIDANCE SYSTEM",font=("Berlin Sans FB Demi",45),fg="black",bg="hotpink4")
    tc.place(x=0,y=0,relwidth=1)
    delt=Label(f1,text="Delete Record!!!",font=("Berlin Sans FB Demi",24),fg="black",bg="dodgerblue2")
    delt.place(x=0,y=20,relwidth=1)
    cur.execute("use bhaviii2")
    def delete2():
        cur.execute('''select * from puff;''')
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    f1=Frame(root,bd=5)
    f1.place(x=5,y=120,width=1350,height=575)
    Table=ttk.Treeview(f1,columns=('Name','D.O.B','Age','Contact','Email'))
    def d_get(ev):
        f=Table.selection()
        Table.delete(f)
    Table.heading('Name',text="Name")
    Table.heading('D.O.B',text="D.O.B")
    Table.heading('Age',text="Age")
    Table.heading('Contact',text="Contact")
    Table.heading('Email',text="Email")
    Table["show"]="headings"
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",d_get)
    delete2()
delete1()
def mainscreen():
    f1=Frame(root,bd=2,relief=RIDGE,bg="light cyan")
    f1.place(x=0,y=50,width=1400,height=800)
    tc=Label(root,text="CAREER GUIDANCE SYSTEM",font=("Berlin Sans FB Demi",45),fg="black",bg="hotpink4")
    tc.place(x=0,y=0,relwidth=1)
    bs=Button(f1,text="Enter Record",font=("Times New Roman",35),command=register,bg="darkslategray4",fg="floralwhite")
    bs.place(x=500,y=80,width=300,height=80)
    bs=Button(f1,text="Delete Record",font=("Times New Roman",35),command=delete1,bg="darkslategray4",fg="white")
    bs.place(x=500,y=230,width=300,height=80)
mainscreen()
def Btech():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from Science where Courses='B.E/B.Tech';''')
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=sci,fg="white", bg="black")
    back2.place(x=600,  y=489)
    def e_get(ev):
        a=" >Engineer \n >Information Technology Engineer \n >Database Manager Developer \n >Technical Assistant"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Bachelor of Technology and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Bachelor of Engineering / Technology", font= ("Arial Rounded MT Bold",22),fg="Red",bg="white")
    e.place(x=15, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=15, y=300)
    e= Label(Table,text=" >Engineer \n >Information Technology Engineer \n >Database Manager Developer \n >Technical Assistant", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )
def MBBS():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from Science where Courses='MBBS';''')
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=sci,fg="white", bg="black")
    back2.place(x=580,  y=450)
    def e_get(ev):
        a=" >Doctor \n >Medical Advisor \n >General Physician \n >Pediatric Doctor \n >Surgeon"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Bachelor of Medicine & Bachelor of Surgery and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    scrollx.pack(side=TOP,fill=X)
    e= Label(Table,text="Bachelor of Medicine & Bachelor of Surgery", font= ("Arial Rounded MT Bold",22),fg="Red",bg="white")
    e.place(x=15, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=15, y=300)
    e= Label(Table,text=" >Doctor \n >Medical Advisor \n >General Physician \n >Pediatric Doctor \n >Surgeon", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )
def BAM():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from Science where Courses='Bachelor of Pharmacy';''')
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=sci,fg="white", bg="black")
    back2.place(x=580,  y=450)
    def e_get(ev):
        a=" >Pharmacist \n >Medical Representative \n >Clinical Research Associate \n >Pharmacy Manager"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Bachelor of Pharmacy and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Bachelor of Pharmacy", font= ("Arial Rounded MT Bold",22),fg="Red",bg="white")
    e.place(x=20, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=15, y=300)
    e= Label(Table,text=" >Pharmacist \n >Medical Representative \n >Clinical Research Associate \n >Pharmacy Manager", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )
def BOM():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from Science where Courses='Bachelor of Homeopathic Medicine & Surgery';''')
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=sci,fg="white", bg="black")
    back2.place(x=580,  y=450)
    def e_get(ev):
        a=" >Public Health Specialist \n >Doctor \n >Pharmacist \n >Consultant \n >Medical Assistant \n >Spa Director"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Bachelor of Homeopathic Medicine & Surgery and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Bachelor of Homeopathic Medicine & Surgery", font= ("Arial Rounded MT Bold",22),fg="Red",bg="white")
    e.place(x=15, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=15, y=300)
    e= Label(Table,text=" >Public Health Specialist \n >Doctor \n >Pharmacist \n >Consultant \n >Medical Assistant \n >Spa Director", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )
def BON():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from Science where Courses='Bachelor of Science in Nursing';''')
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=sci,fg="white", bg="black")
    back2.place(x=580, y=450)
    def e_get(ev):
        a=" >Nurse \n >Assistant Nurse \n >Nursing/Psychiatric Tutor \n >Dean of Nursing \n >Health Service manager"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Bachelor of Science in Nursing and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Bachelor of Science in Nursing", font= ("Arial Rounded MT Bold",22),fg="Red",bg="white")
    e.place(x=15, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=15, y=300)
    e= Label(Table,text=" >Nurse \n >Assistant Nurse \n >Nursing/Psychiatric Tutor \n >Dean of Nursing \n >Health Service manager", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get)
def bscit1():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from Science where Courses='Bachelor of Science in Information Technology';''')
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=sci,fg="white", bg="black")
    back2.place(x=580, y=450)
    def e_get(ev):
        a=" >Application Programmer \n >Graphic Designer \n >Information Technologist \n >Database Administrator \n >Systems Manager \n >Hardware & Network Expert"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Bachelor of Science in Information Technology and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Bachelor of Science in Information Technology", font= ("Arial Rounded MT Bold",22),fg="Red",bg="white")
    e.place(x=15, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=15, y=300)
    e= Label(Table,text=" >Application Programmer \n >Graphic Designer \n >Information Technologist \n >Database Administrator \n >Systems Manager \n >Hardware & Network Expert", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )
def sci():
    sc=Frame(root,bd=5, relief=RIDGE)
    sc.place(x=0, y=75, width=1365, height= 700)
    bot=Button(sc, text= "Bachelor of Medicine & Bachelor of Surgery",font= ("Arial Rounded MT Bold",20),fg="pink", bg="slategrey",command=MBBS)
    bot.place(x=10, y=40,width=620, height=50)
    bscit=Button(sc, text= "Bachelor of Engineering / Technology",font= ("Arial Rounded MT Bold",20),fg="pink", bg="slategrey",command=Btech)
    bscit.place(x=10, y=100,width=620, height=50)
    bsc=Button(sc, text= "Bachelor of Pharmacy",font= ("Arial Rounded MT Bold",20),fg="pink", bg="slategrey",command=BAM)
    bsc.place(x=10, y=160,width=620, height=50)
    mbbs=Button(sc, text= "Bachelor of Homeopathic Medicine & Surgery",font= ("Arial Rounded MT Bold",20),fg="pink", bg="slategrey",command=BOM)
    mbbs.place(x=10, y=220,width=620, height=50)
    bp=Button(sc, text= "Bachelor of Science in Nursing",font= ("Arial Rounded MT Bold",20),fg="pink", bg="slategrey",command=BON)
    bp.place(x=10, y=280,width=620, height=50)
    bscit2=Button(sc, text= "Bachelor of Science in Information Technology",font= ("Arial Rounded MT Bold",20),fg="pink", bg="slategrey",command=bscit1)
    bscit2.place(x=10, y=340,width=620, height=50)
    optp=Button(sc, text= "BACK",font= ("Arial Rounded MT Bold",20),fg="white", bg="hotpink4",command=main)
    optp.place(x=10, y=520,height=50)
def BachelorofCommerce():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from commerce where Courses='Bachelor of Commerce';''')
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=com,fg="white", bg="black")
    back2.place(x=580,  y=450)
    def e_get(ev):
        a=" >Banking \n >Business Analyst \n >Accountant \n >Financial Risk Manager"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Bachelor of Commerce and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Bachelor of Commerce", font= ("Arial Rounded MT Bold",22),fg="Red",bg="white")
    e.place(x=15, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=15, y=300)
    e= Label(Table,text=" >Banking \n >Business Analyst \n >Accountant \n >Financial Risk Manager", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )
def BachelorofBusinessAdministration():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from commerce where Courses='Bachelor of Business Administration';''')
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=com,fg="white", bg="black")
    back2.place(x=580,  y=450)
    def e_get(ev):
        a=" >Human Resource \n >Real Estate Business \n >Sales Executive \n >Digital Marketer \n >Product Manager"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Bachelor of Business Administration and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Bachelor of Business Administration", font= ("Arial Rounded MT Bold",22),fg="Red",bg="white")
    e.place(x=15, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=15, y=300)
    e= Label(Table,text=" >Human Resource \n >Real Estate Business \n >Sales Executive \n >Digital Marketer \n >Product Manager", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )
def CharteredAccountancy():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from commerce where Courses='Chartered Accountancy';''')
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=com,fg="white", bg="black")
    back2.place(x=580,  y=450)
    def e_get(ev):
        a=" >Internal Auditor \n >Forensic Auditing \n >Taxation Advisory \n >Finance Manager"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Chartered Accountancy and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Chartered Accountancy", font= ("Arial Rounded MT Bold",22),fg="Red",bg="white")
    e.place(x=15, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=15, y=300)
    e= Label(Table,text=" >Internal Auditor \n >Forensic Auditing \n >Taxation Advisory \n >Finance Manager", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )
def CompanySecretary():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from commerce where Courses='Company Secretary';''')
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=com,fg="white", bg="black")
    back2.place(x=580,  y=450)
    def e_get(ev):
        a=" >Chief Administrative Officer \n >Legal Advisor \n >Corporate Policy Maker \n >Corporate Planner \n >Pricipal Secretary"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Company Secretary and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Company Secretary", font= ("Arial Rounded MT Bold",22),fg="Red",bg="white")
    e.place(x=15, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=15, y=300)
    e= Label(Table,text=" >Chief Administrative Officer \n >Legal Advisor \n >Corporate Policy Maker \n >Corporate Planner \n >Pricipal Secretary", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.column("Sr_No",width=150)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )
def BachelorsofLaw():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from commerce where Courses='Bachelors of Law (LLB)';''')
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=com,fg="white", bg="black")
    back2.place(x=580,  y=450)
    def e_get(ev):
        a=" >Legal Advisor \n >Public Prosecutor \n >Law Reporter \n >Legal Manager \n >Corporate Lawyer \n >Legal Service Chief"
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Bachelor of Law and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Bachelors of Law", font= ("Arial Rounded MT Bold",22),fg="Red",bg="white")
    e.place(x=15, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=15, y=300)
    e= Label(Table,text=" >Legal Advisor \n >Public Prosecutor \n >Law Reporter \n >Legal Manager \n >Corporate Lawyer \n >Legal Service Chief", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )
def CostManagementAccountant():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from commerce where Courses='Cost & Management Accountant';''')
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=com,fg="white", bg="black")
    back2.place(x=580,  y=450)
    def e_get(ev):
        a=" >Finance Manager\n >Accounts Manager\n >Treasury & Payroll Manager\n >Financial Analyst\n >Chief Financial Analyst"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Cost & Management Accountant and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Cost & Management Accountant", font= ("Arial Rounded MT Bold",22),fg="Red",bg="white")
    e.place(x=15, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=15, y=300)
    e= Label(Table,text=" >Finance Manager\n >Accounts Manager\n >Treasury & Payroll Manager\n >Financial Analyst\n >Chief Financial Analyst", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )
def CertifiedFinancialPlanner():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from commerce where Courses='Certified Financial Planner';''')
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=com,fg="white", bg="black")
    back2.place(x=580,  y=450)
    def e_get(ev):
        a=" >Tax Consultancy \n >Self Employment \n >Investment Advisor \n >Financial Planner \n >Columnist"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Certified Financial Planner and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Certified Financial Planner", font= ("Arial Rounded MT Bold",22),fg="Red",bg="white")
    e.place(x=15, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=15, y=300)
    e= Label(Table,text=" >Tax Consultancy \n >Self Employment \n >Investment Advisor \n >Financial Planner \n >Columnist", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )
def BachelorsinComputerApplication():   
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from commerce where Courses='Bachelors in Computer Application';''')
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=com,fg="white", bg="black")
    back2.place(x=580,  y=450)
    def e_get(ev):
        a=" >Business Analyst \n >App Developer \n >Computer Programmer \n >Auditor \n >Business Consultant"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Bachelors in Computer Application and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Bachelors in Computer Application", font= ("Arial Rounded MT Bold",22),fg="Red",bg="white")
    e.place(x=15, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=15, y=300)
    e= Label(Table,text=" >Business Analyst \n >App Developer \n >Computer Programmer \n >Auditor \n >Business Consultant", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )
def com():
    cm=Frame(root,bd=5, relief=RIDGE)
    cm.place(x=0, y=75, width=1365, height= 700)
    boc=Button(cm, text= "Bachelor of Commerce",font= ("Arial Rounded MT Bold",20),fg="light blue", bg="royalblue4",command=BachelorofCommerce)
    boc.place(x=10, y=40,width=500, height=50)
    ca=Button(cm, text= "Chartered Accountancy",font= ("Arial Rounded MT Bold",20),fg="light blue", bg="royalblue4",command=CharteredAccountancy)
    ca.place(x=10, y=100,width=500, height=50)
    cma=Button(cm, text= "Cost & Management Accountant",font= ("Arial Rounded MT Bold",20),fg="light blue", bg="royalblue4",command=CostManagementAccountant)
    cma.place(x=10, y=160,width=500, height=50)
    bba=Button(cm, text= "Bachelors of Business Administration",font= ("Arial Rounded MT Bold",20),fg="light blue", bg="royalblue4",command=BachelorofBusinessAdministration)
    bba.place(x=10, y=220,width=500, height=50)
    cs=Button(cm, text= "Company Secretary",font= ("Arial Rounded MT Bold",20),fg="light blue", bg="royalblue4",command=CompanySecretary)
    cs.place(x=10, y=280,width=500, height=50)
    boe=Button(cm, text= "Bachelors of Law (LLB)",font= ("Arial Rounded MT Bold",20),fg="light blue", bg="royalblue4",command=BachelorsofLaw)
    boe.place(x=10, y=340,width=500, height=50)
    toe=Button(cm, text= "Certified Financial Planner",font= ("Arial Rounded MT Bold",20),fg="light blue", bg="royalblue4",command=CertifiedFinancialPlanner)
    toe.place(x=10, y=400,width=500, height=50)
    soe=Button(cm, text= "Bachelors in Computer Application",font= ("Arial Rounded MT Bold",20),fg="light blue", bg="royalblue4",command=BachelorsinComputerApplication)
    soe.place(x=10, y=460,width=500, height=50)
    optp=Button(cm, text= "BACK",font= ("Arial Rounded MT Bold",20),fg="white", bg="hotpink4",command=main)
    optp.place(x=50, y=510)
def boa2():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from arts where Courses='Bachelor of Arts';''')
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    global f1
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=arts,fg="white", bg="hotpink4")
    back2.place(x=580,  y=450)
    def e_get(ev):
        a=" >Content Writer \n >Administrative Assistant \n >Linguist \n >Social Worker \n >Journalist \n >Archeologist"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Bachelor of Arts and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Bachelor of Arts", font= ("Arial Rounded MT Bold",20),fg="Red",bg="white")
    e.place(x=15, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=15, y=300)
    e= Label(Table,text=" >Content Writer \n >Administrative Assistant \n >Linguist \n >Social Worker \n >Journalist \n >Archeologist", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.column("Sr_No",width=150)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )
def bofa():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from arts where Courses='Bachelor of Fine Arts';''')
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    global f1
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=arts,fg="white", bg="hotpink4")
    back2.place(x=580,  y=450)
    def e_get(ev):
        a=" >Art Teacher \n >Creative Director \n >Fine Artist \n >Designer \n >Cartoonist \n >Photographer"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Bachelor of Fine arts and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Bachelor of Fine Arts", font= ("Arial Rounded MT Bold",20),fg="red",bg="white")
    e.place(x=20, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=20, y=300)
    e= Label(Table,text=" >Art Teacher \n >Creative Director \n >Fine Artist \n >Designer \n >Cartoonist \n >Photographer", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.column("Sr_No",width=150)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )
def boe():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from arts where Courses='Bachelor of Education';''')
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    global f1
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=arts,fg="white", bg="hotpink4")
    back2.place(x=580,  y=450)
    def e_get(ev):
        a=" >School Teacher \n >Content Writer \n >Private Tutor \n >Education Consultant \n >Principal \n >Counselor"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Bachelor of Education and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Bachelor of Education", font= ("Arial Rounded MT Bold",20),fg="red",bg="white")
    e.place(x=15, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=20, y=300)
    e= Label(Table,text=" >School Teacher \n >Content Writer \n >Private Tutor \n >Education Consultant \n >Principal \n >Counselor", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.column("Sr_No",width=150)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )
def bomc():
    cur.execute("use bhaviii2")
    def b():
        cur.execute('''select Sr_No,College,City,State,Duration from arts where Courses='Journalism & Mass Communication';''')
        rows=cur.fetchall()
        for row in rows:
            print(row)
            Table.insert('',END,values=row)
    global f1
    f1=Frame(root,bd=5)
    f1.place(x=640,y=100,width=700,height=575)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)
    Table=ttk.Treeview(f1,columns=('Sr_No','College','City','State','Duration'),xscrollcommand=scrollx.set)
    back2=Button(Table, text= "Back",font= ("Arial Rounded MT Bold",15),command=arts,fg="white", bg="hotpink4")
    back2.place(x=580,  y=450)
    def e_get(ev):
        a=" >Correspondent \n >Social Media Marketing \n >Media Planner \n >Event Manager \n >Journalist \n >Email Marketing"
        f=Table.selection()
        for i in f:
            row=Table.item(i,'values')
        ll=Name.get()
        print(row)
        otp=f"Hello {ll}\nYou have selected Journalism & Mass Communication and here is the information available about your selected course\n\nCollege Name:{row[1]}\nCity:{row[2]}\nState:{row[3]}\nDuration:{row[4]}\nCareer paths \n{a}"
        k=Email.get()
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("careerguidance2608@gmail.com", "rqjwkgzdsplqrepd")
        emailid = k
        s.sendmail('&&&&&&&&&&&',emailid,msg)
    e= Label(Table,text="Journalism & Mass Communication", font= ("Arial Rounded MT Bold",22),fg="Red",bg="white")
    e.place(x=15, y=250)
    e= Label(Table,text="Career Paths...", font= ("Arial Rounded MT Bold",22),fg="blue",bg="white")
    e.place(x=15, y=300)
    e= Label(Table,text=" >Correspondent \n >Social Media Marketing \n >Media Planner \n >Event Manager \n >Journalist \n >Email Marketing", font= ("Arial Rounded MT Bold",17),fg="black",bg="white",justify=LEFT)
    e.place(x=20, y=350)
    scrollx.pack(side=TOP,fill=X)
    scrollx.config(command=Table.xview)
    Table.heading('Sr_No',text="Sr_No")
    Table.heading('College',text="College")
    Table.heading('City',text="City")
    Table.heading('State',text="State")
    Table.heading('Duration',text="Duration")
    Table["show"]="headings"
    b()
    Table.column("College",width=400)
    Table.pack(fill=BOTH,expand=1)
    Table.column("Sr_No",width=150)
    Table.pack(fill=BOTH,expand=1)
    Table.bind("<ButtonRelease-1>",e_get )
def arts():
    global ar
    ar=Frame(root,bd=5, relief=RIDGE)
    ar.place(x=0, y=75, width=1365, height= 700)
    boa=Button(ar, text= "Bachelor of Arts",font= ("Arial Rounded MT Bold",20),fg="rosybrown1", bg="rosybrown4",command=boa2)
    boa.place(x=10, y=40,width=470, height=50)
    bofa2=Button(ar, text= "Bachelor of Fine Arts",font= ("Arial Rounded MT Bold",20),fg="rosybrown1", bg="rosybrown4",command=bofa)
    bofa2.place(x=10, y=100,width=470, height=50)
    bhm=Button(ar, text= "Bachelor of Education",font= ("Arial Rounded MT Bold",20),fg="rosybrown1", bg="rosybrown4",command=boe)
    bhm.place(x=10, y=160,width=470, height=50)
    bfd=Button(ar, text= "Journalism & Mass Communication",font= ("Arial Rounded MT Bold",20),fg="rosybrown1", bg="rosybrown4",command=bomc)
    bfd.place(x=10, y=220,width=470, height=50)
    optp=Button(ar, text= "BACK",font= ("Arial Rounded MT Bold",20),fg="white", bg="hotpink4",command=main)
    optp.place(x=50, y=340)
def kl():
  def llll():
    global score
    if (score>10 and score<=20):
      yy.showinfo("Results","You Eligible for Science")
      sci()
    elif(score>=1 and score<=5):
      yy.showinfo("Results","You Eligible for Arts")
      arts()
    elif(score>5 or score<=10):
      yy.showinfo("Results","You Eligible for Commerce")
      com()
  global score
  ggggggg=fifthscore.get()
  if(ggggggg==1):
    score=score+2
  elif(ggggggg==2):
    score=score+1
  elif(ggggggg==3):
    score=score+3
  else:
    pass
  print(score)
  llll()
def question5():
    def prvs():
        ssssss.destroy()
        global score
        ggg=fourthscore.get()
        if(ggg==1):
            score=score-2
        elif(ggg==2):
            score=score-1
        elif(ggg==3):
            score=score-3
    global score
    ggg=fourthscore.get()
    if(ggg==1):
        score=score+2
    elif(ggg==2):
        score=score+1
    elif(ggg==3):
        score=score+3
    else:
        pass
    print(score)
    ssssss=Frame(root,bd=5, relief=RIDGE)
    ssssss.place(x=0, y=75, width=1365, height= 700)
    tttttt= Label(ssssss,text="How do you help the economy?", font= ("Arial Rounded MT Bold",20), anchor="c")
    tttttt.place(x=160, y=25)
    uuuuuu=Radiobutton(ssssss,text="Helps in growth of industrial development",font= ("Arial Rounded MT Bold",20),variable=fifthscore, value=1)
    uuuuuu.place(x=160, y=70)
    vvvvvv=Radiobutton(ssssss,text="Raises people’s productivity & creativity",font= ("Arial Rounded MT Bold",20),variable=fifthscore, value=2)
    vvvvvv.place(x=160, y=120)
    wwwwww=Radiobutton(ssssss,text="Creation of new inventions & technology",font= ("Arial Rounded MT Bold",20),variable=fifthscore, value=3)
    wwwwww.place(x=160, y=170)
    yyyyyy=Button(ssssss, text= "Next",font= ("Arial Rounded MT Bold",25),fg="white", bg="hotpink4",command=kl)
    yyyyyy.place(x=900, y=400)
    pvsqn=Button(ssssss, text= "Previous Question",font= ("Arial Rounded MT Bold",25),fg="white", bg="hotpink4",command=prvs)
    pvsqn.place(x=200, y=400)
def question4():
    def prvs():
        ss.destroy()
        global score
        gg=thirdscore.get()
        if(gg==1):
            score=score-2
        elif(gg==2):
            score=score-3
        elif(gg==3):
            score=score-1
    global score
    gg=thirdscore.get()
    if(gg==1):
        score=score+2
    elif(gg==2):
        score=score+3
    elif(gg==3):
        score=score+1
    else:
        pass
    print(score)
    ss=Frame(root,bd=5, relief=RIDGE)
    ss.place(x=0, y=75, width=1365, height= 700)
    tt= Label(ss,text="Do you enjoy helping others or prefer to empower them to do things themselves?", font= ("Arial Rounded MT Bold",20), anchor="c")
    tt.place(x=160, y=25)
    uu=Radiobutton(ss,text="Empower to do things themselves",font= ("Arial Rounded MT Bold",20),variable=fourthscore, value=1)
    uu.place(x=160, y=70)
    vv=Radiobutton(ss,text="Helping others",font= ("Arial Rounded MT Bold",20),variable=fourthscore, value=2)
    vv.place(x=160, y=120)
    ww=Radiobutton(ss,text="Depends on the situation",font= ("Arial Rounded MT Bold",20),variable=fourthscore, value=3)
    ww.place(x=160, y=170)
    yy=Button(ss, text= "Next",font= ("Arial Rounded MT Bold",25),fg="white", bg="hotpink4",command=question5)
    yy.place(x=900, y=400)
    pvsqn=Button(ss, text= "Previous Question",font= ("Arial Rounded MT Bold",25),fg="white", bg="hotpink4",command=prvs)
    pvsqn.place(x=200, y=400)
def question3():
  def prvs():
      s.destroy()
      global score
      gh=secondscore.get()
      if (gh==1):
        score=score-1
      elif(gh==2):
        score=score-2
      elif(gh==3):
        score=score-3
  global score
  gh=secondscore.get()
  if (gh==1):
    score=score+1
  elif(gh==2):
    score=score+2
  elif(gh==3):
    score=score+3
  else:
    pass
  print(score)
  s=Frame(root,bd=5, relief=RIDGE)
  s.place(x=0, y=75, width=1365, height= 700)
  t= Label(s,text="Which of the following statement you find more intresting?", font= ("Arial Rounded MT Bold",20), anchor="c")
  t.place(x=160, y=25)
  u=Radiobutton(s,text="Higher the risk, Higher will be the profit",font= ("Arial Rounded MT Bold",20),variable=thirdscore, value=1)
  u.place(x=160, y=70)
  vet=Radiobutton(s,text="Experimental & theoretical explanation of natural phenomenon",font= ("Arial Rounded MT Bold",20),variable=thirdscore, value=2)
  vet.place(x=160, y=120)
  wet=Radiobutton(s,text="Creative activity that expresses imaginative skill",font= ("Arial Rounded MT Bold",20),variable=thirdscore, value=3)
  wet.place(x=160, y=170)
  yet=Button(s, text= "Next",font= ("Arial Rounded MT Bold",25),fg="white", bg="hotpink4",command=question4)
  yet.place(x=900, y=400)
  pvsqn=Button(s, text= "Previous Question",font= ("Arial Rounded MT Bold",25),fg="white", bg="hotpink4",command=prvs)
  pvsqn.place(x=200, y=400)
def question2():
  def prvs():
      global score
      p=firstscore.get()
      sssss.destroy()
      if (p==1):
        score=score-1 #option a
      elif(p==2):
        score=score-2 #option b
      elif(p==3):
        score=score-3 #option c
      elif(p==4):
        score=score-3 #option d
  global score
  p=firstscore.get()
  if p==0:
      yy.showerror("Error","Enter a option")
      question
  elif (p==1):
    score=score+1 #option a
  elif(p==2):
    score=score+2 #option b
  elif(p==3):
    score=score+3 #option c
  elif(p==4):
    score=score+3 #option d
  else:
    pass
  sssss=Frame(root,bd=5, relief=RIDGE)
  sssss.place(x=0, y=75, width=1365, height= 700)
  ttttt= Label(sssss,text="What qualities from the following do you acquire?", font= ("Arial Rounded MT Bold",20), anchor="c")
  ttttt.place(x=160, y=25)
  uuuuu=Radiobutton(sssss,text="Good imagination & Communication skills",font= ("Arial Rounded MT Bold",20),variable=secondscore, value=1)
  uuuuu.place(x=160, y=70)
  vvvvv=Radiobutton(sssss,text="Good at calculations & planning",font= ("Arial Rounded MT Bold",20),variable=secondscore, value=2)
  vvvvv.place(x=160, y=120)
  wwwww=Radiobutton(sssss,text="Good at knowledge & technology",font= ("Arial Rounded MT Bold",20),variable=secondscore, value=3)
  wwwww.place(x=160, y=170)
  yyyyy=Button(sssss, text= "Next",font= ("Arial Rounded MT Bold",25),fg="white", bg="hotpink4",command=question3)
  yyyyy.place(x=900, y=400)
  pvsqn=Button(sssss, text= "Previous Question",font= ("Arial Rounded MT Bold",25),fg="white", bg="hotpink4",command=prvs)
  pvsqn.place(x=200, y=400)
def question1():
  ef=Frame(root,bd=5, relief=RIDGE)
  ef.place(x=0, y=75, width=1365, height= 700)
  e= Label(ef,text="What subject are you intrested in?", font= ("Arial Rounded MT Bold",20), anchor="c")
  e.place(x=160, y=25)
  v=Radiobutton(ef,text="Literature",font= ("Arial Rounded MT Bold",20), variable=firstscore, value=1)
  v.place(x=160, y=70)
  w=Radiobutton(ef,text="Economics",font= ("Arial Rounded MT Bold",20), variable=firstscore, value=2)
  w.place(x=160, y=120)
  y=Radiobutton(ef,text="Maths",font= ("Arial Rounded MT Bold",20), variable=firstscore, value=3)
  y.place(x=160, y=170)
  z=Radiobutton(ef,text="Biology",font= ("Arial Rounded MT Bold",20), variable=firstscore, value=4)
  z.place(x=160, y=220)
  d=Button(ef, text= "Next",font= ("Arial Rounded MT Bold",25),fg="white", bg="hotpink4", command=question2)
  d.place(x=900, y=400)
  bck=Button(ef,text="BACK",font=("Arial Rounded MT Bold",25),command=ef.destroy,bg="hotpink4",fg="white")
  bck.place(x=100,y=400,width=150,height=70)
print(score)




def certi1():
    cur.execute ("use bhaviii2")
    cur.execute("create table if not exists Investment_Banking_Course(Sr_No int,  College varchar(100), City varchar(100),State varchar(100),Duration varchar(100))")
    cur.execute("delete from Investment_Banking_Course")
    cur.execute("insert into Investment_Banking_Course values(1, 'Gujarat University', 'Ahmedabad', 'Gujarat','2 Years')")
    cur.execute("insert into Investment_Banking_Course values(2, 'Delhi University', 'New Delhi', 'Delhi NCR','2 Years')")
    cur.execute("insert into Investment_Banking_Course values(3, 'Parul University', 'Vadodara', 'Gujarat','2 Years')")
    cur.execute("insert into Investment_Banking_Course values(4, 'Symbiosis Institute of Business Management', 'Pune', 'Maharashtra','2 Years')")
    cur.execute("insert into Investment_Banking_Course values(5, 'Xavier Institute of Management & Research', 'Mumbai', 'Maharashtra','2 Years')")
    cur.execute("insert into Investment_Banking_Course values(6, 'Christ University', 'Bangalore', 'Karnataka','2 Years')")
    cur.execute("insert into Investment_Banking_Course values(7, 'JECRC University', 'Jaipur', 'Rajasthan','2 Years')")
    cur.execute("insert into Investment_Banking_Course values(8, 'NMIMS Deemed-to-be University', 'Bangalore', 'Karnataka','2 Years')")
    cur.execute("insert into Investment_Banking_Course values(9, 'University of Madras', 'Chennai', 'Tamil Nadu','2 Years')")
    cur.execute("insert into Investment_Banking_Course values(10, 'National Institute of Technology', 'Calicut', 'Kerala','2 Years')")
    link.commit()
certi1()


def certi2():
    cur.execute ("use bhaviii2")
    cur.execute("create table if not exists Diploma_in_Hotel_Management(Sr_No int, College varchar(100), City varchar(100),State varchar(100),Duration varchar(100))")
    cur.execute("delete from Diploma_in_Hotel_Management")
    cur.execute("insert into Diploma_in_Hotel_Management values(1, 'Asia Pacific Institute of Hotel Management', 'Ahmedabad', 'Gujarat','3 Years')")
    cur.execute("insert into Diploma_in_Hotel_Management values(2, 'Oberoi Centre of Learning and Development', 'New Delhi', 'Delhi NCR','3 Years')")
    cur.execute("insert into Diploma_in_Hotel_Management values(3, 'Institute of Hotel Management Catering Technology & Applied Nutrition', 'Ahmedabad', 'Gujarat','3 Years')")
    cur.execute("insert into Diploma_in_Hotel_Management values(4, 'Institute of Hotel Management (IHM)', 'Mumbai', 'Maharashtra','3 Years')")
    cur.execute("insert into Diploma_in_Hotel_Management values(5, 'Hotel & Catering Management Institute', 'Chandigarh', 'Punjab','3 Years')")
    cur.execute("insert into Diploma_in_Hotel_Management values(6, 'SRM Institute of Hotel Management', 'Chennai', 'Tamil Nadu','3 Years')")
    cur.execute("insert into Diploma_in_Hotel_Management values(7, 'Institute of Hotel Management', 'Bhopal', 'Madhya Pradesh','3 Years')")
    cur.execute("insert into Diploma_in_Hotel_Management values(8, 'Institute of Advanced Management', 'Kolkata', 'West Bengal','3 Years')")
    cur.execute("insert into Diploma_in_Hotel_Management values(9, 'State Institute of Hotel Management', 'Udaipur', 'Rajasthan ','3 Years')")
    cur.execute("insert into Diploma_in_Hotel_Management values(10, 'Amrapali Institute of Hotel Management', 'Calicut', 'Kerala','3 Years')")
    link.commit()
certi2()


def certi3():
    cur.execute ("use bhaviii2")
    cur.execute("create table if not exists Diploma_in_Engineering (Sr_No int,College varchar(100), City varchar(100),State varchar(100),Duration varchar(100))")
    cur.execute("delete from Diploma_in_Engineering")
    cur.execute("insert into Diploma_in_Engineering values(1, 'The Maharaja Sayajirao University of Baroda', 'Vadodara', 'Gujarat','4 Years')")
    cur.execute("insert into Diploma_in_Engineering values(2, 'Jamia Millia Islamia', 'New Delhi', 'Delhi NCR','4 Years')")
    cur.execute("insert into Diploma_in_Engineering values(4, 'Government Polytechnic', 'Mumbai', 'Maharashtra','4 Years')")
    cur.execute("insert into Diploma_in_Engineering values(5, 'Chandigarh College of Engineering & Technology', 'Chandigarh', 'Punjab','4 Years')")
    cur.execute("insert into Diploma_in_Engineering values(6, 'Hindustan Institute of Technology & Science', 'Chennai', 'Tamil Nadu','4 Years')")
    cur.execute("insert into Diploma_in_Engineering values(7, 'Indira Gandhi Iinstitute of Tchnology', 'Sarang', 'Odisha','4 Years')")
    cur.execute("insert into Diploma_in_Engineering values(8, 'GLA University', 'Bharthia', 'Uttar Pradesh','4 Years')")
    cur.execute("insert into Diploma_in_Engineering values(9, 'Jaipur national University', 'Jaipur', 'Rajasthan ','4 Years')")
    cur.execute("insert into Diploma_in_Engineering values(10, 'Carmel Polytechnic College', 'Alapphuzha', 'Kerala','4 Years')")
    link.commit()
certi3()


def certi4():
    cur.execute ("use bhaviii2")
    cur.execute("create table if not exists Diploma_in_Event_Management(Sr_No int, College varchar(100), City varchar(100),State varchar(100),Duration varchar(100))")
    cur.execute("delete from Diploma_in_Event_Management")
    cur.execute("insert into Diploma_in_Event_Management values(1, 'Maharaja Sayajirao University', 'Vadodara', 'Gujarat','1 year')")
    cur.execute("insert into Diploma_in_Event_Management values(2, 'National Academy of Event Management and Development (NAEMD),', 'Mumbai', 'Maharashtra','1 year')")
    cur.execute("insert into Diploma_in_Event_Management values(3, 'National Institute of Event Management (NIEM)', 'New Delhi', 'Delhi NCR','1 year')")
    cur.execute("insert into Diploma_in_Event_Management values(4, 'Amity School of Communication', 'Noida', 'Uttar Pradesh','1 year')")
    cur.execute("insert into Diploma_in_Event_Management values(5, 'EMDI Institute of Media and Communication', 'New Delhi', 'Delhi NCR','1 year')")
    cur.execute("insert into Diploma_in_Event_Management values(6, 'Institute of Mass Communication, Film and Television Studies', 'Kolkata', 'West Bengal','1 year')")
    cur.execute("insert into Diploma_in_Event_Management values(7, 'Indian School of Media (ISM)', 'Mumbai', 'Maharashtra','1 year')")
    cur.execute("insert into Diploma_in_Event_Management values(8, 'National Academy of Media and Events ', 'Kolkata', 'West Bengal','1 year')")
    link.commit()
certi4()

def certi5():
    cur.execute ("use bhaviii2")
    cur.execute("create table if not exists Diploma_in_Animation(Sr_No int, College varchar(100), City varchar(100),State varchar(100),Duration varchar(100))")
    cur.execute("delete from Diploma_in_Animation")
    cur.execute("insert into Diploma_in_Animation values(1, 'National Institute of Design', 'Ahmedabad', 'Gujarat','1 year')")
    cur.execute("insert into Diploma_in_Animation values(2, 'Anibrain School of Media Design', 'Pune', 'Maharashtra','1 year')")
    cur.execute("insert into Diploma_in_Animation values(3, 'RIMT University', 'Jalandhar', 'Punjab','1 year')")
    cur.execute("insert into Diploma_in_Animation values(4, 'Vels University', 'Chennai', 'Tamil Nadu','1 year')")
    cur.execute("insert into Diploma_in_Animation values(5, 'Indus University ', 'Ahmedabad', 'Gujarat','1 year')")
    cur.execute("insert into Diploma_in_Animation values(6, 'Swami Vivekanand University', 'Sagar', 'Madhya Pradesh','1 year')")
    cur.execute("insert into Diploma_in_Animation values(7, 'Singhania University', 'Jhunjhunu', 'Rajasthan ','1 year')")
    cur.execute("insert into Diploma_in_Animation values(8, 'Central Institute of Technology', 'Guwahati', 'Assam','1 year')")
    link.commit()
certi5()


def certi6():
    cur.execute ("use bhaviii2")
    cur.execute("create table if not exists Diploma_in_Business_Management(Sr_No int, College varchar(100), City varchar(100),State varchar(100),Duration varchar(100))")
    cur.execute("delete from Diploma_in_Business_Management")
    cur.execute("insert into Diploma_in_Business_Management values(1, 'Maharaja Sayajirao University', 'Vadodara', 'Gujarat','1 year')")
    cur.execute("insert into Diploma_in_Business_Management values(2, 'Savitribai Phule Pune University', 'Pune', 'Maharashtra','1 year')")
    cur.execute("insert into Diploma_in_Business_Management values(3, 'Lovely Professional University', 'Jalandhar', 'Punjab','1 year')")
    cur.execute("insert into Diploma_in_Business_Management values(4, 'Noida International University', 'Noida', 'Uttar Pradesh','1 year')")
    cur.execute("insert into Diploma_in_Business_Management values(5, 'Dr Babasaheb Ambedkar Open University', 'Ahmedabad', 'Gujarat','1 year')")
    cur.execute("insert into Diploma_in_Business_Management values(6, 'IIMT University', 'Meerut', 'Uttar Pradesh','1 year')")
    cur.execute("insert into Diploma_in_Business_Management values(7, 'Maharaja Agrasen International College', 'Raipur', 'Chhattisgarh','1 year')")
    cur.execute("insert into Diploma_in_Business_Management values(8, 'Krishna Kanta Handiqui State Open University', 'Guwahati', 'Assam','1 year')")
    link.commit()
certi6()


def certi7():
    cur.execute ("use bhaviii2")
    cur.execute("create table if not exists Diploma_in_Information_Technology(Sr_No int, College varchar(100), City varchar(100),State varchar(100),Duration varchar(100))")
    cur.execute("delete from Diploma_in_Information_Technology")
    cur.execute("insert into Diploma_in_Information_Technology values(1, 'Maharaja Sayajirao University of Baroda', 'Vadodara', 'Gujarat','6-12months')")
    cur.execute("insert into Diploma_in_Information_Technology values(2, 'Dr S and SS Ghandhi College of Engineering and Technology,', 'Surat', 'Gujarat','6-12months')")
    cur.execute("insert into Diploma_in_Information_Technology values(3, 'Ambedkar Institute of Technology', 'New Delhi', 'Delhi NCR','6-12months')")
    cur.execute("insert into Diploma_in_Information_Technology values(4, 'RC Technical Institute', 'Ahmedabad', 'Gujarat','6-12months')")
    cur.execute("insert into Diploma_in_Information_Technology values(5, 'PSG Polytechnic College', 'Coimbatore', 'Tamil Nadu','6-12months')")
    cur.execute("insert into Diploma_in_Information_Technology values(6, 'Government Polytechnic', 'Pune','Maharashtra','6-12months')")
    cur.execute("insert into Diploma_in_Information_Technology values(7, 'Shri Bhagubhai Mafatlal Polytechnic', 'Mumbai', 'Maharashtra','6-12months')")
    cur.execute("insert into Diploma_in_Information_Technology values(8, 'NIMS University', 'Jaipur', 'Rajasthan','6-12months')")
    link.commit()
certi7()

root.mainloop()
