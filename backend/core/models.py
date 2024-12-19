from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,blank=True)
    content=models.TextField(blank=True)
    created_on=models.DateTimeField(auto_now_add=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.title
    
    