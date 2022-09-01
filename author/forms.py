from django import forms
from .models import Author

class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = 'name', 'surname' ,'patronymic'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control'})
        }