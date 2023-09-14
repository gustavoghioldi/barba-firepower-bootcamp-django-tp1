from django import forms
import datetime

now_year = int(str(datetime.datetime.now().year)[2:])

class CheckoutForm(forms.Form):
    card_number = forms.IntegerField(max_value=9507990000004905, min_value=1507990000004905)
    card_expiration_month= forms.IntegerField(max_value=12, min_value=1)
    card_expiration_year = forms.IntegerField(max_value=99, min_value=now_year)
    security_code = forms.IntegerField(max_value=999, min_value=0)
    card_holder_name = forms.CharField(max_length=128)
    card_holder_identification_type = forms.CharField(max_length=3, min_length=3,  initial="DNI")
    card_holder_identification_number = forms.IntegerField(max_value=99999999, min_value=10000)
