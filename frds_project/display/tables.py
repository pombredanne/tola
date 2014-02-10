import django_tables2 as tables
from silo.models import ValueStore

TEMPLATE = '''
   <a href="/value_edit/{{ record.id }}" class="tbl_icon edit">Edit</a>
   <a href="/value_delete/{{ record.id }}" class="tbl_icon delete">Delete</a>
'''

TEMPLATE2 = '''
   <a href="/field_edit/{{ record.field.id }}" class="tbl_icon edit">{{record.field}}</a>
'''

class SiloTable(tables.Table):
	edit = tables.TemplateColumn(TEMPLATE)
	field = tables.TemplateColumn(TEMPLATE2)
	class Meta:
		model = ValueStore
		attrs = {"class": "paleblue"}