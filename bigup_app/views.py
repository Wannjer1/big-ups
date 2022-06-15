from django.shortcuts import render,redirect
from .models import Profile,Project
from django.http import HttpResponse,Http404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer

# Create your views here.
#home function that displays all posts
def home(request):

    return render(request, 'bigup/index.html')

# signup view function
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.objects.create_user(username=username, email=email,password=password1)
        user.save()
        profile=Profile.objects.create(user=user,email=user.email)

        return redirect('login')
    else:
        return render(request,'registration/register.html')