from django.urls import path
from .views import BlogListView, BlogDetailView, BlogDeleteView, BlogUpdateView, BlogCreateView


urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('<int:pk>/delete', BlogDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/edit', BlogUpdateView.as_view(), name='post_edit'),
    path('create/', BlogCreateView.as_view(), name='new_post')
]
