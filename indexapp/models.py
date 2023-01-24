from django.db import models

# Create your models here.
class Admin(models.Model):
    Name=models.CharField(max_length=20,null=True,blank=True)
    Mob=models.IntegerField(null=True,blank=True)
    Email_id=models.EmailField(max_length=20,null=True,blank=True)
    Image=models.ImageField(upload_to="profile",null=True,blank=True)
    User=models.CharField(max_length=10,null=True,blank=True)
    Password=models.CharField(max_length=15,null=True,blank=True)
    Confirm=models.CharField(max_length=15,null=True,blank=True)

class Category(models.Model):
    C_Name=models.CharField(max_length=15,null=True,blank=True)
    Description=models.CharField(max_length=30,null=True,blank=True)
    C_Image=models.ImageField(upload_to="profile",null=True,blank=True)

class Products(models.Model):
    P_Name=models.CharField(max_length=15,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Qty=models.IntegerField(null=True,blank=True)
    Descr=models.CharField(max_length=30,null=True,blank=True)
    P_Image=models.ImageField(upload_to="profile",null=True,blank=True)
    Category=models.CharField(max_length=15,null=True,blank=True)

class Contact(models.Model):
    Name=models.CharField(max_length=25,null=True,blank=True)
    Email=models.EmailField(null=True,blank=True)
    Sub=models.CharField(max_length=50,null=True,blank=True)
    Msg=models.CharField(max_length=100,null=True,blank=True)