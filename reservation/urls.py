from django.urls import path
from. import views

app_name='reservation'
urlpatterns = [
    path('', views.resrve_table,name='reserve_table'),
]