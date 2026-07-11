from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path("__showcase__/", TemplateView.as_view(template_name="showcase/index.html"), name="basecoat_showcase"),
]
