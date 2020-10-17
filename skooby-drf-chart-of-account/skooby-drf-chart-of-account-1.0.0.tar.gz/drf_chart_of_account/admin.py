"""Chart of Accounts Layers Models Django Admin Classes."""
from django.contrib import admin
from .models import (LayerOneModel, LayerTwoModel, LayerThreeModel,
                     LayerFourModel, LayerFiveModel)


# Register your models here.
class DRFChartOfAccountBaseAdmin(admin.ModelAdmin):
    """Base admin class for all layer models admin classes."""

    list_display = ['id', 'name', 'ref_no', 'is_active']
    search_fields = ['ref_no', 'name']


admin.site.register(LayerOneModel, DRFChartOfAccountBaseAdmin)
admin.site.register(LayerTwoModel, DRFChartOfAccountBaseAdmin)
admin.site.register(LayerThreeModel, DRFChartOfAccountBaseAdmin)
admin.site.register(LayerFourModel, DRFChartOfAccountBaseAdmin)
admin.site.register(LayerFiveModel, DRFChartOfAccountBaseAdmin)
