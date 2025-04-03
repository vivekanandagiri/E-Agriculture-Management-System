from cProfile import Profile
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    mobile=models.CharField(max_length=20)
    otp=models.CharField(max_length=6,null=True,blank=True)
    uid=models.CharField(default=f'{uuid.uuid4}',max_length=200)
    
    def __str__(self): 
        return f'Profile : {self.user.username} '
