from django.contrib import admin
from django.urls import path
from diaryapp import views

app_name = "diaryapp"

urlpatterns = [
    path("",views.index,name="index"),
    path("detail/<int:id>/",views.detail,name="detail"),
    path("update/",views.update,name="update"),
]
