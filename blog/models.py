from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render, get_object_or_404


# My Manager
# class PostsByAuthorManager(models.Manager):
#     def get_queryset(self, *args, **kwargs):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         # return Post.objects.filter(author=user).order_by('-date_posted')
#         return super().get_queryset().filter(author=user).order_by('-date_posted')


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    # post_by_author = PostsByAuthorManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
