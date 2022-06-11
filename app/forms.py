from socket import fromshare
from django import forms

class UserInputDataForm(forms.Form):
    project = forms.CharField(max_length=100)
    enrollment_date = forms.DateField()
    distribution_date = forms.DateField()
    name = forms.CharField(max_length=50)
    age= forms.IntegerField()
    sex=forms.CharField(max_length=20)
    address=forms.CharField(max_length=50)
    pincode= forms.CharField(max_length=6)
    mobile_number= forms.IntegerField()
    landline_number= forms.CharField(max_length= 10)
    caliper=forms.CharField(max_length=50)
    wheelchair = forms.CharField(max_length=10)
    tricycle=forms.CharField(max_length=10)
    cruthces=forms.CharField(max_length=10)
    hearing_aids= forms.CharField(max_length=10)
    hands=forms.CharField(max_length=10)
    above_knee_jaipur_foot= forms.CharField(max_length=20)
    below_knee_jaipur_foot= forms.CharField(max_length=20)
    ratnanidhi_leg= forms.CharField(max_length=20)
    ls_belt= forms.CharField(max_length=10)
    knee_cap= forms.CharField(max_length=10)
    soft_collor= forms.CharField(max_length=10)
    maritial_status= forms.CharField(max_length= 10)
    educational_background= forms.CharField(max_length= 25)


class CheckConditions(forms.Form):
    age= forms.IntegerField()
    sex= forms.CharField(max_length=20)
    maritial_status= forms.CharField(max_length= 10)
    wheelchair = forms.CharField(max_length=10)
    tricycle=forms.CharField(max_length=10)
    cruthces=forms.CharField(max_length=10)
    hearing_aids= forms.CharField(max_length=10)
    hands=forms.CharField(max_length=10)
    ls_belt= forms.CharField(max_length=10)
    knee_cap= forms.CharField(max_length=10)
    soft_collor= forms.CharField(max_length=10)


