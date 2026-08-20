from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.Registerview.as_view(), name='register'),
    path('login/', views.Loginview.as_view(), name="login"),
    path('logout/',views.LogoutView.as_view(),name="logout"),
    path('profile/',views.ProfileUpdateView.as_view(),name="profile_edit"),
]
