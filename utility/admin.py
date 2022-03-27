from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CandidateList)
admin.site.register(Votes)
admin.site.register(CastedVotes)
admin.site.register(Constituency)