from django.shortcuts import render
from . import services
from .models import Post

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


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
