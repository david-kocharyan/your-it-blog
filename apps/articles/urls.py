from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleView.as_view(), name='article'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
]
