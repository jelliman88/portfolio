from django.shortcuts import render
from .models import Project


def portfolio(request):
    projects = Project.getProjects()
    return render(request, 'portfolio.html', {'projects': projects})
