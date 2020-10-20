from extras.plugins import PluginTemplateExtension

from .models import Pseudowire


class SitePseudowireCount(PluginTemplateExtension):
    """
    Extend the DCIM site template to include content from this plugin. Specifically,
    we render the pseudowire_count.html template with some additional context to embed
    the current number of pseudowires on the right side of the page.
    """

    model = "dcim.site"

    def right_page(self):
        return self.render(
            "netbox_pseudo_wire/inc/pseudowire_count.html",
            extra_context={
                "pseudowire_count": Pseudowire.objects.count(),
            },
        )


# PluginTemplateExtension subclasses must be packaged into an iterable named
# template_extensions to be imported by NetBox.
template_extensions = [SitePseudowireCount]
