from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Profile(User):
    is_public = models.BooleanField(default=True, verbose_name='Is Public')

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'{self.username}'


class Contact(models.Model):
    user_from = models.ForeignKey(Profile, related_name='followings', on_delete=models.CASCADE)
    user_to = models.ForeignKey(Profile, related_name='followers', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'

#
# # Add following field to User dynamically
# user_model = get_user_model()
# user_model.add_to_class('following',
#                         models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False))
