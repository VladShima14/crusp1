from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectImage
from .form import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

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


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            ae = "{},\n {},\n {}\n".format(message, email, name)

            recepients = ['yourmail@gmail.com']

            try:
                send_mail(name, ae, 'yourmail@gmail.com', recepients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        form = ContactForm()
