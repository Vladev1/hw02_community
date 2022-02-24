from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    state = 10
    posts = Post.objects.order_by('-pub_date')[:state]
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    state = 10
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:state]
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, 'posts/group_list.html', context)
# Create your views here.
