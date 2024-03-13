from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.username