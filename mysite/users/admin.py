from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile


class ProfileInlined(admin.TabularInline):
    model = Profile


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInlined,)
    can_delete = False


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
