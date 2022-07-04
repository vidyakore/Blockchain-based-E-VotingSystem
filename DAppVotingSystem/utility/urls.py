from django.urls import path

from . import views

app_name = 'utility'

urlpatterns = [
    path('', views.home, name='home'),
    path('GetVoter/', views.GetVoter, name='GetVoter'),
    # path('GetVoterDetails/', views.GetVoterDetails, name='GetVoterDetails'),
    path('GetVoterDetails/', views.GetVoterDetails, name='GetVoterDetails'),
    path('Voting/', views.voting, name='Voting'),
    path('Vote/', views.vote, name='Vote'),
    path("Register/",views.register,name='Register')
    
    
]