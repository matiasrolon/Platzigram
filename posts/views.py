# Django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Forms
from posts.forms import PostForm
# Models
from posts.models import Post

"""
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
]"""


def list_posts_direct(request):
    """ List existing posts."""
    content = []
    posts = Post.objects.all().order_by('-created')
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
    posts = Post.objects.all().order_by('-created')
    # A render le paso la request, el html y un contexto (diccionario con datos)
    return render(request, 'posts/feed.html', {'posts': posts})

@login_required
def create_post(request):
    """Create new post view"""
    if request.method == 'POST':
        # como mandamos una foto, hay que pasarle tambien FILES.
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # esto automaticamente nos guarda el Post.
            return redirect('feed')
    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )