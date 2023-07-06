from django.urls import path, include
from . import views
from . import api

urlpatterns = [
    path('', views.job_list,name='job_list'),
    path('add/',views.add_job,name='add_job'),
    path('edit/<str:slug>/', views.edit_job,name='edit_job'),
    path('delete/<str:slug>/', views.delet_job,name='delete_job'),
    path('<str:slug>/', views.job_details,name='job_details'),
    #API
    path('api/jobs/',api.jobs_list_api,name='jobs_list_api'),
    path('api/jobs/<int:id>/',api.job_detal_api,name='job_detal_api'),
    #class based view
    path('api/v2/jobs/',api.JobListApi.as_view(),name='jobs_list_api_vs'),
    path('api/v2/jobs/<int:id>/',api.JobDetaleApi.as_view(),name='job_detal_api_v2'),


]
