"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf.urls import include, url
from app.views import *

urlpatterns = [
    #auth
    path('registration/signup',views.signup,name="signup"),
    path('registration/login',views.login,name="login"),
    path('registration/logout',views.logout,name="logout"),

    # #social login
    # path('accounts/',include('allauth.urls')),
    
    path('admin/', admin.site.urls),
	# 아래 코드르 추가해준다.
	path('', index, name='index'),
    
    #alumni
    path('alumni/',views.alumni,name="alumni"),

    #session
    path('session/',views.session,name="session"),
    path('session/<int:post_pk>',views.session_detail,name="session_detail"),
    path('session_new/',views.session_new,name="session_new"),

    #assignment
    path('assignment/',views.assignment,name="assignment"),

    #contact
    path('contact/',views.contact,name="contact"),

    #study
    path('study/',views.study,name="study"),
    path('study/<int:post_pk>',views.study_detail,name="study_detail"),  
    path('study_new/',views.study_new,name="study_new"),  
    

    path('my/',views.my,name="my"),
    #path('delete/<int:post_pk>',views.delete,name="delete"),
    #path('edit/<int:post_pk>',views.edit,name="edit"),
    #path('delete_comment/<int:post_pk>/<int:comment_pk>',views.delete_comment,name="delete_comment")
]
