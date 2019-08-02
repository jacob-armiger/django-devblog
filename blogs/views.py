from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from comments.models import Comment

from .models import BlogPost

from .forms import BlogPostForm

# Create your views here.
def index(request):
    """Home page for blogs"""
    posts = BlogPost.objects.order_by('-date_added')

    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

def staff_page(request, staff_id):
    """Page that shows all the posts of a staff member"""
    staff_id = get_object_or_404(User, id=staff_id)
    posts = BlogPost.objects.filter(owner=staff_id).order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/staff_page.html', context)

def post(request, post_id):
    """Page that shows an individual post and its comments"""
    post = get_object_or_404(BlogPost, id=post_id)
    comments = Comment.objects.filter(post=post_id).order_by('-date_added')
    
    context = {'post': post, 'comments': comments,}
    return render(request, 'blogs/post.html', context)

@login_required
@staff_member_required
def new_post(request):
    """Page for staff members to create a new blog post"""
    if request.method == 'POST':
        form = BlogPostForm(data=request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:index')
    else:
        form = BlogPostForm()
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
@staff_member_required
def edit_post(request, post_id):
    """Page for staff members to edit a blog post"""
    post = BlogPost.objects.get(id=post_id)
    check_owner(request, post)

    if request.method != 'POST':
        """Initial request; pre-fill form with current post"""
        form = BlogPostForm(instance=post)
    else:
        """POST data submitted; process data"""
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)



#My utility functions
def check_owner(request, post):
    """check to see if current user is editing their own post"""
    if post.owner != request.user:
        raise Http404