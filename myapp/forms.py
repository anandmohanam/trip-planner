from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, TextInput,EmailInput,PasswordInput



class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}),
    )
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username': TextInput(attrs={'class':'form-control'}),
            'email': EmailInput(attrs={'class':'form-control'}),

        }




class contactus(forms.Form):
    fullname = forms.CharField(max_length=100)
    Email=forms.CharField(max_length=20)
    msg=forms.CharField(max_length=100)


