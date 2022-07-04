from django import forms
from django.core.validators import RegexValidator
from .models import election_type,party,constituency,constituency_type,booth_manager,voter,voter_constituency,candidate,candidate_party
my_validator = RegexValidator(r"^([0-9]){4}([0-9]){4}([0-9]){4}$", "Your string should contain letter A in it.")

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import get_user_model
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
class voterDetails(forms.Form):
        class Meta:
            model = voter
            fields = ['name','aadhaar_no','age','address','email','phone_no','constituency_name','constituency_type','constituency_id','voter_id']
        name = forms.CharField(label='name', max_length=100, required=True)
        aadhaar_no=forms.CharField(label='Aadhaar Number',max_length=12,required=True)
        email = forms.EmailField(label='Email', max_length=50, required=True)
        phone_no = forms.CharField(label='Phone Number', max_length=12, required=True)
        constituency_name = forms.CharField(label='Constituency Name', max_length=100, required=True)
        constituency_type = forms.CharField(label='Constituency Type', max_length=100, required=True)
        constituency_id=forms.CharField(label='Constituency Id', max_length=100, required=True,widget=forms.HiddenInput())
        voter_id=forms.CharField(label='Voter Id', max_length=100, required=True,widget=forms.HiddenInput())
# class candidate_List(forms.Form):
#     class Meta:
#         fields=[" candidatelist","constituency_name","constituency_type"]
#     candidatelist=forms.CharField(label='Candidatel',widget=forms.Select())
#     constituency_name=forms.CharField(label='Constituency',required=True)
#     constituency_type=forms.CharField(label='Election Type')
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='Enter a Valid Email',required=True)
    class Meta:
        model= get_user_model()
        fields =['name','email','phone_no','aadhaar_no','constituency_id']
    def save(self,commit=True):
        user=super(UserRegistrationForm, self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user
class userLogin(AuthenticationForm):
    pass