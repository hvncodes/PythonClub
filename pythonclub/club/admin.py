from django.contrib import admin
from .models import TopicType, Event, Comment

# Register your models here.
admin.site.register(TopicType)
admin.site.register(Event)
admin.site.register(Comment)
