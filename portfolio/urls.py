from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home_page, name="Home"),
    path("about/", views.about_page, name="about"),
    path("project/", views.project_page, name="project"),
    path("experience/", views.experience_page, name="experience"),
]
