from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
from django.conf import settings

# Create your models here.
class Checklist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.IntegerField(null = True)
    #content = models.TextField()
    #place = models.CharField(max_length=30)
    #stufflist = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    
    menu_name = models.CharField(max_length = 32, default = '')
    cafeteria_name = models.CharField(max_length = 32, default = '')

    taste = models.IntegerField(null = True) 
    quality = models.IntegerField(null = True) 
    cost = models.IntegerField(null = True) 
    clean = models.IntegerField(null = True) 
    quantity = models.IntegerField(null = True) 

class Board(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
  date = models.IntegerField(null=True)
  title = models.CharField(max_length=128, null=True)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

#평점 모델
class Reviewlist(models.Model):
    menu_name = models.CharField(max_length = 32, default = '')
    cafeteria_name = models.CharField(max_length = 32, default = '')

    avg_taste = models.FloatField() 
    avg_quality = models.FloatField() 
    avg_cost = models.FloatField() 
    avg_clean = models.FloatField() 
    avg_quantity = models.FloatField() 

# 가게 테이블
class Restaurant(models.Model):
  eng_name = models.CharField(max_length = 32, default = '')
  kor_name = models.CharField(max_length = 32, default = '')
  location = models.CharField(max_length = 32, default = '')
  phone = models.CharField(max_length = 32, default = '')
  operating_day = models.CharField(max_length = 32, default = '')
  operating_time = models.CharField(max_length = 32, default = '')
  notice_contents = models.CharField(max_length = 32, default = '')
  notice_registered = models.CharField(max_length = 32, default = '')
  lat = models.FloatField(null = True)  
  lng = models.FloatField(null = True) 


# 메뉴테이블
class Menu(models.Model):
  menu_name = models.CharField(max_length = 32, default = '')
  cafeteria = models.CharField(max_length = 32, default = '')
  price = models.IntegerField(null = True)
  type = models.CharField(max_length = 32, default = '')

