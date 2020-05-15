from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        'author': 'Ilf and Petrov',
        'title': '12 chears',
        'date_posted': '12 August 2018',
    },

    {
        'author': 'Gul Wern',
        'title': '12 000 lie under the water',
        'date_posted': '22 August 2019',
    },

]


def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
