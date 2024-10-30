from django.urls import path
from .views import BlogListView
urlpatterns = [
    
    path('home/', BlogListView.as_view())
]