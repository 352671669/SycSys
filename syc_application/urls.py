"""wechat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from .views import excute, get_business, get_hosts, excute_script, get_scripts, history, get_histories

urlpatterns = [
    url('^admin/$', admin.site.urls),
    url('^$', excute),
    url('^get_business$', get_business),
    url('^get_hosts$', get_hosts),
    url('^excute_script$', excute_script),
    url('^get_scripts$', get_scripts),
    url('^history/$', history),
    url('^get_histories$', get_histories),
]
