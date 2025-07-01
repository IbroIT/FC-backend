from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('players.urls')),
    path('api/news/', include('news.urls')),
    path('academy/', include('academy.urls')),
    path('coaches/', include('coaches.urls')),
]
