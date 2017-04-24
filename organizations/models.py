# _*_ encording:utf-8 _*_
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseOrg(models.Model):
    name=models.FileField()
    desc=models.TextField()
    click_nums=models.IntegerField()
    fav_nums=models.IntegerField()
    add_time=models.TimeField()
    