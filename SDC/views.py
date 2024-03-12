from asyncio.windows_events import NULL
from pickle import TRUE
from tkinter.tix import FileSelectBox
from django.http import HttpResponse
from django.shortcuts import redirect, render
# from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.template import context
from mysqlx import Row
# from django.contrib.auth import authenticate, login, logout
from .models import ourteachers,registeredteacher, registeredstudent,student,subjects,assignteach,feedback
import mysql.connector as sql

sid=''
pwd=''
tchid=''
tnm=''
tmail=''
t1=''
t2=''
t3=''
t4=''
t5=''
t6=''
t7=''
z1=''
z2=''

# from .models import User
# Create your views here.
def home(request):
    return render(request, "index.html")

def addteacher(request):
    global tchid,tnm,tmail
    tch=ourteachers.objects.all()
    if request.method == "POST":
        m=sql.connect(host="localhost", user="root",password="9620413809",database='SDC')
        csor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key == "tid":
                tchid=value
            if key=="tname":
                tnm=value
            if key=="temail":
                tmail=value

        a="select * from ourteachers where tid='{}'".format(tchid)
        csor.execute(a)
        t=tuple(csor.fetchall())
        if t==():
            c="insert into ourteachers Values( '{}','{}','{}')".format(tchid,tnm,tmail)
            csor.execute(c)
            m.commit()
            messages.success(request, "Added successfully")
        else:
            messages.error(request, "Teacher Id already added")
        
    return render(request,"addteacher.html",{'tch':tch})
                


def courses(request):
    return render(request, "courses.html")

def campuslife(request):
    return render(request, "campuslife.html")

def departments(request):
    return render(request, "departments.html")

def alumni(request):
    return render(request, "alumni.html")

def admissions(request):
    return render(request, "admissions.html")



def slogin(request):
    return render(request, "slogin.html")

def ssignin(request):
    return render(request, "studsignin.html")

def tlogin(request):
    return render(request, "tlogin.html")

def plogin(request):
    return render(request, "plogin.html")

def staff(request):
    return render(request, "staff.html")


def forgotpass(request):
    return render(request, "forgotpass.html")

def studsignin(request):
    return render(request, "studsignin.html")

def tsignin(request):
    return render(request, "teachsignin.html")




