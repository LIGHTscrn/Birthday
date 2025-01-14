from django.shortcuts import render
from . import forms
from . import models
from datetime import datetime

# Create your views here.

def Home(request):
    data = models.Birthday.objects.all()

    # Check for Birthday
    today = datetime.now()
    birthday_people = models.Birthday.objects.filter(day=today.day, month=today.month)
    if birthday_people.exists():
        birthday_names = ', '.join([person.name for person in birthday_people])
        return render(request, 'Home/index.html', {'birthdays': data, 'message':'Add Birthday','birthday_message': f'Happy Birthday, {birthday_names}!'})

    form = forms.BirthdayForm()
    print(data, 'This is data')
    return render(request, 'Home/index.html', {'form': form, 'message': "Add Birthday", 'birthdays': data})

def addBirthday(request):
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

                if not name or not day or not year:
                    return render(request, 'Home/index.html', {'form' : form, 'error' : 'Missing Fields', 'birthdays' : data})
                
                if models.Birthday.objects.filter(name=name, day=day, month=month, year=year).exists():
                    return render(request, 'Home/index.html', {'form': form, 'error': 'This birthday entry already exists', 'birthdays': data})

                print(name, day, month, year)
                person = models.Birthday(name=name, day=day, month=month, year=year)
                try:
                    person.save()
                    data = models.Birthday.objects.all() 
                except Exception as e:
                    print(f"Error saving: {e}")
                    return render(request, 'Home/index.html', {'form': form, 'error': f"Error saving: {e}", 'birthdays': data})
                print(data, 'This is data1')
                return render(request, 'Home/index.html', {'form': form, 'success': "Successfully added Birthday", 'birthdays': data})
            else:
                return render(request,'Home.index.html', {'form': form, 'error': 'Invalid Form', 'birthdays': data})
        else:
            return render(request, 'Home/index.html', {'form': form, 'error': 'Invalid Request', 'birthdays': data})

