from django.shortcuts import render
from .models import Projects, Skills


# Create your views here.

def home(request):
    projects = Projects.objects.all()
    skills = Skills.objects.all()
    return render(request,'home.html',{'projects':projects, 'skills':skills})