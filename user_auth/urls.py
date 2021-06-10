from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('', views.mainpage, name='index'),
    path('user/<int:pk>/', views.get_user, name='user'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='user_auth/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='user_auth:login')),
    path('profile/', views.profile, name='profile'),
]