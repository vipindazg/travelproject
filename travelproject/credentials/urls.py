from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login',views.login,name='login'),
    path('demologin', views.demologin, name='demologin'),
    path('demoregistration', views.demoregistration, name='demoregistration'),
    path('logout',views.logout,name='logout')

]
