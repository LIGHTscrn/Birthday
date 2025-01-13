from django.shortcuts import render
from . import forms
from . import models
from datetime import datetime

# Create your views here.

def Home(request):
    data = models.Birthday.objects.all()
    if request.method == 'POST':
        form = forms.BirthdayForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            day = form.cleaned_data['day']

            if day < 1 or day > 31:
                return render(request, 'Home/index.html' , {'form' : form, 'error' : 'Invalid Day', 'birthdays' : data})

            month = form.cleaned_data['month']

            if month < 1 or month > 12:
                return render(request, 'Home/index.html' , {'form' : form, 'error' : 'Invalid Month', 'birthdays' : data})

            if month == 2 and day > 29:
                return render(request, 'Home/index.html' , {'form' : form, 'error' : 'Invalid Day for February','birthdays' : data})

            year = form.cleaned_data['year']

            if year < 1900 or year > datetime.now().year:
                return render(request, 'Home/index.html' , {'form' : form, 'error' : 'Invalid Year', 'birthdays' : data})

            person = models.Birthday(name=name, day=day, month=month, year=year)
            person.save()
        return render(request, 'Home/index.html' , {'form' : form , 'success' : "Successfully added Birthday", 'birthdays' : data })
    form = forms.BirthdayForm()
    return render(request, 'Home/index.html', {'form': form , 'message' : "Add Birthday" , 'birthdays' : data})
