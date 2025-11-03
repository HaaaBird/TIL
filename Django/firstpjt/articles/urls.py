# articles/urls.py

from django.urls import path
from . import views
app_name = 'articles'
urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update', views.update, name='update'),
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('', views.index, name='index'),
#     path('new/', views.new, name="new"),
    path('create/', views.create, name='create'),

]