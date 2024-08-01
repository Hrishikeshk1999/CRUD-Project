from django.urls import path
from . import views



urlpatterns = [
    path('',views.home),
    path('list',views.orders),
    path('add', views.buy),
    path('savecam', views.savecam),
    path('delete/<rid>', views.vanhish),
    path('edit/<rid>', views.editorder)
]
