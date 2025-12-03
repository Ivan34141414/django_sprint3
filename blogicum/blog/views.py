from django.shortcuts import get_object_or_404, render
# Можно лучше:
# При использовании часового пояса отличного от UTC, будет
# выскакивать warning, поэтому лучше заменить время на это
# from django.utils import timezone и использовать timezone вместо datetime.
from django.utils.timezone import now

from core.constants import POSTS_BY_PAGE
from .models import Category, Post


# Надо исправить:
# Вызов now() на уровне модуля недопустим.
# POSTS = Post.objects.filter(..., pub_date__lt=now(),) Так делать нельзя.
# NOW = now()

# Надо исправить:
# Выносим повторяющийся код в функцию.
# Можно лучше:
# Можно рассказать про менеджеры моделей и queryset и вынести туда.
def filtered_select_posts(posts):
    # Можно лучше: Тут может быть queryset, а может быть Post.objects,
    # лучше так, как тут, но нужно рассказать про эту версию.
    # Можно лучше:
    # Студенты проходили в теории оптимизацию запросов, напоминаем им об этом.
    # https://django.fun/tutorials/select_related-i-prefetch_related-v-django/
    return posts.select_related(
        'author', 'category', 'location'
    ).filter(
        is_published=True,
        pub_date__lt=now(),
        category__is_published=True,
    )


def index(request):
    post_list = filtered_select_posts(Post.objects)[:POSTS_BY_PAGE]
    # Надо исправить:
    # Тут чаще всего есть и сортировка и срез 5 постов, убираем сортировку
    # в модель, а срез в константу.
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    # Надо исправить:
    # Тут студенты часто в get_object_or_404 вставляют еще и filter,
    # объясняем им, что шорткат может принимать так же несколько аргументов.
    # Надо исправить:
    # ВНИМАНИЕ! Студенты любят писать тут .values(), он тут не нужен,
    # обсуждение тут https://app.pachca.com/chats?thread_id=1960571
    post = get_object_or_404(
        filtered_select_posts(Post.objects),
        id=post_id
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True
    )
    # Можно лучше:
    # Напоминаем, что достать посты можно из категории, используя related_name.
    post_list = filtered_select_posts(category.posts)
    # Надо исправить:
    # Фильтрация по категории должна происходить по объекту, а не по слаг.
    return render(request, 'blog/category.html', {
        'post_list': post_list,
        'category': category
    })
