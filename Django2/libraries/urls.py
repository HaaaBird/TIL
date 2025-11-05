from django.urls import path, include
from . import views

app_name = 'libraries'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_author/', views.create_author, name='create_author'),
    path('accounts/', include('accounts.urls')),
]
