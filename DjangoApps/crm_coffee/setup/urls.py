from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from core.views import index, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name="about")
]
