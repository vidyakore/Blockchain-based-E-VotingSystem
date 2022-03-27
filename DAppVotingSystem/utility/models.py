from django.db import models

# Create your models here.
class AddContractManager(models.Model):

    ContractManagerId = models.IntegerField(primary_key=True)
    ContractManagerName = models.CharField(max_length=100)
    ContractManagerEmail = models.EmailField(max_length=50)
    ContractManagerPhoneNo = models.CharField(max_length=12)
    ContractManager_ConstituencyId = models.CharField(max_length=50)
    ContractManagerPassword = models.CharField(max_length=50)


