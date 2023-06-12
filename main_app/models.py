from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Snack(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f'A {self.description} {self.name}'
    
    def get_absolute_url(self):
        return reverse('snacks_detail', kwargs={'pk': self.id})

class Brew(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    abv = models.CharField(max_length=100)
    #M:M relationship below
    snacks = models.ManyToManyField(Snack)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'brew_id': self.id})


class Event(models.Model):
    OCCASIONS = (
        ('S', 'Sports Viewing'),
        ('P', 'Party'),
        ('O', 'Outdoor Event'),
        ('G', 'Get-Together'),
        ('F', 'Formal Event'),
        ('I', 'Individual Consumption'),
        ('O', 'Other')
    )
    date = models.DateField('event date')
    occasion = models.CharField(max_length=1, choices=OCCASIONS, default=OCCASIONS[0][0])

    brew = models.ForeignKey(Brew, on_delete=models.CASCADE) 

def __str__(self):
    return f"{self.get_occasion_display()} on {self.date}"

class Meta:
    ordering = ['-date'] 







