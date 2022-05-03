from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class election_type(models.Model):
    Id = models.AutoField(primary_key=True)
    type_of_election=models.CharField(max_length=200)

class party(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    symbol = models.ImageField(upload_to='images')

class constituency(models.Model):
    # Id = models.AutoField()
    constituency_id = models.IntegerField(primary_key=True,unique=True)
    name=models.CharField(max_length=200)
    State=models.CharField(max_length=200)
    total_voters=models.IntegerField()

class constituency_type(models.Model):
    Id = models.AutoField(primary_key=True)
    election_type_id=models.ForeignKey("election_type",on_delete=models.DO_NOTHING)
    constituency_id=models.ForeignKey("constituency",on_delete=models.DO_NOTHING)

# class contract_manager(models.Model):
#     Id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=50)
#     phone_no = PhoneNumberField(max_length=13, unique=True)
#     aadhaar_no = models.CharField(unique=True,max_length=50)
#     password = models.CharField(max_length=50)
#     confirm_password = models.CharField(max_length=50)

class contract_manager(BaseUserManager):
    def create_user(self, email, password=None,**other_fields):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            **other_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password,phone_no,aadhar_no,id,**other_fields):

        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_admin', True)


        user = self.create_user(
            email,
            password=password,
            phone_no=phone_no,
            aadhar_no=aadhar_no,
            id=id,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class booth_manager(AbstractBaseUser):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50,unique=True)
    phone_no = PhoneNumberField(max_length=13,unique=True)
    aadhaar_no = models.CharField(unique=True,max_length=50)
    constituency_id = models.ForeignKey("constituency",on_delete=models.DO_NOTHING)

    USERNAME_FIELD = 'email'
    Reqired_FIELDS = ['name','phone_no','aadhaar_no','constituency_id']

class voter(models.Model):
    # Id = models.AutoField()
    voter_id = models.IntegerField(primary_key=True)
    voter_aadhaar_no = models.CharField(unique=True,max_length=50)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField(max_length=200)
    email = models.EmailField(max_length=50, blank=True)
    phone_no = PhoneNumberField(max_length=13,unique=True)
    
class voter_constituency(models.Model):
    Id = models.AutoField(primary_key=True)
    voter_id=models.ForeignKey("voter",on_delete=models.DO_NOTHING)
    loksabha_id=models.IntegerField()
    vidhansabha_id=models.IntegerField()

class candidate(models.Model):
    # index = models.AutoField()
    candidate_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200)
    phone_no=models.IntegerField()
    email= models.EmailField(max_length=200)
    aadhaar_no=models.CharField(unique=True,max_length=50)

class candidate_party(models.Model):
    Id = models.AutoField(primary_key=True)
    candidate_id=models.ForeignKey("candidate",on_delete=models.DO_NOTHING)
    party_id=models.ForeignKey("party",on_delete=models.DO_NOTHING)

class candidate_constituency(models.Model):
    Id = models.AutoField(primary_key=True)
    candidate_id=models.ForeignKey("candidate",on_delete=models.DO_NOTHING)
    constituency_id=models.ForeignKey("constituency",on_delete=models.DO_NOTHING)
    election_type_id=models.ForeignKey("election_type",on_delete=models.DO_NOTHING)

class votes(models.Model):
    Id = models.AutoField(primary_key=True)
    candidate_id=models.ForeignKey("candidate",on_delete=models.DO_NOTHING)
    total_votes=models.IntegerField()


class voter_vote_status(models.Model):
    # Id = models.AutoField()
    voter_id=models.ForeignKey("voter",on_delete=models.DO_NOTHING)
    casted_vote=models.BooleanField(null=False)
