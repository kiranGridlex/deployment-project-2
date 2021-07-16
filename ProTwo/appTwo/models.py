from django.db import models

# Create your models here.
class User(models.Model):
    f_name = models.CharField(max_length = 128)
    l_name = models.CharField(max_length = 128)
    email = models.EmailField(max_length=264,unique=True)
