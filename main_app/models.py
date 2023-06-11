from django.db import models
from django.urls import reverse

class Snack(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f'A {self.name} {self.description}'
    
    def get_absolute_url(self):
        return reverse('snacks_detail', kwargs={'pk': self.id})

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
    snacks = models.ManyToManyField(Snack)
    
def get_absolute_url(self):
    return reverse('detail', kwargs={'brew_id': self.id})

class Event(models.Model):
    date = models.DateField('event date')
    occasion = models.CharField(max_length=1, choices=OCCASIONS, default=OCCASIONS[0][0])

    brew = models.ForeignKey(Brew, on_delete=models.CASCADE)

def __str__(self):
    return f"{self.get_occasion_display()} on {self.date}"

class Meta:
    ordering = ['-date']

