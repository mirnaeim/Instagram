from django.db import models
from account.models import Profile


class MyBaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date',)
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Updated Date',)

    class Meta:
        abstract = True
        ordering = ('pk',)

    def __str__(self):
        raise NotImplementedError('Implement __str__ method')


class Post(MyBaseModel):
    account = models.ForeignKey(Profile, null=False, blank=False, on_delete=models.CASCADE)
    caption = models.TextField(null=False, blank=False, verbose_name='Caption')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('id',)

    # todo truncate upto 15 chars
    def __str__(self):
        return self.caption

    def media(self):
        return self.post_media.all()

    def images(self):
        return self.post_media.filter(media_type='image').all()

    def videos(self):
        return self.post_media.filter(media_type='video').all()

    def audios(self):
        return self.post_media.filter(media_type='audio').all()


class PostMedia(MyBaseModel):
    MEDIA_TYPE_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )

    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE, related_name='post_media',
                             verbose_name='Posts')
    media_type = models.CharField(max_length=6, choices=MEDIA_TYPE_CHOICES)
    media_file = models.FileField(upload_to='content/post/')

    def __str__(self):
        return self.post.caption
