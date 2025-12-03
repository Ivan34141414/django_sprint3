from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    # Надо исправить:
    # Русифицируем раздел в админке (Требование ТЗ).
    verbose_name = 'Блог'
