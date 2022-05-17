"""rareV2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework import routers
from rareV2Api.views.post import PostView
from django.conf.urls import include
from django.urls import path

# The trailing_slash=False tells the router to accept /gametypes instead of /gametypes/
router = routers.DefaultRouter(trailing_slash=False)

router.register(r'posts', PostView, 'posts')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]