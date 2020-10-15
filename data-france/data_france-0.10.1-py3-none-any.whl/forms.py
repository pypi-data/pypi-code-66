from django import forms

from data_france.models import Commune


class CommuneParametresForm(forms.Form):
    q = forms.CharField(required=True)
    geojson = forms.BooleanField(required=False)
    type = forms.MultipleChoiceField(choices=Commune.TYPE_CHOICES, required=False,)


class ParCodeParametresForm(forms.Form):
    code = forms.CharField(required=True)
    geojson = forms.BooleanField(required=False)


class CommuneParCodeParametresForm(ParCodeParametresForm):
    type = forms.ChoiceField(choices=Commune.TYPE_CHOICES, required=True)
