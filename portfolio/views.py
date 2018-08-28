from django.shortcuts import render
from .models import Project
from django.http import HttpResponse
# Create your views here.
def index(request):

    projects = Project.get_projects()
    print(projects)
    return render(request, 'index.html',{"projects":projects})


