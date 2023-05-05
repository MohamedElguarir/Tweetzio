from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('resetpassword/', views.passwordreset, name='resetpassword'),
    path('analyse/', views.analyse, name='analyse'),
    path('results/', views.result, name='results'),

]

