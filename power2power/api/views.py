from django.shortcuts import render
from .serializers import UserSerializer, NodeSerializer
from .models import User, Node

from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets


# Create your views here.
def index(request):
    #web3 = Web3(HTTPProvider('http://10.0.0.4:8545'))

    return render(request, 'index.html')

def graph(request):
    return render(request, 'graph.html')

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
