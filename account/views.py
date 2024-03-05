from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from .serializers import RegisterSerializer, ProfileSerializer
from .models import Profile
# Register API


class RegisterApi(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
    queryset = Profile.objects.all()

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        profile = serializer.save()
        return Response({
            "profile": ProfileSerializer(profile, context=self.get_serializer_context()).data,
            "message": "Profile Created Successfully.  Now perform Login to get your token",
        })


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
