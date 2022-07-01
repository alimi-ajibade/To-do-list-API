from rest_framework import serializers
from .models import UserList


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserList
        fields = ['title', 'remainderTime', 'remainderDate', 'remainder']
