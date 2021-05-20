""" Users views"""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import  login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# Models
from django.contrib.auth.models import User
from posts.models import Post
# Forms
from users.forms import ProfileForm, SignupForm
#Exception
from django.db.utils import IntegrityError


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view"""
    template_name = 'users/detail.html'
    slug_field = 'username'         #
    slug_url_kwarg = 'username'     # es el parametro de la url
    queryset = User.objects.all()
    content_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user´s posts to context."""
        context = super().get_context_data(**kwargs)    # contexto que hubiera traido si no sobreescribieramos el metodo
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


def update_profile(request):
    """Update a user's profile views"""
    profile = request.user.profile
    print("el metodo es ",request.method)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()
            url = reverse('users:detail',kwargs={'username': request.user.username})
            return redirect(url)
    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile':profile,
            'user':request.user,
            'form': form
        }
    )


def login_view(request):
    """Login view"""
    if request.method == 'POST':
        print('*'*10)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username , password= password)
        if user:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(
                request,
                'users/login.html',
                {'error':'Invalid username or password'}
            )
    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    """Logout a user"""
    logout(request)
    return redirect('users:login')


def signup(request):
    """Sign up view."""
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()

    return render(
        request=request,
        template_name='users/signup.html',
        context={'form': form}
    )