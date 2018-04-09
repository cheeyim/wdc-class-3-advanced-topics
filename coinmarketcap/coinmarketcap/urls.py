"""coinmarketcap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from cryptocoins import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.login, name='login'),
    path('accounts/logout/', auth_views.logout, {'next_page': '/'}, name='logout'),

    # path('', views.index, name='cryptocurrencies-table'),
    path('', views.IndexPageView.as_view(), name='cryptocurrencies-table'),
    # path('create/', views.create_new_cryptocurrency, name='cryptocurrencies-create'),
    path('create/', views.CreateCryptoView.as_view(),
        name='cryptocurrencies-create'),

    path('favorite/', views.favorite, name='favorite'),
]
