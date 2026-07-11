"""
Internal data for the component library
"""
from typing import Optional
from dataclasses import dataclass


SHOWCASE_URL_PREFIX="__showcase__"
"""What to put before all showcase URLS."""
SHOWCASE_URL_NAME="basecoat_showcase"
"""Name for index page of basecoat showcase."""
SHOWCASE_TEMPLATES_COMMON_PATH_PREFIX="showcase/components"
"""Common path in `templates` where to find each components showcase page."""

APP_NAME="basecoat_ds"
"""Django app name."""


@dataclass
class ComponentInfo:
    name: str
    """Name displayed on showcase page."""
    url_path_prefix: str
    """what appears in the url for this view."""
    url_name: str
    """how django internally reverses urls to this view."""
    showcase_template_path_str: str
    """what showcase template to render for this view."""
    url_path: Optional[str] = None
    """We will set this for you!"""

    def __post_init__(self):
        self.url_path = f"{APP_NAME}:{self.url_name}"


COMPONENTS_INFO = {
    "kbd": ComponentInfo(
        name="Kbd",
        url_path_prefix="kbd",
        url_name="kbd",
        showcase_template_path_str=f"{SHOWCASE_TEMPLATES_COMMON_PATH_PREFIX}/kbd.html"
    )
}