def stafflogin(request):
    global sid,pwd
    if request.method == "POST":
        m=sql.connect(host="localhost", user="root",password="9620413809",database='SDC')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key == "userid":
                sid=value
            if key=="password":
                pwd=value


        c="select * from stafflogin where staffid='{}' and staffpassword='{}'".format(sid,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            messages.error(request,"Invalid credentials")
        else:
            messages.success(request, "Login Successful..")
            return render(request, 'staff.html')

    return render(request, "stafflogin.html")



def stud(request):
    stuid=student.objects.all()
    return render(request, "studentlist.html",{'stuid':stuid})
    

def tsignin(request):
    global t1,t2,t3,t4,t5,t6,t7
    if request.method == "POST":
        m=sql.connect(host="localhost", user="root",password="9620413809",database='SDC')
        csor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key == "tuserid":
                t1=value
            if key=="temail":
                t2=value
            if key=="tfname":
                t3=value
            if key=="tlname":
                t4=value
            if key=="tnum":
                t5=value
            if key=="tpass":
                t6=value
            if key=="tpass1":
                t7=value

        if t6 == t7:      
            a1="select * from ourteachers where tid='{}'".format(t1)
            csor.execute(a1)
            t=tuple(csor.fetchall())
            if t!=():
                b="select * from registeredteacher where tid='{}'".format(t1)
                csor.execute(b)
                k=tuple(csor.fetchall())
                if k==():
                    c="insert into registeredteacher Values( '{}','{}','{}','{}','{}','{}')".format(t1,t2,t3,t4,t5,t7)
                    csor.execute(c)
                    m.commit()
                    messages.success(request, "Added successfully")
                else:
                    messages.error(request, "You are already registered")                
            else:
                messages.error(request, "Teacher Id not exits")               
        else:
            messages.error(request, "Password mismatch")

                
    return render(request,"teachsignin.html")

# def staffpassrset(request):
#     try:
#         if request.method == 'POST':
#             staffid = request.POST.get('userid')
# return NULL


s1=''
s2=''
s3=''
def addstudent(request):
    global s1,s2,s3
    stuid=student.objects.all()
    if request.method == "POST":
        m=sql.connect(host="localhost", user="root",password="9620413809",database='SDC')
        csor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key == "studid":
                s1=value
            if key=="studname":
                s2=value
            if key=="studemail":
                s3=value

        a="select * from student where studentid='{}'".format(s1)
        csor.execute(a)
        t=tuple(csor.fetchall())
        if t==():
            c="insert into student Values( '{}','{}','{}')".format(s1,s2,s3)
            csor.execute(c)
            m.commit()
            messages.success(request, "Added successfully")
        else:
            messages.error(request, "Student Id already added")
        
    return render(request,"addstudent.html",{'stuid':stuid})
a1=''
a2=''
a3=''
a4=''
a5=''
a6=''
a7=''
def ssignin(request):
    global a1,a2,a3,a4,a5,a6,a7
    if request.method == "POST":
        m=sql.connect(host="localhost", user="root",password="9620413809",database='SDC')
        csor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key == "studid":
                a1=value
            if key=="studmail":
                a2=value
            if key=="studname":
                a3=value
            if key=="studsem":
                a4=value
            if key=="studsec":
                a5=value
            if key=="studpass":
                a6=value
            if key=="studpass1":
                a7=value

        if a6 == a7:      
            e="select * from student where studentid='{}'".format(a1)
            csor.execute(e)
            t=tuple(csor.fetchall())
            if t!=():
                b="select * from registeredstudent where studentid='{}'".format(a1)
                csor.execute(b)
                k=tuple(csor.fetchall())
                if k==():
                    c="insert into registeredstudent Values( '{}','{}','{}','{}','{}','{}')".format(a1,a2,a3,a4,a5,a7)
                    csor.execute(c)
                    m.commit()
                    messages.success(request, "Added successfully")
                    return redirect("/slogin/")
                else:
                    messages.error(request, "You are already registered")                
            else:
                messages.error(request, "Student Id not exits")               
        else:
            messages.error(request, "Password mismatch")

                
    return render(request,"studsignin.html")



def removeteacher(request):
    global tchid
    tch=ourteachers.objects.all()
    if request.method == "POST":
        m=sql.connect(host="localhost", user="root",password="9620413809",database='SDC')
        csor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key == "tid":
                tchid=value

        a="select * from ourteachers where tid='{}'".format(tchid)
        csor.execute(a)
        t=tuple(csor.fetchall())
        if t!=():
            c="delete from ourteachers where tid='{}'".format(tchid)
            csor.execute(c)
            m.commit()
            messages.success(request, "Removed successfully")
        else:
            messages.error(request, "Teacher does not exits")
        
    return render(request,"removeteacher.html",{'tch':tch})

def removestudent(request):
    global s1
    stuid=student.objects.all()
    if request.method == "POST":
        m=sql.connect(host="localhost", user="root",password="9620413809",database='SDC')
        csor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key == "studid":
                s1=value

        a="select * from student where studentid='{}'".format(s1)
        csor.execute(a)
        t=tuple(csor.fetchall())
        if t!=():
            c="delete from student where studentid='{}'".format(s1)
            csor.execute(c)
            m.commit()
            messages.success(request, "Removed successfully")
        else:
            messages.error(request, "Student does not exit")
        
    return render(request,"removestudent.html",{'stuid':stuid})
hid=''
hpass=''
def hlogin(request):
    global hid,hpass
    if request.method == "POST":
        m=sql.connect(host="localhost", user="root",password="9620413809",database='SDC')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key == "hid":
                hid=value
            if key=="pass":
                hpass=value


        c="select * from hod where hodid='{}' and pass='{}'".format(hid,hpass)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            messages.error(request,"Invalid credentials")
        else:
            messages.success(request, "Login Successful..")
            return render(request, 'hod.html')

    return render(request, "hlogin.html")

def faculty(request):
    tch=ourteachers.objects.all()
    return render(request, "faculty.html",{'tch':tch})

def assignt(request):
    tea=ourteachers.objects.all()
    semes=subjects.objects.all()
    assigntable=assignteach.objects.all()
    return render(request,"assign.html",{'semes':semes,'tea':tea,'assigntable':assigntable})



def assignteacher(request):
    global a1,a2,a3,a4,a5
    if request.method == "POST":
        m=sql.connect(host="localhost", user="root",password="9620413809",database='SDC')
        csor=m.cursor()
        d=request.POST
        
        for key,value in d.items():
            if key == "semester":
                a1=value
            if key=="section":
                a2=value
            if key=="subjectname":
                a3=value
            if key=="teacher":
                a4=value
            if key == "num":
                a5=value
        e="select * from assignteach where semester='{}' and section='{}' and subjectname='{}'".format(a1,a2,a3)
        csor.execute(e)
        t=tuple(csor.fetchall())
        if t==():
                c="insert into assignteach Values('{}','{}','{}','{}','{}')".format(a5,a1,a2,a3,a4)
                csor.execute(c)
                m.commit()
                messages.success(request, "Assigned successfully")
        else:
                messages.error(request, "Teacher already assigned to section")

    return redirect('/assignt/')

def slogin(request):
    global z1,z2
    if request.method == "POST":
        m=sql.connect(host="localhost", user="root",password="9620413809",database='SDC')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key == "sregnum":
                z1=value
            if key=="spass":
                z2=value


        c="select * from registeredstudent where studentid='{}' and studentpass='{}'".format(z1,z2)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            messages.error(request,"Invalid credentials")
        else:
            messages.success(request, "Login Successful..")
            rs=registeredstudent.objects.filter(studentid=z1)
            for i in rs:
                myteacher=assignteach.objects.filter(semester=i.studentsem , section=i.studentsec)

            return render(request, 'student.html',{'rs':rs,'myteacher':myteacher})

    return render(request, "slogin.html")

def feedback(request):
    global a1,a2,a3,a4,a5,a6,a7
    if request.method == "POST":
        m=sql.connect(host="localhost", user="root",password="9620413809",database='SDC')
        csor=m.cursor()
        d=request.POST
        
        for key,value in d.items():
            if key == "teachername":
                a1=value
            if key=="subject":
                a2=value
            if key=="rating":
                a3=value
            if key=="suggestion":
                a4=value
            if key=="regnum":
                a5=value
            if key=="stusem":
                a6=value
            if key=="stusec":
                a7=value
        e="select * from feedback where regnum='{}' and subjectname='{}'".format(a5,a2)
        csor.execute(e)
        t=tuple(csor.fetchall())
        if t==():
                c="insert into feedback Values('{}','{}','{}','{}','{}','{}','{}')".format(a5,a6,a7,a2,a1,a3,a4)
                csor.execute(c)
                m.commit()
                messages.success(request, "Feedback submitted succesfully")
                rs=registeredstudent.objects.filter(studentid=a5)
                for i in rs:
                    myteacher=assignteach.objects.filter(semester=i.studentsem , section=i.studentsec)
                
                    return render(request,"student.html",{'rs':rs ,'myteacher':myteacher})
        else:
                messages.error(request, "Feedback already submitted")

    return render(request,"student.html")

def tlogin(request):
    global z1,z2
    if request.method == "POST":
        m=sql.connect(host="localhost", user="root",password="9620413809",database='SDC')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key == "tlid":
                z1=value
            if key=="tlpass":
                z2=value
            
    
        c="select * from registeredteacher where tid='{}' and password='{}'".format(z1,z2)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            messages.error(request,"Invalid credentials")
        else:
            messages.success(request, "Login Successful..")
            
            rs=registeredteacher.objects.filter(tid=z1)
            for i in rs:
                myteacher=assignteach.objects.filter(teacher=i.tname)
            myt="ROY SIR"

            g="select * from feedback where teacher='{}'".format(myt)
            cursor.execute(g)
            fbs=tuple(cursor.fetchall())

            return render(request, 'teacher.html',{'rs':rs,'myteacher':myteacher,'fbs':fbs})

    return render(request, "tlogin.html")




def viewfeedback(request):
    
    if request.method == "POST":
        m=sql.connect(host="localhost", user="root",password="9620413809",database='SDC')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key == "tname":
                f1=value
            if key == "fsem":
                f2=value
            if key == "fsec":
                f3=value
            if key == "fsub":
                f4=value
                
        c="select regnum and suggestion from feedback where teacher='{}'  semester='{}' and section='{}' and subjectname='{}'".format(f1,f2,f3,f4)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            messages.error(request,"No feedbacks")
        else:
            return render(request,"teacher.html",{'t':t})