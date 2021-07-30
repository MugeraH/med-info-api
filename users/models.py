from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField  

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    username = models.CharField(max_length=250, unique=True)
    firstname = models.CharField(max_length=255,null=True)
    lastname = models.CharField(max_length=255,null=True)
    profile_picture = models.URLField(null=True)
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = []
    
    @classmethod
    def filter_user_by_id(cls, id):
        user = User.objects.filter(id = id).first()
        return user
    
    def __str__(self):
        return self.username
