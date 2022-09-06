from django import forms

from authentication.models import CustomUser
from order.models import Order


class OrderForm(forms.ModelForm):
    # user = forms.ChoiceField(choices=CustomUser.get_all(), label='Користувач:')
    class Meta:
        model = Order
        fields = 'book', 'user', 'plated_end_at'
        widgets = {
            'book': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.RadioSelect(),
            'plated_end_at': forms.DateInput(attrs={'type': 'date'}),
        }