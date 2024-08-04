from django.urls import path
from . import views

urlpatterns = [
    path("newsarticles/", views.ArticleListCreate.as_view(), name="newsarticlepost-view-create"),
    path('article/<int:pk>/', views.ArticleDetail.as_view(), name='article-detail'),
]
