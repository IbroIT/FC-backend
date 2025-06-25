from django.urls import path
from .views import FeaturedNewsList, AllNewsList, NewsDetail

urlpatterns = [
    path('featured/', FeaturedNewsList.as_view(), name='featured-news'),
    path('all/', AllNewsList.as_view(), name='all-news'),
    path('<int:pk>/', NewsDetail.as_view(), name='news-detail'),
]