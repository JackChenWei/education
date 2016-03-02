"""education URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin

from smart import views as smart_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^accounts/', include('users.urls')),
    #url(r'^$', smart_views.index, name='index'),
    #url(r'^$', smart_views.login, name='login'),
    url(r'^login/', smart_views.login),
    url(r'^index/', smart_views.index),
    url(r'^coordinative_project_manage/', smart_views.coordinative_project_manage),
    url(r'^system_user_manage_show/', smart_views.system_user_manage_show),
    url(r'^system_user_manage_delete/', smart_views.system_user_manage_delete),
    url(r'^system_user_manage_add/', smart_views.system_user_manage_add),
]
