from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('signin/', views.SignIn.as_view(), name="sign_in"),
    path('ekkos/', views.EkkoList.as_view(), name="ekko_list"),
    path('ekkos/new/', views.EkkoCreate.as_view(), name="ekko_create"),
    # path('artists/<int:pk>/', views.ArtistDetail.as_view(), name="artist_detail"),
        # this can be comments
    path('ekkos/<int:pk>/update',views.EkkoUpdate.as_view(), name="ekko_update"),
    path('ekkos/<int:pk>/delete',views.EkkoDelete.as_view(), name="ekko_delete"),
]