from django import forms


class TodoForm(forms.Form):
    task = forms.CharField(label='Add a task', max_length=255)
