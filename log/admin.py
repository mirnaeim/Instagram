from django.contrib import admin
from .models import Log
# Register your models here.


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'log_text')
