from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, "home.html")


def about_page(request):
    return render(request, "about.html")


def project_page(request):
    return render(request, "projects.html")


def experience_page(request):
    return render(request, "experience.html")
