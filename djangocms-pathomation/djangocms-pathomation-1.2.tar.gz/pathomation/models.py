from django.db import models
from cms.models import CMSPlugin
from django.utils import timezone
from django.core.exceptions import ValidationError
from pma_python import core, control
from django.shortcuts import render
from pma_python import core
import requests
from django.utils.translation import gettext_lazy as _
from django import forms




def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)


class Setting(models.Model):
    def clean(self):
        validate_only_one_instance(self)


    title = "My Pathomation connection settings"

    def __str__(self):
        return self.title



    PMACoreUsername = models.CharField(max_length=100, verbose_name='Email address')
    PMACorePassword =  models.CharField(max_length=100, verbose_name='Password')


class Slide(CMSPlugin):

    image_path= models.CharField(default="",max_length=200)


    def __str__(self):
        return self.image_path



    def user():
        try:
            for x in Setting.objects.all():
                return x.PMACoreUsername
        except:
            pass

    def password():
        try:
            for x in Setting.objects.all():
                return x.PMACorePassword
        except:
            pass



    user = user()
    password = password()



    headers = {
        'Accept': 'application/json',
    }

    data = {
        'grant_type': 'password',
        'client_id': '6',
        'client_secret': '9APfPpHZMoDKe6ECVYweIrAaopFXVqOSlsrfNGam',
        'username': user,
        'password': password,
        'scope': '*'
    }

    auth= requests.post('https://myapi.pathomation.com/oauth/token', headers=headers, data=data)

    try:
        accestoken =auth.json()['access_token']
    except:
        accestoken = ""

    headers2 = {
        'Accept': 'application/json',
        'Authorization': "Bearer " + accestoken,
    }

    params2 = (
        ('caller', 'Plugin Django'),
    )


    response = requests.get('https://myapi.pathomation.com/api/v1/authenticate?caller=Plugin Django', headers=headers2)

    try:
        folder = response.json()['folder']
        selected_nodes = response.json()['selected_nodes'][0]['Uri'] + "/"
        session_ID = response.json()['session_id']
    except:
        folder = ""
        selected_nodes = ""
        session_ID = ""

    sessionID = session_ID
    link = selected_nodes





