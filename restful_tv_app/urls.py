"""restful_tv_app Configuration

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
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.addshow),
    # path('shows/create', views.createshow),
    path('shows/<int:Show_id>/viewshow', views.specificshow),
    path('shows/<int:Show_id>/edit', views.edit),
    path('shows/<int:Show_id>/update', views.update),
    path('shows/<int:Show_id>/destroy', views.destroy),
]
