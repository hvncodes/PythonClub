from django.contrib import admin
from .models import Resources, Event, Comment

# Register your models here.
admin.site.register(Resources)
admin.site.register(Event)
admin.site.register(Comment)
