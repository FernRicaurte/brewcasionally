from django.contrib import admin

#import Brew model below
from .models import Brew
#register model below
admin.site.register(Brew)
