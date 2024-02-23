from django import forms


class CUForm(forms.Form):
    title = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'placeholder': 'Name of task'}))
    description = forms.CharField(max_length=200,
                                  widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    due_date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Set date', 'type': 'date'}))
