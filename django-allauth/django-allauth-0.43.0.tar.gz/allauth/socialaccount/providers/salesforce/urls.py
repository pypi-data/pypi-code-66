from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import SalesforceProvider


urlpatterns = default_urlpatterns(SalesforceProvider)
