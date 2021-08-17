from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from . models import User1

class OrderForm(ModelForm):
	class Meta:

		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
  
class CustomerRegistration(forms.ModelForm):
    class Meta:
        model=User1
        fields=['area', 'approch', 'lead']
        widgets={
            'area':forms.TextInput(attrs={'class':'form-control'}),
            'approch':forms.NumberInput(attrs={'class':'form-control'}),
            'lead':forms.NumberInput(attrs={'class':'form-control'}),
            }