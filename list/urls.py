from django import views
from django.urls import path
from rest_framework.routers import SimpleRouter

from list.models import UserList
from . import views

router = SimpleRouter()

router.register('adminlist', views.AdminListViewSet)
router.register('userlist', views.UserListViewSet, basename='user')
# router.register('userdetail', views.UserDetailViewSet,
#                 basename='userlistdetail')

# patterns = [
#     path('userlist/<int:pk>', views.UserListView.as_view())
# ]

urlpatterns = router.urls
