""" Users views"""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import  login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile
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


class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save from data"""
        form.save()
        return super().form_valid(form)


class UpdateProfileView(UpdateView):
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile"""
        return self.request.user.profile

    def get_success_url(self):
        """"Return to user's profile."""
        username = self.object.user.username # self.object es el profile que ya se trajo en get_object
        return reverse('users:detail', kwargs={'username': username})

class LoginView(auth_views.LoginView):
    """Login view."""
    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LoginView):
    """Logout view."""
    template_name = 'users/login.html'
