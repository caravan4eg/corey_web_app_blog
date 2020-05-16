# services.py
from .models import Post


def get_all_posts():
    """
    Returns all posts from DB
    Example here: https://apirobot.me/posts/where-to-put-business-logic-in-django
    """
    return Post.objects.all()
