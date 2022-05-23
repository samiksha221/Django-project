from django.shortcuts import render,redirect
from .models import employee
from .forms import EmployeeForms,AdminForms
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    return render(request,'home.html')

def slider(request):
    return render(request,'slider.html')

def Employee(request):
    form=EmployeeForms
    if request.method=='POST':
        emp_form= EmployeeForms(request.POST)
        if emp_form.is_valid():
            emp_form.save()
            return redirect('/employee')

    return render(request,'employee.html',{'form':form})

def list(request):
    data=employee.objects.all()
    return render(request,'employeelist.html',{'data':data})

def deleteemployee(request,id):
    name=employee.objects.get(id=id)
    name.delete()
    return redirect('/list')

def updateemployee(request,id):
    name=employee.objects.get(id=id)
    form=EmployeeForms(instance=name)
    if request.method == 'POST':
        saveform=EmployeeForms(request.POST or None,instance=name)
        if saveform.is_valid():
            saveform.save()
            return redirect('/list')
    return render(request,'updateemployee.html',{'form':form})


def addemployee(request):
    form=EmployeeForms
    if request.method=='POST':
        saveform=EmployeeForms(request.POST)
        if saveform.is_valid():
            saveform.save()
            return redirect('/list')
    return render(request,'addemployee.html',{'form':form})

# def login(request):
#     return render(request,'admin/login.html')

# def registerpage(request):
#     form=CreateUserForm
#     if request.method=='POST':
#         reg_form=CreateUserForm(request.POST)
#         if reg_form.is_valid():
#             reg_form.save()
#
#
#     return render(request,'admin/register.html',{'form':form})

def register(request):
    form=AdminForms
    if request.method=='POST':
        admin_form= AdminForms(request.POST)
        if admin_form.is_valid():
            admin_form.save()
            return redirect('/register')
    else:
        form=AdminForms

    return render(request,'registration/adminregister.html',{'form':form})


