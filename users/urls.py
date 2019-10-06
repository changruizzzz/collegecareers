from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('loginUser/', views.login_user, name='login-user'),
    path('signupUser/', views.signup_user, name='signup-user'),
]
