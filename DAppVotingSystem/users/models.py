from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser

# Create your models here.
class BoothManager(AbstractUser):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50,unique=True)
    phone_no = models.CharField(max_length=200)
    aadhaar_no = models.CharField(unique=True,max_length=50)
    constituency_id = models.ForeignKey("constituency",on_delete=models.DO_NOTHING)

