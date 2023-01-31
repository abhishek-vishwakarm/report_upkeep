from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import PostsSerializer
from .models import Posts
import requests

class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by('title')
    serializer_class = PostsSerializer


def home(request):
    response = requests.get('http://127.0.0.1:8000/posts/')
    data = response.json()
    return render(request,{'data': data})

# def bank(request):
#     response = requests.get('http://127.0.0.1:8000/posts/save/')
#     data = response.json()
#     return render(request, {'data':data})