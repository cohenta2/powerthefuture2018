from django.shortcuts import render
from .serializers import UserSerializer, NodeSerializer
from .models import User, Node

from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

# Create your views here.
def index(request):
    return render(request, 'index.html')

class UserViewSet(mixins.RetrieveModelMixin,
                mixins.ListModelMixin,
                viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class NodeViewSet(mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.ListModelMixin,
                viewsets.GenericViewSet):

    queryset = Node.objects.all()
    serializer_class = NodeSerializer
