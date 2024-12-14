from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.edit_profile, name='profile'),
]




from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

]
post/<int:pk>/update/

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/<int:pk>/update/', post/<int:pk>/comments/new/),
]




from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('search/', views.post_search, name='post_search'),
    path('tags/<str:tag_name>/', views.posts_by_tag, name='tagged_posts'),  # New URL
]

tags/<slug:tag_slug>/, PostByTagListView.as_view()