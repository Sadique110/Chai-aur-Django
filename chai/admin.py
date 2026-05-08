from django.contrib import admin
from .models import ChaiVerities

# Register your models here.
admin.site.register(ChaiVerities)

def __str__(self):
    return self.name