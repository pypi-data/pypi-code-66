from django.contrib import admin
from .models import Setting
from .models import Slide




@admin.register(Setting)
class Setting (admin.ModelAdmin):
    class Media:

        js = ('//ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',
              'static/test_connection.js',)
        css = {
            'all': ('static/test_connection.css',)
        }




