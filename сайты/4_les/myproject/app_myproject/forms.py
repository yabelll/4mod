from django import forms
from django.db import models
from django.forms import Textarea, TextInput, NumberInput, CheckboxInput, FileInput

class Advertisement(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    auction = models.BooleanField()
    image = models.ImageField()

class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': Textarea(attrs={'class': 'form-control form-control-lg'}),
            'price': NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'auction': CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': FileInput(attrs={'class': 'form-control form-control-lg'}),
        }