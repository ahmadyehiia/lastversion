from django.contrib import admin
from .models import book #must be added to give access to admin the table

# Register your models here.

admin.site.register(book) #must be added to give admin access for this table 