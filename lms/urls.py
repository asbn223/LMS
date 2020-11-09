"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import index, sign_up, add_book, edit_book, delete_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', sign_up, name='sign-up'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/(?P<pk>\d+)$', edit_book, name='edit_book'),
    path('delete_book/(?P<pk>\d+)$', delete_book, name='delete_book'),
]