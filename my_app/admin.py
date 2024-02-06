from django.contrib import admin

#import the model
from .models import LongToShort

# Register your models here.
admin.site.register(LongToShort)

#whenever we do changes in model we have to run 2 commds
#python manage.py makemigrations
#python manage.py migrate