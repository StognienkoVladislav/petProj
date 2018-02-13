
from .models import Order
from django import forms


class OrderForm(forms.ModelForm):

    internalID = forms.IntegerField
    orderCreationTime = forms.CharField
    merchantID = forms.IntegerField
    status = forms.CharField
    amount = forms.CharField
    currency = forms.CharField
    orderID = forms.TextInput
    orderType = forms.CharField
    orderDescription = forms.CharField

    class Meta:
        model = Order
        fields = ['internalID', 'orderCreationTime', 'merchantID',
                  'status', 'amount', 'currency', 'orderID',
                  'orderType', 'orderDescription']