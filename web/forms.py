from .models import Orders
from django.forms import ModelForm

class OrdersForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['name', 'token', 'bank_details', 'amount', 'limit', 'date_craete', 'date_update', 'status', 'bill']
