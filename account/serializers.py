from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        # TODO number of followers and followings
        fields = (
            'id',
            'username',
            'followers',
            'followings',
            # 'bio',
            # 'name',
        )
