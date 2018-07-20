from django.urls import path
from . import views


app_name='InterfaceAuto'
urlpatterns=[
path('',views.index, name='index'),
]