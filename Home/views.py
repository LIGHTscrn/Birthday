from django.shortcuts import render
from . import forms

# Create your views here.

def Home(request):
    form = forms.BirthdayForm()
    return render(request, 'Home/index.html', {'form': form })
