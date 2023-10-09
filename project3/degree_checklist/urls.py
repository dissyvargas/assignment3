from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #path('', views.welcome_view,
    #name='welcome_view'),
    path('courses/', views.course_list,
        name='course_list'),
]   