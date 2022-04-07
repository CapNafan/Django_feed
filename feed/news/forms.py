from django import forms
from django.forms import ModelForm
from .models import NewsItem


class NewsForm(ModelForm):
    class Meta:
        model = NewsItem
        fields = ('title', 'body', 'image')

        labels = {'title': '',
                  'body': '',
                  'image': ''}

        widgets = {'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'News Title'}),
                   'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'News body'})
                   }
