from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task', 'completed', 'priority']
        widgets = {
            'priority': forms.Select(choices=Todo.PRIORITY_CHOICES),
        }