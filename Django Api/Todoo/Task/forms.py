from django import forms
from Task.models import TodoTask


class DateInpute(forms.DateInput):
    input_type = 'date'

class TaskTodoForm(forms.ModelForm):
    created = forms.DateField(widget=DateInpute)
    class Meta:
        model = TodoTask
        fields = ('title','content','category')