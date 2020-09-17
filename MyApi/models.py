from django.db import models

class MyFile(models.Model):
    image = models.ImageField()


class MyFile_new(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=200)   





## pip install pillow
## Top Connect this with DataBase we need 2 Com..


#1 . python manage.py makemigrations MyApi
#2. python manage.py migrate