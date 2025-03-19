from django.db import models
from django.shortcuts import redirect, render


# Create your models here.

class table(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    date = models.DateField()
    people = models.IntegerField()
    time = models.TimeField()
    message = models.TextField()

    def __str__(self):
        return self.name

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


