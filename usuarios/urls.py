from django.contrib import admin
from django.urls import path
from .views import home_usuario, user_logout

urlpatterns = [
    path('', home_usuario, name='home'),
    path('logout/', user_logout, name='logout'),
    

]
