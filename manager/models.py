from django.db import models

# Create your models here.

class landingpagecontent(models.Model):
    img = models.ImageField(upload_to="upload/", verbose_name='')
    imageheading = models.CharField(max_length=50)
    imagedex = models.TextField()
    
class brandpagecontent(models.Model):
    brandimg = models.ImageField(upload_to="upload/", verbose_name='')
    brandname = models.CharField(max_length=20)
    
