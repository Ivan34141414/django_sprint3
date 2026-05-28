from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from core.constants import POSTS_BY_PAGE

from .models import Category, Post


def index(request):
    posts = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )[:POSTS_BY_PAGE]

    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(
        Post,
        pk=post_id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )

    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )

    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    )

    return render(
        request,
        'blog/category.html',
        {
            'category': category,
            'posts': posts,
        }
    )