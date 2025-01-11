from django.shortcuts import render
from portfolio.models import HomePage_model


# Create your views here.
def home_page(request):
    # data = HomePage_model.objects.all()
    # # context = {
    # #     'JobSubTitle': data['Sub_heading_into'],
    # #     'facebookurl': data['facebook_url'],
    # #     'instagramurl': data['facebook_url'],
    # #     'linkedinurl': data['facebook_url'],
    # # }
    # print(data)
    return render(request, "home.html")


def about_page(request):
    return render(request, "about.html")


def project_page(request):
    return render(request, "projects.html")


def experience_page(request):
    return render(request, "experience.html")
