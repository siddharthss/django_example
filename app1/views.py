from django.shortcuts import render
from rest_framework import viewsets
from app1.models import Project
from app1.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
