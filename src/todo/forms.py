from django import forms
from django.forms import ModelForm

from .models import Task


#creating model forms   
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('created',)

        widgets = {
        'due_time': forms.TimeInput(format='%H:%M %p' ,attrs={'type': 'time'}),
        'due_date': forms.DateInput(format = "%d-%m-%y", attrs={'type': 'date'} )
            }

