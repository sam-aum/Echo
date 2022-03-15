from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('signin/', views.SignIn.as_view(), name="sign_in"),
    path('ekkos/', views.EkkoList.as_view(), name="ekko_list"),
    path('ekkos/new/', views.EkkoCreate.as_view(), name="ekko_create"),
    path('ekkos/<int:pk>/', views.EkkoDetail.as_view(), name="ekko_detail"),
    path('ekkos/<int:pk>/update',views.EkkoUpdate.as_view(), name="ekko_update"),
    path('ekkos/<int:pk>/delete',views.EkkoDelete.as_view(), name="ekko_delete"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('ekkos/<int:pk>/comments/new/', views.CommentCreate.as_view(), name="comment_create"),
    # path('ekkos/<int:pk>/comment',views.EkkoComment.as_view(), name="ekko_comment"),
]