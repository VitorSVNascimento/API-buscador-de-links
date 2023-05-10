from django.urls import path
from .views import get_links

urlpatterns = [
    path('get-links/', get_links, name='get_links'),
]
