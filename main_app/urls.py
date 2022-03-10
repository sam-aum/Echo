from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('signin/', views.SignIn.as_view(), name="sign_in"),
    path('ekkos/', views.EkkoList.as_view(), name="ekko_list"),
    path('ekkos/new/', views.EkkoCreate.as_view(), name="ekko_create"),

]