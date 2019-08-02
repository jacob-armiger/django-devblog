"""Define URL patterns for blogs"""
from django.urls import path

from . import views

app_name = 'comments'
urlpatterns = [
    # Page that shows comments
    path('comments/<int:post_id>', views.comments, name='comments'),
    # Page to create a comment
    path('create_comment/<int:post_id>/', views.create_comment, name='create_comment'),
]