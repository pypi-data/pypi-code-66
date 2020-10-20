from django.contrib import admin

from .models import Pseudowire


@admin.register(Pseudowire)
class PseudowireAdmin(admin.ModelAdmin):
    """
    This class defines a Django administrative view for the Pseudowire model. The register()
    decorator above registers the view with NetBox's admin site object.
    """

    list_display = ("name", "tunnel")
