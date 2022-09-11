# Provide the ability to register the user as an administrator or as an ordinary user (guest)
# Provide the ability to log in (guest)
# Provide the ability to Log out (authorized user)
from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser,  ROLE_CHOICES


# class UserLoginFormEmail(AuthenticationForm):
class UserLoginFormEmail(forms.Form):
    email = forms.EmailField(label='User Name', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='User Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# class AuthenticateUserForm(forms.Form):
class AuthenticateUserForm(forms.ModelForm):
#     username = forms.CharField(label='User Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     first_name = forms.CharField(label='User Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     middle_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     password2 = forms.CharField(label='Пароль ще раз', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    role = forms.ChoiceField(widget=forms.RadioSelect(), choices=ROLE_CHOICES)
    class Meta:
        model = CustomUser
        # fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'role')
        fields = ('first_name', 'last_name', 'middle_name','email', 'password', 'role')
        # fields = '__all__'
        widgets = {
            'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'role' : forms.RadioSelect(),
        }