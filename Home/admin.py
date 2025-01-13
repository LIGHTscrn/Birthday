from django.contrib import admin
from .models import Birthday

@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    list_display = ('name', 'day', 'month' , 'year') 
    search_fields = ('name',)       
    list_filter = ('day','month', 'year')        
