from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view

from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment, Like
from account.models import Profile
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response

# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterSet_fields = ('id', 'category',)
    search_fields = ('title', 'description',)

    def perform_create(self, serializer):
        # Assign the current user to the profile field of the post
        user = self.request.user
        profile = Profile.objects.get(id=user.id)
        serializer.save(account=profile)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Assign the current user to the author field of the post
        serializer.save(author=self.request.user)


@api_view()
def like(request, post_id):
    post = Post.objects.get(id=post_id)
    profile = Profile.objects.get(id=request.user.id)
    like = Like.objects.filter(post=post, account_id=profile.id)
    if like:
        like.delete()
        return Response("UnLiked")
    else:
        Like.objects.create(
            account=profile,
            post=post
        )
        return Response("Liked")
