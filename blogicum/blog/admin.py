from django.contrib import admin

from .models import Category, Location, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author',
        'category',
        'pub_date',
        'location',
        'is_published',
        'created_at',
    )
    list_display_links = ('title',)
    list_editable = ('category', 'is_published', 'location')
    search_fields = ('title', 'text')
    list_filter = ('is_published', 'category', 'location', 'created_at')
    empty_value_display = '-пусто-'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'slug',
        'is_published',
        'created_at',
    )
    list_editable = ('slug', 'is_published')
    search_fields = ('title',)
    list_filter = ('is_published', 'created_at')
    empty_value_display = '-пусто-'


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'is_published',
        'created_at',
    )
    list_editable = ('is_published',)
    search_fields = ('name',)
    list_filter = ('is_published', 'created_at')
    empty_value_display = '-пусто-'