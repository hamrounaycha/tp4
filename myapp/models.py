from django.db import models


# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length = 40)
    email = models.EmailField(max_length = 20)
    section = models.CharField(max_length = 40)
    photo = models.FileField(upload_to='photos')
    photoo = models.FileField(upload_to ='photos')
    
  
    
    