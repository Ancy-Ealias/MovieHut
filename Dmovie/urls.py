"""Dmovie URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Movieapp import views

from django.conf.urls import url,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name="home.html"),
    url(r'^$',views.index),
    path('index/',views.index,name="index.html"),
    path('search', views.search,name='search.html'),
    path('sign/',views.sign,name="signup.html"),
    path('adminpanel/', views.adminpanel,name='adminpanel.html'),
    path('addmovie', views.addmovie,name='moviedetails.html'),
    path('viewmovie/', views.viewmovie,name='viewmovie.html'),
    path('viewreviewrate', views.viewreviewrate,name='viewmovie.html'),
    path('editmovie', views.editmovie,name='edit.html'),
    path('edit', views.edit,name='edit.html'),
    path('deletemovie', views.deletemovie,name='delet.html'),

    path('userpanel/', views.userpanel,name='userpanel.html'),
    path('reguser', views.reguser,name='reguser.html'),
    path('moviereview/',views.moviereview,name='moviereview.html'),
    path('addreview', views.addreview,name='moviereview.html'),
    path('addrate', views.addrate,name='moviereview.html'),


    path('logout', views.logout,name='signup.html'),

    


]
urlpatterns += staticfiles_urlpatterns()



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)