# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import re
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User)
    nick = models.CharField(max_length =64)
    photo = models.ImageField(upload_to='user/',null = True)   

    def save(self, *args, **kwargs):
        for field in self._meta.fields:
            if field.name == 'photo':
                field.upload_to = 'photo/%s' % term.replace(' ','')
                super(Profile,self).save(*args, **kwargs)

    def __unicode__(self):
       return self.nick.strip()
 
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

class Contribution(models.Model):
    user = models.ForeignKey(Profile)
    title = models.CharField(max_length = 128)
    description = models.TextField(max_length=450)
    
    def __unicode__(self):
       return self.title.strip()
 
    class Meta:
        verbose_name = 'Contribucion'
        verbose_name_plural = 'Contribuciones'


class Content (models.Model):
    active = models.BooleanField( default = False)
    image_content = models.ImageField(upload_to='content/',null = True)
    link_video =  models.CharField( max_length = 128, null = True, blank = True)
    title = models.CharField( max_length = 64)
    description = models.TextField( max_length = 512)
    important =  models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    def save(self, *args, **kwargs):
        for field in self._meta.fields:
            if field.name == 'image_content':
                field.upload_to = 'content_img/%s' % self.title.replace(' ','')
                super(Content,self).save(*args, **kwargs)

    def __unicode__(self):
       return self.title.strip()
 
    class Meta:
        verbose_name = 'Contenido'
        verbose_name_plural = 'Contenidos'


