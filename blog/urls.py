from django.urls import path

from .views import Home, PostsByCategory, GetPost, PostsByTag, Search, Comment

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('comment/<int:pk>/', Comment.as_view(), name="create_comment"),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('search/', Search.as_view(), name='search'),
]
