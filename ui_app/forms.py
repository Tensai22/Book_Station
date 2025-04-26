from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Book

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class": "form-control"}))
    avatar = forms.ImageField(required=True)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2", "avatar"]

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "description", "cover"]