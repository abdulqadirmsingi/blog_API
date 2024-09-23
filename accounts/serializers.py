from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser

class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        permission_classes = [IsAdminUser]
        model = get_user_model()
        fields = ("id", "username",)