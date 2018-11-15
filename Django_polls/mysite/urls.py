"""mysite URL Configuration

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
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

# from . import views as local_view
from rest_framework.authtoken import views as rest_framework_views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('RestApiExample.urls')),
                  path('index/', include('polls.urls')),
                  url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
