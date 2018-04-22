from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectImage

# Create your views here.


def index(request):
    projects = Project.objects.all()

    return render(request, 'crusp/index.html', context= {'projects': projects})


def portfolio(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project_images = ProjectImage.objects.filter(project=project)
    projects_slider = Project.objects.all()

    return render(request, 'crusp/portfolio.html', context={
        "project": project,
        "project_images": project_images,
        "projects_slider": projects_slider,
    })
