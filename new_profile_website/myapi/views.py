from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProjectInfoSerializers
from .models import ProjectInfo

# Create your views here.


class ProjectView(viewsets.ModelViewSet):
    queryset = ProjectInfo.objects.filter(show=True)
    serializer_class = ProjectInfoSerializers


def random(request):
    return HttpResponse("Hello World")
