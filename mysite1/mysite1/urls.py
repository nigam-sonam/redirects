"""mysite1 URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from url_resolver.views import index,bye,login,logout
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/',index,name="index"),
    url(r'^bye/',bye,name="bye"),
    url(r'^login/',login,name="login"),
    url(r'^logout/',logout,name="logout"),
    #url(r'^[a-z]\d/',login,name="login"),
    #url(r'^[0-9]+/',logout,name="logout"),

    #url(r'^.*/$',RedirectView.as_view(url='/home/')),
    #url(r'^bye/',RedirectView.as_view(url='/home/')),
]
