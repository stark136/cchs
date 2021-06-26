from django.db import models
from django.db.models.fields import DateTimeField
from django.db import models
# Create your models here.
class image(models.Model):
    photo= models.ImageField(upload_to="images")
    # date= models.DateTimeField(auto_now_add=True)
   
class info(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)