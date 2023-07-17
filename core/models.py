from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.
class mainpost(models.Model):
    title=models.CharField(max_length=100)
    lessdiscription=models.TextField()
    publishdate=models.DateField()
    btnlink=models.CharField(max_length=30)


        
    


