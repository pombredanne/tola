from django.contrib import admin
from silo.models import Silo,DataField,DataValue,ValueStore,ValueType

admin.site.register(Silo)
admin.site.register(DataField)
admin.site.register(DataValue)
admin.site.register(ValueStore)
admin.site.register(ValueType)