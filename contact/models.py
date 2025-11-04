from django.db import models
from django.utils import timezone
# Create your models here.

# id (primary key - automático criado pelo django)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)
# category (foreign key), show (boolean), picture (imagem)

#Depois
#owner (foreign key)


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True) #blank da opicional no cadastro 
    created_date = models.DateTimeField(default=timezone.now)
    descripicion = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    def __str__(self):
        return f'{self.first_name} {self.last_name}'