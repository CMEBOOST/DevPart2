from django.urls import path
from . import views


urlpatterns = [
    path("taiwind_components/", views.components_view, name="tailwind_showcase"),
]