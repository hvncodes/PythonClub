from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# resources, event, comment

class Resources(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcedescription=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table='resources'

class Event(models.Model):
    eventname=models.CharField(max_length=255)
    resources=models.ForeignKey(Resources, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    evententrydate=models.DateField()
    eventurl=models.URLField(null=True, blank=True)
    eventdescription=models.TextField()

    def __str__(self):
        return self.eventname

    class Meta:
        db_table='event'

class Comment(models.Model):
    commenttitle=models.CharField(max_length=255)
    commentdate=models.DateField()
    event=models.ForeignKey(Event, on_delete=models.CASCADE)
    user=models.ManyToManyField(User)
    commentrating=models.SmallIntegerField()
    commenttext=models.TextField()

    def __str__(self):
        return self.commenttitle
    
    class Meta:
        db_table='comment'