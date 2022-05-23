from django.forms import ModelForm
from . models import employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class EmployeeForms(ModelForm):
    class Meta:
        model=employee
        fields='__all__'

# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model=User
#         fields=['username','email','password1','password2']
#

class AdminForms(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password']
