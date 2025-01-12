from django.db import models

# Create your models here.

class Birthday(models.Model):
    name = models.CharField(max_length=100)
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.day}/{self.month}/{self.year}"
