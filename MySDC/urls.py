"""MySDC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SDC.urls')),
    # path("courses/",courses,name="courses"),
    # path("campuslife/",campuslife,name="campuslife"),
    # path("departments/",departments,name="departments"),
    # path("alumni/",alumni,name="alumni"),
    # path("admissions/",admissions,name="admissions"),
    # path("faculty/",faculty,name="faculty"),
    # path("slogin/",slogin,name="slogin"),
    # path("hlogin/",hlogin,name="hlogin"),
    # path("tlogin/",tlogin,name="tlogin"),
    # path("plogin/",plogin,name="plogin"),
    # path("stafflogin/",stafflogin,name="stafflogin"),
    # path("forgotpass/",forgotpass,name="forgotpass"),
    # path("student-signin/",studsignin ,name="studsignin"),
    # path("teacher-signin/",tsignin ,name="tsignin"),
    #  path("staff/",staff ,name="staff"),
    # path('stafflogin/staff/',staff ,name="staff"),
]

urlpatterns += static (settings.STATIC_URL,document_root = settings.STATIC_ROOT)
urlpatterns += static (settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)