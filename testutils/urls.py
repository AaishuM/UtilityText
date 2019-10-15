"""testutils URL Configuration

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
from django.contrib import admin
from django.urls import path
from . import view


#code for navigagtion
#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('',view.index,name='index'),
#    path('about',view.about,name='about')
#]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.index,name='index'),
    path('analyze',view.analyze,name='analyze'),
    #path('capitalizefirst',view.capfirst,name='capfirst'),
    #path('newlineremove',view.newlineremove,name='newlineremove'),
    #path('spaceremove',view.spaceremove,name='spaceremove'),
    #path('charcount',view.charcount,name='charcount'),

]