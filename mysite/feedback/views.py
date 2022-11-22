from django.shortcuts import render, redirect
from .forms import FeedbackForm


def feedback(request):
    template = 'feedback/feedback_page.html'
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        # text = form.cleaned_data['text']
        return redirect('feedback:feedback')
    context = {'form': form}
    return render(request, template, context)
