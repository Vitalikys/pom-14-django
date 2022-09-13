from datetime import timezone, datetime

from django import forms

from authentication.models import CustomUser
from order.models import Order


class OrderForm(forms.ModelForm):
    # user = forms.ChoiceField(choices=CustomUser.get_all(), label='Користувач:')
    class Meta:
        date_today = datetime.date.today
        end_date = datetime.date.today() + datetime.timedelta(days=14)
        model = Order
        fields = ['book','plated_end_at'] #, ,,'user'
        widgets = {
            'book': forms.Select(attrs={'class': 'form-control'}),
            # 'user': forms.RadioSelect(),
            # 'user': forms.HiddenInput(),
            'plated_end_at': forms.DateInput(attrs={'type': 'date', 'min':date_today, 'max':end_date}),
        }

        
