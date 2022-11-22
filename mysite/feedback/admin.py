from django.contrib import admin

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    fields = ('text',)
    list_display = ('text', 'created_on')
