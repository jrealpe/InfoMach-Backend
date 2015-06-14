"""infomach URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from web.views import *
from rest_framework import routers, serializers, viewsets
from web.viewsets import *
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()

router.register(r'Profile', ProfileViewSet)
router.register(r'Contribution', ContributionViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
