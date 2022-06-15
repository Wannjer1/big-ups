
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from requests import delete

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profilepic/', default='default.jpeg')
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,blank=True)
    bio = models.CharField(max_length=500)
    email = models.EmailField(max_length=250)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self, new_bio):
        '''method to update user bio'''
        self.bio = new_bio
        self.save()

    def update_profilepic(self, new_image):
        self.photo = new_image
        self.save()

    def __str__(self):
        return self.name

class Project(models.Model):
    webimage = models.ImageField(upload_to='webimage/',null=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def __str__(self):
        return self.name
        