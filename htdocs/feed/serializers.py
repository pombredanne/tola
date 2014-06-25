from django.forms import widgets
from rest_framework import serializers
from feed.models import Feed
from silo.models import ValueStore,Silo,DataField
from django.contrib.auth.models import User


class SiloSerializer(serializers.HyperlinkedModelSerializer):
	fields = serializers.HyperlinkedIdentityField(view_name='field-list',format="html")
	id = serializers.HyperlinkedIdentityField(view_name='feed-detail',format="html")
	class Meta:
		model = Silo
		fields = ('owner','name','source','description','create_date','id','fields')
		depth =1

class DataFieldSerializer(serializers.HyperlinkedModelSerializer):
    data = serializers.HyperlinkedIdentityField(view_name='value-list', format='html')
    class Meta:
        model = DataField
        fields = ('silo','name','is_uid','create_date','edit_date','data')
        depth=1

class ValueStoreSerializer(serializers.HyperlinkedModelSerializer):
    fields = serializers.HyperlinkedIdentityField(view_name='field-list', format='html')
    class Meta:
        model = ValueStore
        fields = ('field','char_store','create_date','edit_date','fields')
