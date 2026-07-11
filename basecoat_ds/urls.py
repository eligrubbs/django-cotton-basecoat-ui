from django.urls import path
from django.views.generic import TemplateView

from .data import (
    APP_NAME,
    SHOWCASE_URL_PREFIX,
    SHOWCASE_URL_NAME,
    COMPONENTS_INFO
)


class BasecoatShowcaseTemplateView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[APP_NAME] = {
            "app_name": APP_NAME,
            "base_url": f"{APP_NAME}:{SHOWCASE_URL_NAME}",
            "components": COMPONENTS_INFO,
        }
        return context


app_name=APP_NAME

urlpatterns = (
    [
        path(f"{SHOWCASE_URL_PREFIX}/", BasecoatShowcaseTemplateView.as_view(template_name="showcase/index.html"), name=SHOWCASE_URL_NAME),
    ]
    +
    [
        path(
            f"{SHOWCASE_URL_PREFIX}/{x.url_path_prefix}",
            BasecoatShowcaseTemplateView.as_view(template_name=x.showcase_template_path_str),
            name=x.url_name,
        )
        for _, x in COMPONENTS_INFO.items()
    ]
)
