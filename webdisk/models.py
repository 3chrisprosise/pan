# _*_ coding: utf-8 _*_
from __future__ import unicode_literals

from django.db import models
import django
import django.utils.timezone as timezone
# Create your models here.

class Files(models.Model):
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(null=False, max_length=100)  #名称描述
    up_date = models.DateField(default=django.utils.timezone.now())
    file_url = models.CharField(null=False, max_length=200)   #文件的存储目录
    file_self = models.FileField(null=False, upload_to='files')  #文件本体
    file_size = models.FloatField(null=False)
    is_use = models.BooleanField(default=True)
    def __unicode__(self):
        return self.file_name
class users(models.Model):
    id =models.AutoField(primary_key=True)
    user_name = models.CharField(unique=True,max_length=20)
    password = models.CharField(null=False,max_length=20)
    is_use = models.BooleanField(default=True)
    def __unicode__(self):
        return self.user_name