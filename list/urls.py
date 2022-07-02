from django import views
from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()

router.register('adminlist', views.AdminListViewSet)
router.register('userlist', views.UserListViewSet, basename='user')

urlpatterns = router.urls
