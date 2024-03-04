from django.urls import path, include
from rest_framework import routers
from .views import ProfileViewSet

account_router = routers.DefaultRouter()
account_router.register('', ProfileViewSet,)


urlpatterns = [
    # TODO accounts/username for retrieving
    path('profiles/', include(account_router.urls,),),
]
