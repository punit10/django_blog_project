from django.shortcuts import render
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView, UpdateView)
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now().order_by('-published_date'))


class PostDetailView(DetailView):
    model = Post


"""login_required can be done using decorators in template based views but here 
we are using LoginRequiredMixin in class based views, for similar task.
"""


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class UpdatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post