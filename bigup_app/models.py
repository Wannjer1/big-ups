from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profilepic/', default='default.jpeg')
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50,blank=True)
    bio = models.CharField(max_length=500)
    email = models.EmailField(max_length=250)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update_profile()

    def __str__(self):
        return self.name