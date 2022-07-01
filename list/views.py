from django.db.models import Q
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from list.models import UserList
from list.serializers import UserListSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated

# Create your views here.


class AdminListViewSet(ModelViewSet):
    queryset = UserList.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAdminUser]


class UserListViewSet(ListModelMixin, RetrieveUpdateDestroyAPIView, GenericViewSet):
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserList.objects.filter(user_id=self.request.user.id)

    def get_serializer_context(self):
        return {'user_id': self.request.user}
