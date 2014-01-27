import django_tables2 as tables
from silo.models import ValueStore

TEMPLATE = '''
   <a href="/value_edit/{{ record.id }}" class="tbl_icon edit">Edit</a>
   <a href="/value_delete/{{ record.id }}" class="tbl_icon delete">Delete</a>
'''

class SiloTable(tables.Table):
	column_name = tables.TemplateColumn(TEMPLATE)
	class Meta:
		model = ValueStore
		attrs = {"class": "paleblue"}