from django.db import models
from django.urls import reverse

class Brew(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    abv = models.CharField(max_length=100)

def __str__(self):
    return self.name
    # Add this method
def get_absolute_url(self):
    return reverse('detail', kwargs={'brew_id': self.id})
