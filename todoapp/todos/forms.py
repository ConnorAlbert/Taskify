from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    order = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Todo
        fields = ['task', 'priority', 'order']