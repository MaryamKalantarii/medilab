from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Services (models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_data']

class HealthService(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title



class Skills(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name



class Doctor(models.Model):
    info = models.ForeignKey(User , on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    description = models.TextField()
    image = models.ImageField(upload_to='doctor', default='doctor.jpg')
    twitter = models.CharField(max_length=255, default='#')
    facebook = models.CharField(max_length=255, default='#')
    instagram = models.CharField(max_length=255, default='#')
    linkdin = models.CharField(max_length=255, default='#')
    status = models.BooleanField(default=False)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.info.username