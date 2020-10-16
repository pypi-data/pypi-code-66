from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models import CMSPlugin
from .models import *
from django.conf import settings
from django.shortcuts import render
from pma_python import core, control
import requests
from .models import Setting
from .models import Slide
from django import template



class Slides(CMSPluginBase):

    # form = SlidesAdminForm
    name = 'Pathomation slide'
    model = Slide
    render_template = "slides/_slides.html"
    text_enabled = True
    change_form_template = "slides/_custom.html"
    cache= True



    def render(self, context, instance, placeholder):


        context.update({
            'instance': instance,
            'slides': Slide.objects.all(),
            'placeholder': placeholder,

        })

        return context

    def render_change_form(self, request, context, *args, **kwargs):

        self.change_form_template = 'slides/_custom.html'
        extra = {'link': Slide.link, 'user': Slide.user, 'password': Slide.password, 'sessionID': Slide.sessionID, 'folder': Slide.folder}
        context.update(extra)
        return super(Slides, self).render_change_form(request, context, *args, **kwargs)



    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['osm_data'] = self.get_dynamic_info()
        return super(Slides, self).change_view(
            request, object_id, form_url, extra_context=extra_context)


    def icon_src(self,instance):
        return settings.STATIC_URL + 'pathomation/images/pathomation.png'

    def icon_alt(self,instance):
        return u'Slide: %s' %instance



plugin_pool.register_plugin(Slides)

