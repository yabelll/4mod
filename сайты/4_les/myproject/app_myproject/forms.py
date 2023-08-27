from django.db import models
from django.forms import Textarea, TextInput, NumberInput, CheckboxInput, FileInput

class AdvertisementForm(models.Model):
    title = models.CharField(max_length=64, widget = {'name': TextInput(attrs={'class': 'form-control form-control-lg'})})
    description = models.CharField(max_length=1000, widget = {'name': Textarea(attrs={'class': 'form-control form-control-lg'})})
    price = models.DecimalField(max_digits=100000, decimal_places=100, widget = {'name': NumberInput(attrs={'class': 'form-control form-control-lg'})})
    auction = models.BooleanField(widget = {'name': CheckboxInput(attrs={'class': 'form-control form-control-lg'})})
    image = models.ImageField(widget = {'name': FileInput(attrs={'class': 'form-control form-control-lg'})})                 
