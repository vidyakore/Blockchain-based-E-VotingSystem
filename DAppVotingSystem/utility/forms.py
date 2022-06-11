from django import forms

class voterAadhar(forms.Form):
    aadhar_no = forms.CharField(label='aadhar_no', max_length=50)