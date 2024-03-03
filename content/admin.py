from django.contrib import admin
from django.contrib.admin import register

from .models import Post, PostMedia

# Register your models here.


@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'caption',)


@register(PostMedia)
class PostMediaAdmin(admin.ModelAdmin):
    list_display = ('get_media_type_display',)
