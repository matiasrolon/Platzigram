""""Posts URLs"""
# Django
from django.urls import path
# Views

from posts import views

urlpatterns = [
    path(
        route= 'posts-direct/',
        view= views.list_posts_direct, name='posts-direct'
    ),
    path(
        route='',
        view=views.PostsFeedView.as_view(),
        name='feed'),
    path(
        route='posts/new/',
        view=views.create_post,
        name='create'
    )
]