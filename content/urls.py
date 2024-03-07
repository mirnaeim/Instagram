from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, like

post_router = routers.DefaultRouter()
post_router.register('', PostViewSet,)

urlpatterns = [
    # path(f'{settings.ADMIN_PANEL_URL}/', admin.site.urls)
    path('posts/', include(post_router.urls)),
    path('posts/<int:post_id>/like', like)

]
