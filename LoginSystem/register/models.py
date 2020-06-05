from django.db import models

# Create your models here.

class UserDetail(models.Model):
    first_name=models.CharField(max_length=30)
    middle_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    course=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    phone=models.CharField(max_length=15)
    address=models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    class Meta:
        db_table='UserDetail'
