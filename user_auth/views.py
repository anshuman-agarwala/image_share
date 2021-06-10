from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from .models import AppUser
from .forms import AppUserForm

def register(request):
    form = AppUserForm
    if request.method == 'POST':
        form = AppUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully.')
            return HttpResponseRedirect(reverse('user_auth:index'))
    return render(request, 'user_auth/register.html', {'form':form})

def get_user(request, pk):
    user = get_object_or_404(AppUser, pk=pk)
    return render(request, 'user_auth/user.html', {'user': user})

def mainpage(request):
    return render(request, 'user_auth/index.html')

# def login(request):
#     form = AuthenticationForm
#     if request.method == 'POST':
#         form = AuthenticationForm(request.POST)
#         if form.is_valid:
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, email=email, password=password)
#     return render(request, 'user_auth/login.html', {'form': form})

def profile(request):
    if request.user.is_authenticated:
        current_user_id = request.user.id
        current_user = AppUser.objects.get(pk=current_user_id)
        return render(request, 'user_auth/profile.html')
    else:
        return HttpResponseRedirect(reverse('user_auth:login'))
