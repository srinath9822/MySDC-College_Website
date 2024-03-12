from unicodedata import name
from xml.etree.ElementInclude import include
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home ,name="home"),
    path('courses/', views.courses, name="courses"),
    path('campuslife/', views.campuslife, name="campuslife"),
    path('departments/', views.departments, name="departments"),
    path('alumni/', views.alumni, name="alumini"),
    path('admissions/', views.admissions, name="admissions"),
    path('faculty/', views.faculty, name="faculty"),
    path('slogin/', views.slogin, name="slogin"),
    path('tlogin/', views.tlogin, name="tlogin"),
    path('hlogin/', views.hlogin, name="hlogin"),
    path('stafflogin/', views.stafflogin, name="stafflogin"),
    path('plogin/', views.plogin, name="plogin"),
    path('forgotpass/', views.forgotpass, name="forgotpass"),
    path('student-signin/', views.ssignin, name="ssignin"),
    path('teacher-signin/', views.tsignin, name="tsignin"),
    path('staff/', views.staff, name="staff"),
    path('addteacher/', views.addteacher, name="addteacher"),
    path('addstudent/', views.addstudent, name="addstudent"),
    path('removestudent/', views.removestudent, name="removestudent"),
    path('removeteacher/', views.removeteacher, name="removeteacher"),
    path('studentslist/', views.stud, name="stud"),
    path('assignt/', views.assignt, name="assignt"),
    path('assignteach/', views.assignteacher, name="assignteach"),
    path('feedback/', views.feedback, name="feedback"),
    # path('viewfeedback/',views.viewfeedback,name="viewfeedback")
    # path('signout/', views.signout, name="signout"),
    # path('staffsignup/', views.staffsignup, name="staffsignup"),
]