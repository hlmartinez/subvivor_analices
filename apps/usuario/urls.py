from django.conf.urls import url
from django.urls import path , include
from apps.usuario.views import ReistrarUsuario,resetpass
from apps.kmanalisis.views import homeview
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', LoginView.as_view(), name="login_url"),
    path('logaut/',LogoutView.as_view(next_page='usuario:login_url'),name="logout"),
    path('register/',ReistrarUsuario.as_view(),name="registrar"),
    path('updatepass/',resetpass,name='resetpass'),
    path('home/', homeview, name="home"),
]
