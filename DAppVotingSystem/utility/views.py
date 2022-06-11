from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
# from models import election_type,party,constituency,constituency_type,booth_manager,voter,voter_constituency
from . import models


#BLockchain Imports
from solcx import compile_standard, install_solc
import json
from web3 import Web3 
from dotenv import load_dotenv
from web3.middleware import geth_poa_middleware
import os
load_dotenv()

# Create your views here.

def home(request):
    return render(request,'home.html')

def GetVoter(request):
    return render(request,'GetVoter.html')

def hello(request):
    return HttpResponse("Hello world")

