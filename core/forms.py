from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        widgets = {
            'due_date': forms.DateInput(attrs={'class':'datepicker'})
        }
        fields = ('title', 'text', 'due_date', 'completed')
