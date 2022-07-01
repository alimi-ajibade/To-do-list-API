from rest_framework import serializers
from .models import UserList


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserList
        fields = ['id', 'title', 'remainderTime',
                  'remainderDate', 'remainder']

    def create(self, validated_data):
        task = UserList(**validated_data)
        task.user_id = self.context['user_id']
        task.save()
        return task
