from django.urls import path, include
from rest_framework import routers

from .views import ChoreViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'chore', ChoreViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]