from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['text', 'mail']
        labels = {'text': 'Текст вашего сообщения', 'mail': 'Ваша почта'}
        help_texts = {'text':
                      ('Пожелание хорошего настроения вместо бесполезного '
                       'хелптекста :)')}
        widgets = {'text': forms.TextInput(attrs={'class': 'form-control'}),
                   'mail': forms.TextInput(attrs={'class': 'form-control'})}
