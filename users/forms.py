from django import forms
from .models import Car, Customer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя пользователя'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(render_value=True, attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(render_value=True, attrs={
        'class': 'form-control',
        'placeholder': 'Подтвердите пароль'
    }))
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
class CustomerLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=16,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'
                               }))

    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(render_value=True, attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Ваш пароль'
                               }))
    