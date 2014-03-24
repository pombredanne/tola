from django.forms import widgets
from rest_framework import serializers
from feed.models import Feed
from silo.models import ValueStore,Silo,DataField
from django.contrib.auth.models import User



class FeedSerializer(serializers.ModelSerializer):
	source = serializers.HyperlinkedIdentityField(view_name='api_root',format="html")
	class Meta:
		model = Silo  
		fields = ('owner','name','source','description','create_date')

class FeedInstanceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ValueStore
        fields = ('field','char_store','create_date','edit_date')
 