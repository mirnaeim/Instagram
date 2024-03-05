from django.contrib import admin
from django.contrib.admin import register

from .models import Profile, Contact


@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
