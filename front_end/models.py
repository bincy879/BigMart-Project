from django.db import models

# Create your models here.
class registration_db(models.Model):
    Username=models.CharField(max_length=20,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=15,null=True,blank=True)
    C_password=models.CharField(max_length=15,null=True,blank=True)