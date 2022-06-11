from django import forms
from django.core.validators import RegexValidator
my_validator = RegexValidator(r"^([0-9]){4}([0-9]){4}([0-9]){4}$", "Your string should contain letter A in it.")

def number_code_validator(value):
    if not re.compile(r'^([0-9]){4}([0-9]){4}([0-9]){4}$').match(value):
        raise ValidationError('Enter Number Correctly')
class voterAadhar(forms.Form):
    aadhar_no = forms.CharField(label='aadhar_no', max_length=12, required=True, validators=['^([0-9]){4}([0-9]){4}([0-9]){4}$'])