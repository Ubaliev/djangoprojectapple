from django.db import models

class Iphone(models.Model):
    name = models.CharField(max_length=127)
    version = models.CharField(max_length=127)
    gb = models.CharField(max_length=127)
    color = models.CharField(max_length=127)
    year = models.CharField(max_length=127)

    
class Macbook(models.Model):
    name = models.CharField(max_length=127)
    version = models.CharField(max_length=127)
    gb = models.CharField(max_length=127)
    year = models.CharField(max_length=127)

class Airpods(models.Model):
    name = models.CharField(max_length=127)
    version = models.CharField(max_length=127)
    color = models.CharField(max_length=127)
    year = models.CharField(max_length=127)
