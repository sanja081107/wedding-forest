from django.forms import ModelForm
from django import forms
from main.models import WeddingPhotos


class WeddingPhotosForm(ModelForm):

    class Meta:
        model = WeddingPhotos
        fields = ['photos']
        widgets = {
            'photos': forms.FileInput(attrs={'class': 'form-control', 'multiple': 'multiple'}),
        }
        labels = {
            'photos': ''
        }
