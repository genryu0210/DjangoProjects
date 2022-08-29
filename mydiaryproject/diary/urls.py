"""mydiaryproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import IndexView, DiaryCreateView, DiaryCreateCompleteView, \
                   DiaryListView, DiaryDetailView, DiaryUpdateView, DiaryDeleteView


app_name = 'diary'
urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('diary/create/', DiaryCreateView.as_view(), name="diary_create"),
    path('diary/create/complete/', DiaryCreateCompleteView.as_view(), name='diary_create_complete'),
    path('diary/list/', DiaryListView.as_view(), name='diary_list'),
    path('diary/deatail/<uuid:pk>/', DiaryDetailView.as_view(), name='diary_detail'),
    path('diary/update/<uuid:pk>/', DiaryUpdateView.as_view(), name='diary_update'),
    path('diary/delete/<uuid:pk>/', DiaryDeleteView.as_view(), name='diary_delete'),

]