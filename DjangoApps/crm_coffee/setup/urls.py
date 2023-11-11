from os import name
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from core.views import index, about
from userprofile.views import signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name="about"),
    path('signup/', signup, name="signup"),
    path('login/', views.LoginView.as_view(template_name='userprofile'), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout")
]
