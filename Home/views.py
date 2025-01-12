from django.shortcuts import render
from . import forms

# Create your views here.

def Home(request):
    if request.method == 'POST':
        form = forms.BirthdayForm(request.POST)
        if form.is_valid():
            form.save()
    form = forms.BirthdayForm()
    return render(request, 'Home/index.html', {'form': form })
