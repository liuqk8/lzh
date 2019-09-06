"""lzhcn URL Configuration

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
# from django.contrib import admin
from django.conf.urls import url
from django.views.static import serve
from . import settings
from django.urls import path, include
from django.views.generic import TemplateView
import xadmin
from users.views import UserLoginView

urlpatterns = [
    path('admin/', xadmin.site.urls),
    path('', include('lzapps.center.urls',namespace='center')),
    # path("", TemplateView.as_view(template_name="peixun/index.html"), name="index"),
    path('ueditor/', include('DjangoUeditor.urls')),
    path("login/", UserLoginView.as_view(), name='login'),
    url(r'^uploads/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
]
