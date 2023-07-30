from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name = "starting_point"),
    path("home", views.home_page, name = "home_page"),
    path("signup", views.sign_up, name = "sign_up"),

]