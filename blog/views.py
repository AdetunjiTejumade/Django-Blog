
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView
)
from .models import Blog
from django.urls import reverse_lazy
# Create your views here.


class BlogListView(ListView):
    model = Blog
    context_object_name = 'posts'
    template_name = 'index.html'


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'post'
    template_name = 'post_detail.html'

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = "post_delete.html"
    success_url = reverse_lazy('home')
    login_url = 'login'
    
class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = "post_update.html"
    fields = ['title','body']
    login_url = 'login'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = "create_post.html"
    fields = ['title', 'body']
    login_url = 'login'