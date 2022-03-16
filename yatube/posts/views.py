from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Post, Group

NUM_TITLE = 10


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, NUM_TITLE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'posts/index.html', context)


@login_required
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:NUM_TITLE]
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, 'posts/group_list.html', context)


@login_required
def profile(request, username):
    count = Post.objects.filter(author__username=username).count()
    post_list = Post.objects.filter(author__username=username)
    paginator = Paginator(post_list, NUM_TITLE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'count': count,
        'author': username,
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)


@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    author = post.author
    count = Post.objects.filter(author=author).count()
    context = {
        'post': post,
        'author': author,
        'count': count
    }
    return render(request, 'posts/post_detail.html', context)
