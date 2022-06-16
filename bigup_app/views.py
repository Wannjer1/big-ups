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
    projects =  Project.objects.all()

    return render(request, 'bigup/index.html',{'projects':projects})

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

# new project view function
@login_required(login_url='login')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')

    else:
        form = NewProjectForm()
    return render (request, 'bigup/project.html', {'form': form, 'current_user': current_user})

# sear project view function
@login_required(login_url='login')
def search_project(request):
    if "project" in request.GET and request.GET["project"]:
        search_term=request.GET.get("project")
        searched_projects=Project.search_by_name(search_term)
        message = f"{search_term}"

        return render(request,'bigup/search.html',{"message":message, "projects":searched_projects, "project":search_term})
    
    else:
        message = "Please enter search name"

        return render(request, 'bigup/search.html',{"message":message})
    



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
@login_required(login_url='login')
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