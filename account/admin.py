from django.contrib import admin
from django.contrib.admin import register

from .models import Profile


@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    raw_id_fields = ['user']
