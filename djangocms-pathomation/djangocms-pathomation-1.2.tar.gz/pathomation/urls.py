from django.urls import path
from . import cms_plugins as views

app_name = 'pathomation'
urlpatterns = [
    path('get_path', views.Slide.render_change_form)


]