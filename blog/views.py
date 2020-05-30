from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from . import services
from .models import Post, Comment
from django.contrib.auth.models import User
from .forms import CommentForm


'''
# dummy data
posts = [
    {
        'author': 'Ilf and Petrov',
        'title': '12 chears',
        'date_posted': '12 August 2018',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc tempor gravida porta. Morbi eu pretium erat, vitae ullamcorper elit. Fusce et magna ut felis maximus gravida. Curabitur lacinia quam quis tempor tristique. Donec vehicula, urna ut pretium tempor, ipsum arcu pretium tellus, id sagittis lacus eros vel est. Aliquam eget ullamcorper enim. Aliquam fringilla dui eu ullamcorper iaculis. Suspendisse porta purus sodales diam eleifend, vel tristique quam condimentum. Proin et luctus dolor. Nunc aliquam augue ac erat fermentum pharetra. Morbi dapibus odio at purus rutrum rhoncus. Phasellus hendrerit erat et augue sodales, ac aliquam orci suscipit. Praesent dictum mi ex, ac ullamcorper neque lobortis aliquet. Proin tempus massa a turpis faucibus fringilla.'
    },

    {
        'author': 'Gul Wern',
        'title': '12 000 lie under the water',
        'date_posted': '22 August 2019',
         'content': 'Mauris rutrum convallis ex a maximus. Etiam ac dolor nec tortor iaculis egestas. Praesent viverra magna diam, non iaculis odio pulvinar lacinia. Cras elementum lacus in tellus cursus, ac sodales elit viverra. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec egestas sed lacus ac euismod. Maecenas vestibulum libero in est mollis luctus. Etiam fringilla lorem eu eros dignissim luctus. Nullam ac orci tellus. Integer eu nisl diam. Vivamus lacinia ante vitae consequat hendrerit. In lobortis viverra pulvinar. Mauris non fringilla lorem, at accumsan velit.'
    },

]'''


def home(request):
    posts = services.get_all_posts()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # app/model_typeview.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # app/model_typeview.html
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

    # # use My own Manager - post_by_author
    # def get_queryset(self):
    #     username = self.kwargs.get('username')
    #     return Post.post_by_author.all(username)

class PostDetailView(DetailView):
    model = Post
    # it will look template in 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # Без указания автора не знает кто автор при сохранении
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Сейчас каждый залогинившийся может редактировать любой пост, в том числе и не свой. Надо проверить чтобы был автором
    # для этого UserPassesTestMixin
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog-home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
