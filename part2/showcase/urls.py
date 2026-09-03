from django.urls import path
from . import views


urlpatterns = [
    path("taiwind_components/", views.components_view, name="tailwind_showcase"),
    path("alpineJS_vs_VanilaJa", views.javascripts_view.as_view(), name="javascripts_showcases"),
]