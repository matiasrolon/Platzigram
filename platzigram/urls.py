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
from django.urls import path
from platzigram import views as local_views
from posts import views as posts_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # agrego la URL junto con el método (vista) que responderá por la misma.
    path('hello-world/',local_views.hello_world, name='hello_world'),
    path('print-numbers/',local_views.non_sorted_numbers, name='print-numbers'),
    path('sorted-numbers/',local_views.sorted_numbers, name='sorted-numbers'),
    path('hi/<str:name>/<int:age>', local_views.say_hi, name='hi-name'),

    path('posts-direct/',posts_views.list_posts_direct,name='posts-direct'),
    path('posts/',posts_views.list_posts_html, name='feed'),

    path('users/login/',users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
    path('users/signup/', users_views.signup, name='signup'),
    path('users/me/profile', users_views.update_profile, name='update_profile')
  # Para que busque las imagenes localmente y no las detecte como una url normal del sitio.
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)