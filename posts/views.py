# Django
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Utilities
from datetime import datetime

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]


def list_posts_direct(request):
    """ List existing posts."""
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - {timestamp}<i></i></small></p>
            <figure><img src="{picture}"/></figure>
        """.format(**post)) # desempaqueta todo el diccionario que hay en cada POST.
    return HttpResponse('<br>'.join(content))

@login_required
def list_posts_html(request):
    """ List existing posts."""
    # A render le paso la request, el html y un contexto (diccionario con datos)
    return render(request, 'posts/feed.html', {'posts': posts})

