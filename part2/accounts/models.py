from django.db import models
from django.contrib.auth.models import User  # Correct import

def user_avatar_path(instance, filename):
    ext = filename.split('.')[-1]  # Extract file extension
    return f'avartar/user_{instance.user.id}/avatar.{ext}'

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One user, one profile
    avatar = models.ImageField(upload_to=user_avatar_path, blank=True, null=True)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.user