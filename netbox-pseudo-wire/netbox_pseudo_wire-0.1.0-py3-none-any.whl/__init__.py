from extras.plugins import PluginConfig


class PseudowireConfig(PluginConfig):
    """
    This class defines attributes for the NetBox Pseudowire plugin.
    """

    name = "netbox_pseudo_wire"
    verbose_name = "Pseudowires"
    description = "BitCo bespoke plugin for Pseudowire management"
    version = "0.1"
    author = "Gabri Botha"
    author_email = "gabri.botha@bitco.co.za"
    base_url = "pseudowire"
    required_settings = []
    default_settings = {"loud": True}
    caching_config = {"*": None}


config = PseudowireConfig
