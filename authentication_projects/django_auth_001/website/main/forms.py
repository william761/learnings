from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import Post 


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    First_Name = forms.CharField(required=True, max_length=15)
    Last_Name = forms.CharField(required=True, max_length=20)

    class Meta:
        model = User
        fields = ["username", "First_Name", "Last_Name", "email", "password1", "password2"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]