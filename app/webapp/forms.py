from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'type', 'status']
        labels = {
            'summary': 'Заголовок',
            'description': 'Описание',
            'status': 'Статус',
            'type': 'Тип задачи'

        }
