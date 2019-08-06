from django.shortcuts import render, redirect
from .models import Comment, BlogPost
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import CommentForm

# Create your views here.
def comments(request, post_id):
    """A view for a comment section"""
    """ Move logic into the app/view you want comments for. """
    comments = Comment.objects.filter(post=post_id).order_by('-date_added')

    context = {'comments': comments}
    return render(request, 'comments/comments.html', context)

@login_required
def create_comment(request, post_id):
    """Page for users to create a new comment"""
    post = BlogPost.objects.get(id=post_id)

    if request.method == 'POST':
        form = CommentForm(data=request.POST)

        if form.is_valid():
            create_comment= form.save(commit=False)
            #This creates the relationship between the comment and the user/post
            create_comment.owner = request.user
            create_comment.post = post

            create_comment.save()
            return redirect('blogs:post', post_id=post.id)
    else:
        form = CommentForm()
    context = {'form': form, 'post': post}
    return render(request, 'comments/create_comment.html', context)

@login_required
def delete_comment(request, comment_id):
    comment_to_delete = Comment.objects.get(id=comment_id)
    post = comment_to_delete.post
    if comment_to_delete.owner == request.user:
        comment_to_delete.delete()
    return redirect('blogs:post', post_id=post.id)

def edit_comment(request, comment_id):
    """Page for users to create a new comment"""
    comment = Comment.objects.get(id=comment_id)
    post = comment.post

    if request.method == 'POST':
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:post', post_id=post.id)
    else:
        form = CommentForm(instance=comment)
    
    context = {'form': form, 'comment': comment}
    return render(request, 'comments/edit_comment.html', context)
