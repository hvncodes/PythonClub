from django import forms
from .models import Events, Resources, Comments

class EventForm(forms.ModelForm):
    class Meta:
        model=Events
        fields='__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields='__all__'