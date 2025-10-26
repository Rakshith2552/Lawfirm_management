from django.urls import path
from btrapp import views

urlpatterns = [
    path('',views.register,name='register'),
    path('login',views.user_login,name='login'),
    path('home',views.home_page,name='home'),
    path('logout',views.user_logout,name='logout'),
    path('profile',views.Profile,name='profile'),
    path('update',views.Update,name='update')
]
