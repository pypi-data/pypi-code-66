from django.urls import path

# import netbox_pseudo_wire.views as views
from .views import ListPseudowiresView, RandomPseudowireView, PseudowireView

# Define a list of URL patterns to be imported by NetBox. Each pattern maps a URL to
# a specific view so that it can be accessed by users.
urlpatterns = (
    path("list/", ListPseudowiresView.as_view(), name="list_pseudowires"),
    path("random/", RandomPseudowireView.as_view(), name="random_pseudowire"),
    path("<str:name>/", PseudowireView.as_view(), name="pseudowire"),
)
