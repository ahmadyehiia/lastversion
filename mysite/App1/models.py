from django.db import models

# Create your models here.
# USED FOR DB LINES (SQL LINE -- TABLE DATABASE TABLE)

#WE TYPE TABLE AS A CLASS AND DJANO CONVERTS IT TO TABLES

#IT CREATES ID COLOMN A AS A DEFAULT PRIMARY KEY
#models.models is default function we always use
#book is the class name
#title and rating are the names of columns in the books table
#models.***** are the data types of the columns 


#to add data to tables we can open a interface for admin to add data by adding the following  line to url page
#http://127.0.0.1:8000/admin

#we create user and pass in terminal by typing the line
# python manage.py migrate (to get you to type in the user and password)
#pyhon manage.py make migrations (to create db file)
# then type pyhon manage.py createsuperuser command in termnal (to ask for email and pass)

#i created user and email and pass :
 #user ahmed
# email ahmed@gmail.com
# pass ahmed123




class book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField
    
