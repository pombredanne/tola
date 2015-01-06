from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from silo.models import Silo
from oauth2client.django_orm import CredentialsField

class GoogleCredentialsModel(models.Model):
    id = models.ForeignKey(User, primary_key=True, related_name='google_credentials')
    credential = CredentialsField()