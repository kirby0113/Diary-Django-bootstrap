from django.contrib import admin
from django.urls import path
from diaryapp import views

app_name = "diaryapp"

urlpatterns = [
    path("",views.index)
]
