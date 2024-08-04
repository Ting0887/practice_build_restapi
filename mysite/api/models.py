from django.db import models
from datetime import datetime

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    link = models.URLField()
    label = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    content = models.TextField()
    keyword = models.TextField()
    
    def save(self, *args, **kwargs):
        if isinstance(self.date_time, str):
            self.date_time = datetime.strptime(self.date_time, '%Y-%m-%d')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title