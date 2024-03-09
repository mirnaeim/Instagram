from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view

from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment, Like
from account.models import Profile
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from log.models import Log

# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    search_fields = ('account', 'caption',)

    def perform_create(self, serializer):
        # Assign the current user to the profile field of the post
        user = self.request.user
        profile = Profile.objects.get(id=user.id)
        serializer.save(account=profile)
        Log.objects.create(
            log_text=f"@{profile.username} posted {self.id}"
        )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Assign the current user to the author field of the post
        user = self.request.user
        profile = Profile.objects.get(id=user.id)
        serializer.save(account=profile)
        post_id = serializer.data['post']
        Log.objects.create(
            log_text=f"@{self.request.user.username} commented for post id {post_id}"
        )


@api_view()
def like(request, post_id):
    post = Post.objects.get(id=post_id)
    profile = Profile.objects.get(id=request.user.id)
    like = Like.objects.filter(post=post, account_id=profile.id)
    if like:
        like.delete()
        Log.objects.create(
            log_text=f'@{profile.username} unLiked post id {post_id}'
        )
        return Response("Post UnLiked")
    else:
        Like.objects.create(
            account=profile,
            post=post
        )
        Log.objects.create(
            log_text=f'@{profile.username} Liked post id {post_id}'
        )
        return Response("Post Liked")
