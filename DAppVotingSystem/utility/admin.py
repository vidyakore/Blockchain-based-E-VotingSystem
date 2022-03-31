from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(election_type)
admin.site.register(party)
admin.site.register(constituency)
admin.site.register(constituency_type)
admin.site.register(contract_manager)
admin.site.register(booth_manager)
admin.site.register(voter)
admin.site.register(voter_constituency)
admin.site.register(candidate)
admin.site.register(candidate_party)
admin.site.register(candidate_constituency)
admin.site.register(votes)
admin.site.register(voter_vote_status)