from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.


class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


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


class UpdatePostView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-published_date')


# Comments section #####################################
########################################################

@login_required()
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
        else:
            form = CommentForm()
            return render(request, 'blog/comment_form.html', {form: form})

