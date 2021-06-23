from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import FloatField
# Create your models here.

class User(AbstractUser):
    
    username=models.CharField('Alias',max_length=256, blank=True,null=True)
    first_name=models.CharField('Nombre',max_length=256, blank=True, null=True)
    last_name=models.CharField('Apellido',max_length=256, blank=True, null=True)
    email=models.CharField('Correo electronico',max_length=254,blank=True,null=True, unique=True)
    run=models.CharField('Run',max_length=10, blank=True, null=True)
    address=models.CharField('Direccion',max_length=50, blank=True, null=True)
    phone=models.CharField('Telefono',max_length=9,blank=True, null=True)
    birth_day=models.DateField('Fecha de nacimiento',blank=True,null=True)
    movie_preference=models.CharField('Preferencia de peliculas',max_length=30,blank=True,null=True)
    sex=models.CharField('Genero',max_length=10, blank=True, null=True)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name']
    
    def set_phone(self, raw_phone):
        self.phone= raw_phone

class Movie(models.Model):
    user=models.ForeignKey('core.User', on_delete=models.CASCADE)
    id=models.CharField(max_length=10, primary_key=True)
    title=models.CharField(max_length=30)
    release_date=models.DateField()
    runtime=models.CharField(max_length=20)
    imdb_rating=FloatField()
    
    def set_fields(self,user,id,title,release_date,runtime,imdb_rating):
        self.user=user
        self.id=id
        self.title=title
        self.release_date=release_date
        self.runtime=runtime
        self.imdb_rating=imdb_rating