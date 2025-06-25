import filters
from rest_framework import generics
from .models import FootballNews
from .serializers import NewsSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

class FeaturedNewsList(generics.ListAPIView):
    queryset = FootballNews.objects.filter(is_featured=True)
    serializer_class = NewsSerializer

class AllNewsList(generics.ListAPIView):
    queryset = FootballNews.objects.all()
    serializer_class = NewsSerializer

class NewsDetail(generics.RetrieveAPIView):
    queryset = FootballNews.objects.all()
    serializer_class = NewsSerializer

class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class AllNewsList(generics.ListAPIView):
    queryset = FootballNews.objects.all()
    serializer_class = NewsSerializer
    pagination_class = StandardPagination

class AllNewsList(generics.ListAPIView):
    queryset = FootballNews.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'excerpt', 'content']