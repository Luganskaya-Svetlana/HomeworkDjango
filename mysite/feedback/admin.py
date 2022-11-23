from django.contrib import admin

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    fields = ('text', 'mail')
    list_display = ('text', 'mail', 'created_on')
