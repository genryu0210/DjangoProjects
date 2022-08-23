from django.contrib import admin
from django.urls import path
from .views import TodoList, TodoDetail, TodoCreate, TodoDelete, TodoUpdate

urlpatterns = [
    path('list/', TodoList.as_view(), name='list'),
    path('detail/<pk>', TodoDetail.as_view(), name='detail'),
    path('create/', TodoCreate.as_view(), name='create'),
    path('delete/<pk>', TodoDelete.as_view(), name='delete'),
    path('update/<pk>', TodoUpdate.as_view(), name='update')
]
