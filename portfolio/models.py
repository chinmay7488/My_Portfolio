from django.db import models


# Create your models here.
class HomePage_model(models.Model):
    Job_titles = models.JSONField()
    Sub_heading_into = models.CharField(max_length=500)
    profile_pic = models.FileField(upload_to='ProfilePhoto/')


class general_info_model(models.Model):
    phone_number = models.IntegerField(max_length=10)
    website_title = models.CharField(max_length=100)
    site_title = models.CharField(max_length=100)
    facebook_url = models.CharField(max_length=500, null=True)
    instagram_url = models.CharField(max_length=500, null=True)
    twitter_url = models.CharField(max_length=500, null=True)
    github_url = models.CharField(max_length=500, null=True)
    linkedin_url = models.CharField(max_length=500, null=True)
    resume_url = models.CharField(max_length=500)


class Certificate_model(models.Model):
    Certi_Title = models.CharField(max_length=150)
    Certi_Duration = models.CharField(max_length=150)
    Certi_Institution = models.CharField(max_length=150)


class Education_model(models.Model):
    Title = models.CharField(max_length=150)
    Duration = models.CharField(max_length=150)
    Institution = models.CharField(max_length=150)


class Skill_model(models.Model):
    Title = models.CharField(max_length=150)
    Icon = models.FileField(upload_to='Skill/')
    ToShow = models.BooleanField(default=False)


class Project_model(models.Model):
    Title = models.CharField(max_length=150)
    Description = models.TextField()
    Video_link = models.FileField(upload_to='Skill/')
    Skills_learned = models.JSONField()
    GitHub_link = models.CharField(max_length=150, null=True)
    Visit_link = models.CharField(max_length=150, null=True)


class Experience_model(models.Model):
    Title = models.CharField(max_length=150)
    Duration = models.CharField(max_length=150)
    Description = models.TextField()
