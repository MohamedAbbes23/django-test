from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Receipt


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['store_name', 'date_of_purchase', 'item_list', 'total_amount']


        widgets = {
            'date_of_purchase' : forms.DateInput(attrs={'type': 'date'}),
        }

