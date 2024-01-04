from django.urls import path
from magasin import views

urlpatterns = [
    path('magasin/', views.inv_magasin, name='inv_magasin'),
]