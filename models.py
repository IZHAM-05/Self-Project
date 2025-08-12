from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    usertype=models.CharField(max_length=20)

class Teacher(models.Model):
    usrname=models.ForeignKey(User,on_delete=models.CASCADE)
    passd=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    phone=models.IntegerField()
    email=models.EmailField()   
    age=models.PositiveBigIntegerField()
    qualification=models.CharField(max_length=20)
    dep=models.CharField(max_length=20)
    profile_Pic=models.ImageField(upload_to='media',null=True,blank=True)



class NotApproved(models.Model):
    usrname=models.CharField(max_length=20)
    passd=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    phone=models.IntegerField()
    email=models.EmailField()   
    age=models.PositiveBigIntegerField()
    dep=models.CharField(max_length=20)
    profile_Pic=models.ImageField(upload_to='media',null=True,blank=True)

class Student(models.Model):
    usrname=models.ForeignKey(User,on_delete=models.CASCADE)
    passd=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    phone=models.IntegerField()
    email=models.EmailField()   
    age=models.PositiveBigIntegerField()
    dep=models.CharField(max_length=20)  
    profile_Pic=models.ImageField(upload_to='media',null=True,blank=True)  