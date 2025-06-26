from django.urls import path
from . import views


urlpatterns = [
   # path('car/',views.car__list),
    path('table/',views.table),
    path('index/',views.index),
    #path('carlist/',views.car_list, name='car_list',),
   #path('date-time/', views.date, name='date'),
   #path('carmodels/<str:model>/', views.car, name='car'),#url with parameters
]
