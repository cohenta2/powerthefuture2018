from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Ur mom')

def room(request):
    return render(request, 'ws/room.html', {'message':'Cunt'})
