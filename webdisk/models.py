from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone
# Create your models here.

class Files(models.Model):
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(null=False,max_length=100)
    up_date = models.DateField(default=timezone.now())
    file_url = models.CharField(null=False,max_length=200)
    file_self = models.FileField(null=False,upload_to='files')
    is_use = models.BooleanField(default=True)

class users(models.Model):
    id =models.AutoField(primary_key=True)
    user_name = models.CharField(unique=True,max_length=20)
    password = models.CharField(null=False,max_length=20)
    is_use = models.BooleanField(default=True)