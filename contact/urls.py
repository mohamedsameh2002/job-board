from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.send_masseg,name='contact'),
    path('applys/', views.applys,name='applys'),
    path('details/<str:slug>/', views.apply_details,name='applys/details'),
    path('cv/<str:slug>/', views.cv,name='cv'),
    path('delete/<str:slug>/', views.delete_apply,name='delete'),

]
