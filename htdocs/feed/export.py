from import_export import resources
from .models import Silo
from import_export.admin import ImportExportModelAdmin


class SiloResource(resources.ModelResource):

    class Meta:
        model = Silo


class SiloAdmin(ImportExportModelAdmin):
    resource_class = SiloResource
    pass