from app1.models import Project

__author__ = 'siddharth'
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    """
    Project model serializer
    """
    class Meta:
        model = Project
        fields = "__all__"
        depth = 1
