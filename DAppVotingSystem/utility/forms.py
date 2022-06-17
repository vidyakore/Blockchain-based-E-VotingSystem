from django import forms
from django.core.validators import RegexValidator
from .models import election_type,party,constituency,constituency_type,booth_manager,voter,voter_constituency,candidate,candidate_party
my_validator = RegexValidator(r"^([0-9]){4}([0-9]){4}([0-9]){4}$", "Your string should contain letter A in it.")


FRUIT_CHOICES= [
    (None,'Election Type '),
    ('vidhansabha', 'Vidhansabha'),
    ('loksabha', 'Loksabha'),
    ]


def number_code_validator(value):
    if not re.compile(r'^([0-9]){4}([0-9]){4}([0-9]){4}$').match(value):
        raise ValidationError('Enter Number Correctly')
class voterAadhar(forms.Form):
        class Meta:
            model = voter
            fields = ['aadhaar_no','election_type']
        aadhar_no = forms.CharField(label='aadhar_no', max_length=12, required=True, validators=['^([0-9]){4}([0-9]){4}([0-9]){4}$'])
        election_type= forms.CharField(label='Select Election Type : ', widget=forms.Select(choices=FRUIT_CHOICES))
