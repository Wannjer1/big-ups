
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from requests import delete

# Create your models here.
class Profile(models.Model):
    avatar = models.ImageField(upload_to='profilepic/', default='default.jpeg')
    user = models.OneToOneField(User,on_delete=models.CASCADE)
# The user field has a OneToOneField that forms a direct connection to a user stored in the database
# on_delete=models.CASCADE argument signifies that a Profile object will be deleted if the referenced User is deleted
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
    link = models.CharField(max_length=200)

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def __str__(self):
        return self.name

# rating model
class Rating(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    design = models.IntegerField(choices=rating, default=0, blank=True)
    usability = models.IntegerField(choices=rating, blank=True)
    content = models.IntegerField(choices=rating, blank=True)
    score = models.FloatField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    post = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings', null=True)
    def save_rating(self):
        self.save()
    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(post_id=id).all()
        return ratings
    def __str__(self):
        return f'{self.post} Rating'
        