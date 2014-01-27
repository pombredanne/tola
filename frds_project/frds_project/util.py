import dicttoxml,json
import unicodedata

#CREATE NEW DATA DICTIONARY OBJECT 
def siloToDict(silo):
	parsed_data = {}
	key_value = 1
	for d in silo:
		label = unicodedata.normalize('NFKD', d.field.name).encode('ascii','ignore')
		if d.value_type.value_type == "Char":
			value = unicodedata.normalize('NFKD', d.char_store).encode('ascii','ignore')
		elif d.value_type.value_type == "Int":
			value = unicodedata.normalize('NFKD', d.int_store).encode('ascii','ignore')
		elif d.value_type.value_type == "Bool":
			value = unicodedata.normalize('NFKD', d.bool_store).encode('ascii','ignore')
	
		parsed_data[key_value] = {label : value}
		
		key_value = key_value + 1
		
		print parsed_data
	
	return parsed_data	


