from django.urls import path
from . import views


app_name='InterfaceAuto'
urlpatterns=[
path('',views.login, name='login'),
path('index/',views.index, name='index'),
path('signup/',views.signup, name='signup'),
]