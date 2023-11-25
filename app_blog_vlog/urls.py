from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('addpost/', views.add_post, name = 'add_post'),
    path('edit_delete/', views.edit_delete, name = 'edit_delete'),
    path('register/', views.register, name = 'register'),
    path('login/', views.user_login, name='login'),
    path('post/<int:post_id>/', views.show_post, name='show_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]