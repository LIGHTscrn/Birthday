from django.shortcuts import render, redirect, reverse
from . import forms
from . import models
from datetime import datetime
from django.contrib import messages

# Create your views here.

def Home(request):
    data = models.Birthday.objects.all()

    # Check for Birthday
    today = datetime.now()
    birthday_people = models.Birthday.objects.filter(day=today.day, month=today.month)
    if birthday_people.exists():
        birthday_names = ', '.join([person.name for person in birthday_people])
        return render(request, 'Home/index.html', {
            'birthdays': data,
            'message': 'Add Birthday',
            'birthday_message': f'Happy Birthday, {birthday_names}!'
        })

    form = forms.BirthdayForm()
    print(data, 'This is data')
    return render(request, 'Home/index.html', {'form': form, 'message': "Add Birthday", 'birthdays': data})

def addBirthday(request):
    if request.method == 'POST':
        form = forms.BirthdayForm(request.POST)
        if form.is_valid():

            if not form.cleaned_data['name'] or not form.cleaned_data['day'] or not form.cleaned_data['year']:
                messages.error(request, 'Some fields are empty')
                return redirect(reverse('Home:Home'))


            name = form.cleaned_data['name']
            day = form.cleaned_data['day']
            
            if day < 1 or day > 31:
                messages.error(request, 'Invalid day')
                return redirect(reverse('Home:Home'))


            month = form.cleaned_data['month']

            if month < 1 or month > 12:
                messages.error(request, 'Invalid month')
                return redirect(reverse('Home:Home'))


            if month == 2 and day > 29:
                messages.error(request, 'Invalid day in February')
                return redirect(reverse('Home:Home'))


            year = form.cleaned_data['year']

            if year < 1900 or year > datetime.now().year:
                messages.error(request, 'Invalid year')
                return redirect(reverse('Home:Home'))


            if models.Birthday.objects.filter(name=name, day=day, month=month, year=year).exists():
                messages.error(request, "The birthday already exists")
                return redirect(reverse('Home:Home'))


            print(name, day, month, year)
            person = models.Birthday(name=name, day=day, month=month, year=year)
            try:
                person.save()
            except Exception as e:
                print(f"Error saving: {e}")
                messages.error(request, f"{e}")
                return redirect(reverse('Home:Home'))

            messages.success(request, 'Successfully added Birthday')
            return redirect(reverse('Home:Home'))

        else:
            return redirect(reverse('Home:Home'))

    else:
        messages.error(request, 'Invalid request')
        return redirect(reverse('Home:Home'))

