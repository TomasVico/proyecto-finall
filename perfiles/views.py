from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from .models import UserProfile
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from blog.urls import *
from .models import  Message


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'perfiles/profile.html', {'user_profile': user_profile})

def registration_success(request):
    return render(request, 'registration/registration_success.html')

from django.contrib.auth import views as auth_views

class CustomLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('article_list')







