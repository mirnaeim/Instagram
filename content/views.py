from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


from .serializers import PostSerializer
from .models import Post
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('-pk')

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterSet_fields = ('id', 'category',)
    search_fields = ('title', 'description',)

    def perform_create(self, serializer):
        # Assign the current user to the author field of the post
        serializer.save(author=self.request.user)
