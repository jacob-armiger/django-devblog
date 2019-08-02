from django.shortcuts import render, redirect
from .models import Comment, BlogPost

from .forms import CommentForm

# Create your views here.
def comments(request, post_id):
    """A view for a comment section"""
    """ Move logic into the view you want comments for. """
    comments = Comment.objects.filter(post=post_id).order_by('-date_added')

    context = {'comments': comments}
    return render(request, 'comments/comments.html', context)

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

