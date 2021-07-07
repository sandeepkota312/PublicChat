from django.urls import path, include
from . import views

app_name = "main"

urlpatterns = [
    # path("", views.homepage, name="homepage"),

    path("", views.register_request, name="register"),
    path('home/', views.home, name='home'),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
    path('<str:room>/', views.room, name='room'),
    path('home/checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),

]

