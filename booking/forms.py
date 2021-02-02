from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        
        fields = ['username', 'password1', 'password2',]

class extraForm(forms.ModelForm):
    
    class Meta:
        model = Booker
        fields = ['name', 'dob', 'address', 'phone']


        
class trainForm(forms.ModelForm):
    # train_name = 
    class Meta:
        model = Train
        fields = ['train_name','train_number','rows_available']

class passengerForm(forms.ModelForm):
    
    class Meta:
        model = Passengers
        fields = ['p_name', 'age', 'gender', 'seat_number']



