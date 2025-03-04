from django import forms
from . import models

class BirthdayForm(forms.ModelForm):
    class Meta:
        model = models.Birthday
        fields = ['name', 'day', 'month', 'year']
        labels = {
            'name' : 'Full Name',
            'day' : 'Day',
            'month' : "Month",
            'year' : 'Year'
        }