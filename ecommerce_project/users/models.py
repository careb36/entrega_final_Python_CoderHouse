from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    name= models.CharField(max_length=40)
    surname= models.CharField(max_length=40 )
    birth_date= models.DateField()
    address= models.CharField(max_length=40 )

    def __str__(self):
        return self.user.username
    
    #avatar = models.ImageField(default='default.jpg', upload_to='profile_images')

# creo una clase para implementar los roles de admin y de usuario final para visualizar el CRUD

'''
class User(AbstractUser):
    ADMINISTRATOR = 1
    FINALUSER = 2
    ROLE_CHOICES = (ADMINISTRATOR, 'administrator', FINALUSER, 'finaluser')
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
'''
