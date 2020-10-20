from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from .models import Pseudowire


class ListPseudowiresView(View):
    """
    List all pseudowire in the database.
    """

    def get(self, request):
        pseudowires = Pseudowire.objects.all()
        return render(
            request,
            "netbox_pseudo_wire/pseudowire_list.html",
            {
                "pseudowires": pseudowires,
            },
        )


class PseudowireView(View):
    """
    Display a single pseudowire, identified by name in the URL.
    """

    def get(self, request, name):
        pseudowire = get_object_or_404(Pseudowire.objects.filter(name=name))
        return render(
            request,
            "netbox_pseudo_wire/pseudowire.html",
            {
                "pseudowire": pseudowire,
            },
        )


class RandomPseudowireView(View):
    """
    Display a randomly-selected pseudowire.
    """

    def get(self, request):
        pseudowire = Pseudowire.objects.order_by("?").first()
        return render(
            request,
            "netbox_pseudo_wire/pseudowire.html",
            {
                "pseudowire": pseudowire,
            },
        )
