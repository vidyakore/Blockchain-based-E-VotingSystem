from django.urls import path

from . import views
app_name = 'utility'
urlpatterns = [
    path('', views.home, name='home'),
    path('GetVoter/', views.GetVoter, name='GetVoter'),
    path('GetVoterDetails/', views.GetVoterDetails, name='VoterDetails'),
]