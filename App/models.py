from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Budget(models.Model):
    date = models.DateField()
    day = models.TextField(max_length=50)
    category = models.TextField(max_length=255)
    quantity = models.IntegerField(default=0)
    amount= models.FloatField()
    description = models.TextField(max_length=255, blank=True)
    status = models.CharField(default="completed", max_length=100)
    
    
    
    
class Expense(models.Model):
    day = models.CharField(default=timezone.now(), max_length=100)
    date = models.DateField()
    category = models.CharField(max_length=255, blank=True)
    quantity = models.IntegerField(default=0)
    amount= models.FloatField()
    description = models.TextField(max_length=255, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
        
class register(models.Model):
     username= models.CharField(max_length=50) 
     email = models.EmailField(max_length=50) 
     password= models.CharField(max_length=20)
      
    
class employee(models.Model):
    name = models.CharField(max_length=20)
    email= models.EmailField(max_length=30)
    role = models.TextField(max_length=200)
    phone = models.IntegerField()
    address = models.TextField(max_length=300)
    salary = models.DecimalField(max_digits=12, decimal_places=6)
        

class Sales(models.Model):
    name = models.CharField(max_length=100)
    day = models.CharField(max_length=80, default=timezone.now())
    date = models.DateField()
    quantity = models.IntegerField()
    category = models.TextField(max_length=100)
    pay_method = models.TextField(default='cash',   max_length=100)
    amount = models.FloatField()
    description = models.TextField(max_length= 300)
    image = models.ImageField(upload_to='images/', null=True)
    
    
    
            
class slides(models.Model):
    image = models.ImageField(upload_to="images/", null=True)                                
       