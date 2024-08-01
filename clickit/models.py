from django.db import models

# Create your models here.
class Cam(models.Model):
    #id will be given by ORM
    camera = models.CharField(max_length=30)
    lens = models.CharField(max_length=30)
    price = models.IntegerField()
