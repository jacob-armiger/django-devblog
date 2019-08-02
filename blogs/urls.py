"""Define URL patterns for blogs"""
from django.urls import path

from . import views

app_name="blogs"
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # page to create a new post
    path('new_post/', views.new_post, name='new_post'),
    # page to edit a post
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    # Page that shows a certain staff member's post
    path('staff_page/<int:staff_id>/', views.staff_page, name='staff_page'),
    # Page that shows a post and its comments
    path('post/<int:post_id>/', views.post, name='post'),
]