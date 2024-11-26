from django.urls import path
from . import views

from .views import home, about_view 
from django.contrib.auth import views as auth_views

urlpatterns = [
      path('home/', home, name='home'),
    path('about/', about_view, name='about'), 
     
     path('', views.post_list, name='post_list'),  # Home page
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),  # Use the custom logout view
    path('category/<slug:slug>/', views.category_posts_view, name='category_posts'),  # Category posts
     path('post/<int:id>/', views.post_detail, name='post_detail'),
]


