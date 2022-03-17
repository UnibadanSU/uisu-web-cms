from django.shortcuts import render
from rest_framework import viewsets
from news.models import Article, Profile, Tag, Executive
from news.serializers import ArticleSerializer, ProfileSerializer, TagSerializer, ExecutiveSerializer

# Create your views here.
class ArticleView(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class TagView(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class ExecutiveView(viewsets.ModelViewSet):
    serializer_class = ExecutiveSerializer
    queryset = Executive.objects.all()