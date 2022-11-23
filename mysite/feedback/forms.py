from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['text', 'mail']
        labels = {'text': 'Текст вашего сообщения', 'mail': 'Ваша почта'}
        help_texts = {'text': 'Введите ваше сообщение'}
        widgets = {'text': forms.TextInput(attrs={'class': 'form-control'})}
