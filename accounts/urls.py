from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('user/<str:username>/', views.view_user_profile, name='user_profile'),
    path('edit/', views.edit_profile, name='edit_profile'),

]
