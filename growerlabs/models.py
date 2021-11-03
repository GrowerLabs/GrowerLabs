from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import *

# Create your models here.
class Skill(models.Model):
    skill = models.CharField(max_length=100)
    def __str__(self):
        return self.skill

class Profile(models.Model):
    name = models.CharField(max_length=300)
    role = models.CharField(max_length=300)
    bio = models.TextField(blank=True, null=True)
    dp = models.ImageField(upload_to = 'dp', null= True)
    prof_user = models.ForeignKey(User, on_delete=models.CASCADE)
    github_link = models.URLField(null= True, blank=True)
    portfolio_link = models.URLField(null= True, blank=True)
    insta_link = models.URLField(null= True, blank=True)
    linkedin_link = models.URLField(null= True, blank=True)
    skills = models.ManyToManyField(Skill, related_name="skills")
    def __str__(self):
        return str(self.prof_user.username) + " " + str(self.name) + " " + str(self.role)   

class Project(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to = 'project', null= True)
    project_github_link = models.URLField(null= True)
    website_link = models.URLField(null= True)
    contributors = models.ManyToManyField(Profile, related_name="contributors")
    def __str__(self):
        return str(self.title)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(prof_user=instance)

post_save.connect(create_user_profile, sender=User)  
