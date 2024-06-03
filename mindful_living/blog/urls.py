from django.urls import path, re_path
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about_view'),
    re_path('post/(?P<pk>\d+)', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    re_path('post/(?P<pk>\d+)/edit/', views.UpdatePostView.as_view(), name='post_edit')
]
