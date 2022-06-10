from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def GetVoter(request):
    return render(request,'GetVoter.html')