from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from list.models import UserList
from list.serializer import UserListSerializer

# Create your views here.


class UserListViewSet(ModelViewSet):
    queryset = UserList.objects.all()
    serializer_class = UserListSerializer
