from django.conf import settings
from django.shortcuts import get_object_or_404, render

from .models import Group, Post

limit = settings.MAX_POSTS

def index(request):
    posts = Post.objects.select_related('group', 'author')[:limit]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:limit]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
