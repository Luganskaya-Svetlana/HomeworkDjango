from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .forms import FeedbackForm


def feedback(request):
    template = 'feedback/feedback_page.html'
    form = FeedbackForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        text = form.cleaned_data['text']
        send_mail(
            'Feedback',
            text,
            'user@example.com',
            ['admin@example.com'],
            fail_silently=False,)
        return redirect('feedback:feedback')
    context = {'form': form}
    return render(request, template, context)
