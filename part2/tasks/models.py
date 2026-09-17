from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    onwer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task" ,verbose_name="Tasks")
    title = models.CharField(max_length=254)
    done = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['done', '-create_at']
        
    def __str__(self):
        return self.title 