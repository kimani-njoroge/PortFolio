from django.shortcuts import render
from .models import Project
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')


def index(request):

    projects = Project.get_projects()
    print(projects)
    return render(request, 'index.html',{"projects":projects})


