# Django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# Forms
from posts.forms import PostForm
# Models
from posts.models import Post

class PostsFeedView(LoginRequiredMixin,ListView):
    """Return all published posts."""
    template_name = 'posts/feed.html'
    model= Post
    ordering = ('-created')
    paginate_by = 2
    context_object_name = 'posts'

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
            return redirect('posts:feed')
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