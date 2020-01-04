from django.db import models

# Create your models here.
class Identification(models.Model):
    # Creating the models for the user in the data base by taking the below creditionals
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100,blank=True,null=True)
    lastname = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(max_length=254,blank=True,null=True)
   
