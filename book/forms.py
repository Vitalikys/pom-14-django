from django import forms

from author.models import Author
from .models import Book

class BookForm(forms.ModelForm):
    # name = forms.CharField(label='Book Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # description = forms.CharField(label = 'опис', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # count = forms.IntegerField(label='кількість', widget= forms.NumberInput(attrs={'class': 'form-control'}))
    # authors = forms.ChoiceField(label='автор',choices=Author.get_all(), widget=forms.Select(attrs={'class': 'form-control'}))
    # authors = forms.MultipleChoiceField(label='автор',choices=Author.get_all(), widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    class Meta:
        model = Book
        fields = 'name', 'description', 'count', 'authors'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows':6}),
            'count': forms.NumberInput(attrs={'class': 'form-control'}),
            'authors': forms.SelectMultiple(attrs={'class': 'form-control'})
        }