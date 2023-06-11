from django.db import models
from django.urls import reverse

OCCASIONS = (
    ('S', 'Sports Viewing'),
    ('P', 'Party'),
    ('O', 'Outdoor Event'),
    ('G', 'Get-Together'),
    ('F', 'Formal Event'),
    ('I', 'Individual Consumption'),
    ('O', 'Other')
)

class Brew(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    abv = models.CharField(max_length=100)

def __str__(self):
    return self.name
    # Add this method
def get_absolute_url(self):
    return reverse('detail', kwargs={'brew_id': self.id})

class Event(models.Model):
    date = models.DateField()
    occasion = models.CharField(max_length=1, choices=OCCASIONS, default=OCCASIONS[6][6])

