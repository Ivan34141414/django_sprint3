from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls', namespace='pages')),
    # Можно лучше:
    # Объяснить, что чтобы случайно не затереть стандартные урлы - наши
    # нужно перенести в конец

    # Надо исправить:
    # Урлы приложения blog подключаются именно таким образом и никак иначе.
    path('', include('blog.urls', namespace='blog')),
]
