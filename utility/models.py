from django.db import models
from django.forms import IntegerField

# Create your models here.
class CandidateList(models.Model):
     CandidateId=models.AutoField()
     CandidateName=models.CharField(max_length=200)
     CandidateConstituencyId=models.IntegerField()
     CandidatePartyId=models.IntegerField()
     CandidatePhoneNo=models.IntegerField()
     CandidateEmail= models.EmailField(max_length=200)


class Votes(models.Model):
    PartyId=models.IntegerField()
    CandidateId=models.IntegerField()
    NoOfVotes=models.IntegerField()


class CastedVotes(models.Model):
    VoterId=models.IntegerField()
    CastedVote=models.BooleanField(null=False)


class Constituency(models.Model):
    ConstituencyId=models.IntegerField()
    ConstituencyName=models.CharField(max_length=200)
    ConstituencyState=models.TextField(max_length=200)
    ConstituencyTypeOfElection=models.TextField(max_length=200)
    ConstituencyZipCode=models.IntegerField()
    TotalVoters=models.IntegerField()