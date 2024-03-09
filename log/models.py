from django.db import models

# Create your models here.


class Log(models.Model):
    time = models.DateTimeField(auto_now_add=True, verbose_name='Log Time')
    log_text = models.CharField(max_length=255, verbose_name='Log Text')

    class Meta:
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'
        ordering = ('time',)
