"""Empmgmt URL Configuration

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

from django.urls import path,include
from .views import home,slider,Employee,list,deleteemployee,updateemployee,addemployee,register

urlpatterns = [

    path('',home),
    path('slides',slider),
    path('employee',Employee),
    path('list',list),
    path('delete-employee/<str:id>',deleteemployee),
    path('update-employee/<str:id>',updateemployee),
    path('add-employee',addemployee),
    path('register',register)

]
