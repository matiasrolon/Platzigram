""" Users views"""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import  login_required
from django.contrib.auth import authenticate, login, logout
import pdb

# Models
from django.contrib.auth.models import User
from users.models import Profile

#Exception
from django.db.utils import IntegrityError

def update_profile(request):
    """Update a user's profile views"""
    return render(request, 'users/update_profile.html')

def login_view(request):
    """Login view"""
    if request.method == 'POST':
        print('*'*10)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username , password= password)
        if user:
            login(request, user)
            return redirect('feed')
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
    return redirect('login')

def signup(request):
    """Sign up view."""
    if request.method == "POST":
        username = request.POST['username']
        passwd = request.POST['password']
        passwd_confirmation = request.POST['password_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error':'Password confirmation does not match'})

        try:
            user = User.objects.create_user(username=username,password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html',{'error':'Username is already in user'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']

        profile = Profile(user=user)
        profile.save() # Tambien podes salvarlos como los usuarios: Profile.objects.create()

        return redirect('login')

    return render(request, 'users/signup.html')