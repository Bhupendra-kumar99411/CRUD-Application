from django.db import models

# Create your models here.

class Student(models.Model):
    Firstname = models.CharField(max_length=122)
    Lastname = models.CharField(max_length=122)
    Email = models.EmailField(max_length=50)
    Contact = models.BigIntegerField()

    
