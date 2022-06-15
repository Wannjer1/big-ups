from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Profile,Project
from django.http import HttpResponse,Http404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.contrib import messages
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer

# Create your views here.
#home function that displays all posts
def home(request):

    return render(request, 'bigup/index.html')

# profile view function
@login_required
def profile(request):

    return render(request, 'bigup/profile.html')

# update profile function
@login_required
def update_profile(request):
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, ('Profile is updated successfully'))
           
        else:
            messages.error(request,('Unable to complete request'))
            return redirect("profile")
    profile_form = UpdateProfileForm(instance=request.user)


    return render( request=request, template_name='bigup/update_profile.html', context={"user":request.user, "profile_form": profile_form})

# @login_required
# def update_profile(request):
#     profile_form = UpdateProfileForm()
#     if request.method == 'POST':
#         profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

#         if profile_form.is_valid():
#             profile_form.save()
#             messages.success(request, 'Profile is updated successfuly')
#             return redirect (to='profile')
#     else:
#          profile_form = UpdateProfileForm(instance=request.user.profile)
#     #   import the required forms and create instances of those forms depending on whether the request is get or post. 

#     return render(request, 'bigup/update_profile.html', {'profile_form': profile_form})



# signup view function
def signup_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
         
            form.save()
            messages.success(request, "Registration successful." )
            return redirect(reverse("login"))
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegisterForm()
    context={"form":form}
    return render (request, "registration/register.html", context)


# login view function
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            # else:
            #     messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")

    else:
        form = AuthenticationForm()
    return render (request, 'registration/login.html', context={"login_form": form})

def logout(request):
    logout(request)

    return render (request, 'registration/logout.html')



# APIView section
def bigapi(request):
    return render(request,'bigup/api_page.html')

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles =Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self, request, fromat=None):
        all_projects =Project.objects.all()
        serializers =ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)