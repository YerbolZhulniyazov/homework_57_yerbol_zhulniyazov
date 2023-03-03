from django import forms
from django.core.exceptions import ValidationError
from webapp.models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('summary', 'description', 'status', 'type')
        labels = {
            'summary': 'Заголовок задачи',
            'description': 'Описание задачи',
            'status': 'Статус',
            'type': 'Тип'
        }

    def clean_summary(self):
        summary = self.cleaned_data.get('summary')
        if len(summary) < 2:
            raise ValidationError('Заголовок должен быть длинее 2-ух символов')
        return summary