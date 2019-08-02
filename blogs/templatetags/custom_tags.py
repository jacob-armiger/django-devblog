from django.contrib.auth.models import User
from comments.models import Comment
from django import template

register = template.Library()

# Used to get all staff users
@register.simple_tag
def get_staff_users():
    staff_users = User.objects.filter(is_staff=True)
    return staff_users
