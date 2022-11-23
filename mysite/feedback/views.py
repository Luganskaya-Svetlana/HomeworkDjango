from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import FeedbackForm
from .models import Feedback


def feedback(request):
    template = 'feedback/feedback_page.html'
    form = FeedbackForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        text = form.cleaned_data['text']
        user_mail = form.cleaned_data['mail']
        send_mail(
            'Feedback',
            text,
            'user@example.com',
            [settings.ADMIN_MAIL],
            fail_silently=False,)
        send_mail(
            'Your feedback',
            ('Здравствуйте! Мы получили от вас следующее сообщение: '
             f'"{text}" Спасибо за ваш отзыв.'),
            'user@example.com',
            [user_mail],
            fail_silently=False,)
        feedback = Feedback(text=text, mail=user_mail)
        feedback.save()
        messages.success(request, 'Отзыв отправлен')
        return redirect('feedback:feedback')
    context = {'form': form}
    return render(request, template, context)
