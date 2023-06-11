from django.contrib import admin

#import Brew model below
from .models import Brew, Event, Snack
#register model below
admin.site.register(Brew)
admin.site.register(Event)
admin.site.register(Snack)

