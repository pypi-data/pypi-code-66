from django.db import models


class Pseudowire(models.Model):
    """
    A database table representing pseudowires and the tunnel each represents.
    """

    name = models.CharField(max_length=50)
    tunnel = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]
        app_label = "netbox_pseudo_wire"

    def __str__(self):
        return self.name
