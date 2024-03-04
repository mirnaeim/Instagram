from rest_framework import viewsets, permissions
from .models import Profile
from .serializers import ProfileSerializer


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
