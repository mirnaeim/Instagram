from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer, ProfileSerializer
from .models import Profile, Contact
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


@api_view()
def follow(request, profile_id):
    profile = Profile.objects.get(id=request.user.id)
    following = Profile.objects.get(id=profile_id)
    contact = Contact.objects.filter(user_from=profile, user_to=following)
    if contact :
        contact.delete()
        return Response(following.username + " is Unfollowed")
    else:
        Contact.objects.create(
            user_from=profile,
            user_to=following
        )
        return Response(profile.username + " started folowing " + following.username)

