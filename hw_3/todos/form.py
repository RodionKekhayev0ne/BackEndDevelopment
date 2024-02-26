from django import forms

from .models import Todo


class CUForm(forms.ModelForm):
    class Meta:
        model = Todo()
        fields = ['title', 'description', 'due_date']
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Name of task'}))
    description = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    due_date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Set date', 'type': 'date'}))


