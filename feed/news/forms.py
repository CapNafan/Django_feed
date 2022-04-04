from django import forms
from django.forms import ModelForm
from .models import NewsItem


class NewsForm(ModelForm):
    class Meta:
        pass
        model = NewsItem
        fields = ('title', 'body')

        labels = {'title': '',
                  'body': ''}

        widgets = {'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'News Title'}),
                   'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'News body'})
                   }
