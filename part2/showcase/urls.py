from django.urls import path
from . import views


urlpatterns = [
    path("taiwind_components/", views.components_view, name="tailwind_showcase"),
    path("alpineJS_vs_VanilaJa/", views.javascripts_view.as_view(), name="javascripts_showcases"),
    path("htmx/showcase", views.htmx_demo_view, name="htmx_showcase"),
    path("htmx/showcase/items/add", views.htmx_item_add_view, name="htmx_showcase_add"),
    path("htmx/showcase/items/<int:pk>/delete", views.htmx_item_delete_view, name="htmx_showcase_delete"),
    path("htmx/showcase/items/<int:pk>/edit", views.htmx_item_edit_form_view, name="demo_item_edit_form"),
    path("htmx/showcase/items/<int:pk>/update", views.htmx_item_update_view, name="demo_item_update"),
]