from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

from .forms import FeedbackForm
from .models import Feedback
from django.conf import settings


def feedback(request):
    template = 'feedback/feedback_page.html'
    form = FeedbackForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        text = form.cleaned_data['text']
        send_mail(
            'Feedback',
            text,
            'user@example.com',
            [settings.ADMIN_MAIL],
            fail_silently=False,)
        feedback = Feedback(text=text)
        feedback.save()
        messages.success(request, 'Отзыв отправлен')
        return redirect('feedback:feedback')
    context = {'form': form}
    return render(request, template, context)
