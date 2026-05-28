from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from core.constants import POSTS_BY_PAGE

from .models import Category, Post


def get_published_posts(post_manager=None):
    if post_manager is None:
        post_manager = Post.objects

    return post_manager.select_related(
        'category',
        'location',
        'author'
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )


def index(request):
    posts = get_published_posts()[:POSTS_BY_PAGE]

    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(
        get_published_posts(),
        pk=post_id
    )

    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )

    posts = get_published_posts(category.posts)

    return render(
        request,
        'blog/category.html',
        {
            'category': category,
            'posts': posts,
        }
    )