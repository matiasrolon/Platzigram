
""" Post models"""
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """ Post model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Si ya tengo importado el User, puedo usarlo para hacer referencia al profile.
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Return title and username"""
        return '{} by @{}'.format(self.title, self.user.username)




# Primer forma de crear el modelo.
""""
class User(models.Model):
    #User model

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField()

    birthdate = models.DateField(blank=True, null=True) #Aclaramos que puede ser null
    # guarda la hora tambien
    created = models.DateTimeField(auto_now_add=True)   # Guarda automaticamente la fecha de alta
    modified = models.DateTimeField(auto_now=True)      # Guarda automaticamente la ultima fecha de modificacion

    #Sobreescribo este metodo para que imprima esto por defecto cuando hago un print del objeto por consola
    def __str__(self):
        #Return email
        return self.email
    
"""