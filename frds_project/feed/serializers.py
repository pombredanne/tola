from django.forms import widgets
from rest_framework import serializers
from silo.models import ValueStore
from django.contrib.auth.models import User



class FeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = ValueStore
