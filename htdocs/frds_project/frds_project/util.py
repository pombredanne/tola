import dicttoxml,json
import unicodedata

#CREATE NEW DATA DICTIONARY OBJECT 
def siloToDict(silo):
	parsed_data = {}
	key_value = 1
	for d in silo:
		label = unicodedata.normalize('NFKD', d.field.name).encode('ascii','ignore')
		value = unicodedata.normalize('NFKD', d.char_store).encode('ascii','ignore')
		parsed_data[key_value] = {label : value}
		
		key_value = key_value + 1
		
		print parsed_data
	
	return parsed_data	


