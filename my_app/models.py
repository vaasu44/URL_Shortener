from django.db import models

# Create your models here.
class LongToShort(models.Model):#must specify models.Model
    long_url=models.URLField(max_length=250)#its only for url
    short_url=models.CharField(max_length=50,unique=True)#its only for string
    date=models.DateField(auto_now_add=True)
    clicks=models.IntegerField(default=0)

