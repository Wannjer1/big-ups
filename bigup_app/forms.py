
from django import forms
from .models import Profile, Project
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



# signup form
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# update profile form
class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    name = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    email = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
    # class Meta enables us to to create a form based on a model
        model = Profile
        fields = ['avatar', 'bio','name', 'email']

# post project form
class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','email']

    
