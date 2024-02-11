from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('registration/', views.register, name='reg'),
    path('login/', authViews.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', authViews.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile/', views.edit_profile, name='profile'),
    path('links/', views.LinksView.as_view(), name='links'),
]
