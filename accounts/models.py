from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    Profile_pic = models.ImageField(upload_to='profile_pics',default='default.jpg')
    followers = models.ManyToManyField(User,related_name='followers',blank=True)
    following = models.ManyToManyField(User,related_name='following',blank=True)

    def __str__(self):
        return self.user.username








