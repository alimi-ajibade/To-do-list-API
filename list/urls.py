from django import views
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserListViewSet

router = SimpleRouter()

router.register('', UserListViewSet)

urlpatterns = router.urls
