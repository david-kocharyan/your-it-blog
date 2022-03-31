from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.articles.serializers import ArticleSerializer, ArticleDetailSerializer
from apps.articles.models import Article


class ArticleView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['name', 'tag__name', 'category__name', 'author__username']
    ordering_fields = ['title', 'created_at']
    filter_fields = ['tag', 'category', 'author']



class ArticleDetailView(generics.RetrieveAPIView):
    serializer_class = ArticleDetailSerializer
    queryset = Article.objects.all()
