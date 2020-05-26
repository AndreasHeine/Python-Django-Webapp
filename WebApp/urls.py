"""WebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.conf import settings

from Main.views import MainIndexView, MainAboutView, MainJsonDataView
from Blog.views import BlogIndexView

urlpatterns = [
    #Default:
    url(regex=r'^$', view=MainIndexView, kwargs=None, name=''),

    # Main-App:
    url(regex=r'^main$', view=MainIndexView, kwargs=None, name='main'),
    url(regex=r'^main/ajax/json$', view=MainJsonDataView, kwargs=None, name='main'),
    url(regex=r'^about$', view=MainAboutView, kwargs=None, name='about'),

    # Blog-App:
    url(regex=r'^blog$', view=BlogIndexView, kwargs=None, name='blog'),

    # Django-Admin:
    path('admin/', admin.site.urls),
]