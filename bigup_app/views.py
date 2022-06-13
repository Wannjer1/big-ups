from django.shortcuts import render
from django.http import HttpResponse,Http404

# Create your views here.
#home function that displays all posts
def home(request):

    return render(request, 'bigup/index.html')