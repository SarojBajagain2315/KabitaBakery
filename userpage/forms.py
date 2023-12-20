from django.forms import ModelForm
from .models import *


class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields=['quantity','payment_method','phone_no','address']