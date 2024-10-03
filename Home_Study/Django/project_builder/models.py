from django.db import models

class project(models.Model):
    name= models.CharField(max_length=255)
    discription = models.TextField()

class location(models.Model):
    address = models.TextField()
    models.OneToOneField('project',on_delete = models.SET_NULL,related_name='location' )



class Task(models.Model):
    titel = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

class Tag(models.Model):    
    name= models.CharField(max_length=100)