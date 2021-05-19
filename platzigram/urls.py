"""platzigram URL Configuration"""
'''
The import order in a Django project is:
1.- Standard library imports.
2.- Imports from core Django.
3.- Imports from third-party apps including those unrelated to Django.
4.- Imports from the apps that you created as part of your Django project
'''
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # URLs de la fase de prueba
    # agrego la URL junto con el método (vista) que responderá por la misma.
    # path('hello-world/', local_views.hello_world, name='hello_world'),
    # path('print-numbers/', local_views.non_sorted_numbers, name='print-numbers'),
    # path('sorted-numbers/', local_views.sorted_numbers, name='sorted-numbers'),
    # path('hi/<str:name>/<int:age>', local_views.say_hi, name='hi-name'),

    # posts
    path('', include(('posts.urls', 'posts'), namespace='posts')),
    # users
    path('users/', include(('users.urls', 'users'), namespace='users'))

  # Para que busque las imagenes localmente y no las detecte como una url normal del sitio.
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)