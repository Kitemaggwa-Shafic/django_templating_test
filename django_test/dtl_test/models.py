from django.db import models

# Create your models here.

# Creating my students model
class RegisterStudent(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    gender = models.CharField(max_length=15)
    age = models.IntegerField()

    def __str__(self):
        return self.firstname