from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
# from models import election_type,party,constituency,constituency_type,booth_manager,voter,voter_constituency
from . import models
from .forms import voterAadhar

#BLockchain Imports
from solcx import compile_standard, install_solc
import json
# from web3 import Web3 
# from dotenv import load_dotenv
# from web3.middleware import geth_poa_middleware
# import os
# load_dotenv()

# Create your views here.

def home(request):
    return render(request,'home.html')

def GetVoter(request):
    context ={}
    context['form']= voterAadhar()
    return render(request,'GetVoter.html',context)

def GetVoterDetails(request,aadhar_no):
    obj = models.voter.objects.get(voter_aadhaar_no=aadhar_no)
    # obj = models.voter.objects.get(voter_aadhaar_no=request.aadharNo)
    context = {"object":request}
    return render(request,'VoterDetails.html',context)

def hello(request):
    return HttpResponse("Hello world")

