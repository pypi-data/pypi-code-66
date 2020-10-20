from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


# Declare a list of menu items to be added to NetBox's built-in naivgation menu
menu_items = (
    # Each PluginMenuItem instance renders a custom menu item. Each item may have zero or more buttons.
    PluginMenuItem(
        link="plugins:netbox_pseudo_wire:list_pseudowires",
        link_text="List all pseudowires",
        buttons=(
            PluginMenuButton(
                link="admin:netbox_pseudo_wire",
                title="Add a new pseudowire",
                icon_class="fa fa-plus",
                color=ButtonColorChoices.GREEN,
                permissions=["netbox_pseudo_wire.add_pseudowire"],
            ),
            PluginMenuButton(
                link="plugins:netbox_pseudo_wire:random_pseudowire",
                title="Random pseudowire",
                icon_class="fa fa-question",
                color=ButtonColorChoices.BLUE,
            ),
        )
        # permissions=[],
        # buttons=(
        #     # Add a default button which links to the random pseudowire view
        #     PluginMenuButton(
        #         link="plugins:netbox_pseudo_wire:random_pseudowire",
        #         title="Random pseudowire",
        #         icon_class="fa fa-question",
        #     ),
        #     # Add a green button which links to the admin view to add a new pseudowire. This
        #     # button will appear only if the user has the "add_pseudowires" permission.
        #     # PluginMenuButton(
        #     #     link="admin:netbox_pseudo_wire",
        #     #     title="Add a new pseudowire",
        #     #     icon_class="fa fa-plus",
        #     #     color=ButtonColorChoices.GREEN,
        #     #     permissions=["netbox_pseudo_wire.add_pseudowire"],
        #     # ),
        # ),
    ),
)
