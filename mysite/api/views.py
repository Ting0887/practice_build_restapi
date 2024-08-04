from django.shortcuts import render
from rest_framework import generics
from .models import NewsArticle
from .serializers import NewsArticleSerializer
    
class ArticleListCreate(generics.ListCreateAPIView):
    querset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer
    def get_queryset(self):
        return NewsArticle.objects.all()

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer

def ArticleList(request):
    return render(request, 'news_article_view.html')