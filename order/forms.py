from datetime import timezone, datetime

from django import forms

from authentication.models import CustomUser
from order.models import Order


class OrderForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     try:
    #         self.user_id = kwargs.pop('user_id')
    #     except KeyError:
    #         pass
    #     # from date import datetime, timezone
    #     super().__init__(*args, **kwargs)
    #     self.fields['book'].empty_label = 'Book not selected'
    #     self.fields['user'].initial = self.user_id
    #     self.fields['plated_end_at'].initial = timezone.now()+ datetime.timedelta(days=14)

    # user = forms.ChoiceField(choices=CustomUser.get_all(), label='Користувач:')
    class Meta:
        model = Order
        fields = 'book', 'user', 'plated_end_at'
        widgets = {
            'book': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.RadioSelect(),
            # 'user': forms.HiddenInput(),
            'plated_end_at': forms.DateInput(attrs={'type': 'date'}),
        }

