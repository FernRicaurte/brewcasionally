from django.contrib import admin

#import Brew model below
from .models import Brew, Event
#register model below
admin.site.register(Brew)
admin.site.register(Event)
