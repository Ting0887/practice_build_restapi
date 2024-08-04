from django.shortcuts import render
from rest_framework import generics
from django.db.models import Q
from rest_framework.response import Response
from .models import NewsArticle
from .serializers import NewsArticleSerializer
    
class ArticleListCreate(generics.ListCreateAPIView):
    querset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer
    def get_queryset(self):
        return NewsArticle.objects.all()

class ArticleListSearch(generics.ListAPIView):
    serializer_class = NewsArticleSerializer
    
    def get_queryset(self):
        queryset = NewsArticle.objects.all()
        query = self.request.query_params.get('q', None)
        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(content__icontains=query))
        return queryset

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer

def ArticleList(request):
    return render(request, 'news_article_view.html')

