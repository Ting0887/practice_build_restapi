from rest_framework import serializers
from .models import BlogPost, NewsArticle

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'published_date']


class NewsArticleSerializer(serializers.ModelSerializer):
    date_time = serializers.DateTimeField(format="%Y/%m/%d")
    class Meta:
        model = NewsArticle
        fields = '__all__'
