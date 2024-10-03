from django.db import models

class project(models.Model):
    name= models.CharField(max_length=255)
    discription = models.TextField()

class location(models.Model):
    address = models.TextField()
    null=True,
    blank = True ,
    project = models.OneToOneField('project',
    on_delete = models.SET_NULL,related_name='location'
  
    )



class Task(models.Model):
    titel = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    project = models.ForeignKey('project',
    on_delete =models.CASCADE,related_name='task')

class Tag(models.Model):    
    name= models.CharField(max_length=100)
    projects =models.models.ManyToManyField('project',
    related_name='tags')