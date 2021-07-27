from django.db import models

class Ipaddress(models.Model):
    ipaddress = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    regionName = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    createDate = models.DateTimeField(auto_now=True)