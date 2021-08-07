from django.views.generic import ListView, DetailView

from .models import *

# Create your views here.
class HomeNews(ListView):
    model = Posts
    template_name = 'coffee_blog/blog.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Блог'
        return context

    def get_queryset(self):
        return Posts.objects.filter(is_published=True)

class ViewNews(DetailView):
    model = Posts
    template_name = 'coffee_blog/detail_post.html'
    context_object_name = 'posts_item'
