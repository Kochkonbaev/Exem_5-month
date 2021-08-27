from django.urls import path

from . import views


urlpatterns = [
    path('', views.LoginView.as_view(), name='dashboard'),
    path('register/', views.RegisterView.as_view(), name='registration'),
    path('logout/', views.logout_view, name='logout'),
]